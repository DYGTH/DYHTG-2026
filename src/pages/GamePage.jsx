import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Assistant } from "../components/Assistant";
import { Statistics } from "../components/Statistics";
import { DisplayButtons, DisplayDecision } from "../components/Decisions";
import { TurnSummary } from "../components/TurnSummary";

const API = "http://localhost:8000";
const CONFIRM_MS = 3000;

export default function GamePage() {
    const [statistics, setStatistics] = useState(null);
    const [decision, setDecision] = useState(null);
    const [alive, setAlive] = useState(true);
    const [busy, setBusy] = useState(false);
    const [amount, setAmount] = useState(null);
    const [summary, setSummary] = useState(null);

    const loadDecision = () =>
        fetch(`${API}/decision`)
            .then(res => (res.ok ? res.json() : null))
            .then(setDecision)
            .catch(err => console.error("Failed to load decision:", err));

    useEffect(() => {
        fetch(`${API}/stats`)
            .then(res => res.json())
            .then(data => setStatistics(data.stats))
            .catch(err => console.error("Failed to load statistics:", err));
        loadDecision();
    }, []);

    const answer = value => {
        setAmount(null);
        setBusy(true);
        return fetch(`${API}/decision`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ choise_answer: value }),
        })
            .then(res => (res.ok ? res.json() : Promise.reject(new Error(res.status))))
            .then(data => {
                setStatistics(data.stats);
                setAlive(data.alive);
                setSummary(data.summary);
                return loadDecision();
            })
            .catch(err => console.error("Failed to send choice:", err))
            .finally(() => setBusy(false));
    };

    const nudge = direction => setAmount(current => (current ?? 0) + direction);

    const scaling = alive && !busy && !summary && decision?.type === "scales";

    useEffect(() => {
        if (!scaling) return;
        const onKeyDown = event => {
            const direction = { ArrowLeft: -1, ArrowRight: 1 }[event.key];
            if (!direction) return;
            event.preventDefault();
            nudge(direction);
        };
        window.addEventListener("keydown", onKeyDown);
        return () => window.removeEventListener("keydown", onKeyDown);
    }, [scaling]);

    useEffect(() => {
        if (amount === null) return;
        const timer = setTimeout(() => answer(amount), CONFIRM_MS);
        return () => clearTimeout(timer);
    }, [amount]);

    return (
        <div className="page game">
            <Statistics statistics={statistics} />

            {summary ? (
                <TurnSummary summary={summary} alive={alive} onContinue={() => setSummary(null)} />
            ) : alive ? (
                <>
                    <div className="scene">
                        <Assistant />
                        <DisplayDecision decision={decision} />
                    </div>
                    <DisplayButtons decision={decision} onAnswer={answer} onNudge={nudge} amount={amount} confirmMs={CONFIRM_MS} disabled={busy} />
                </>
            ) : (
                <div className="panel game-over">
                    <h2>Game over</h2>
                    <p>Your term has come to an end.</p>
                    <Link to="/" className="link-button">Back to menu</Link>
                </div>
            )}
        </div>
    );
}
