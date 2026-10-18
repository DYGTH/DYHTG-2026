import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Assistant } from "../components/Assistant";
import { Statistics } from "../components/Statistics";
import { DisplayButtons, DisplayDecision } from "../components/Decisions";

const API = "http://localhost:8000";

export default function GamePage() {
    const [statistics, setStatistics] = useState(null);
    const [decision, setDecision] = useState(null);
    const [alive, setAlive] = useState(true);
    const [busy, setBusy] = useState(false);

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
                return loadDecision();
            })
            .catch(err => console.error("Failed to send choice:", err))
            .finally(() => setBusy(false));
    };

    return (
        <div className="page game">
            <Statistics statistics={statistics} />

            {alive ? (
                <>
                    <div className="scene">
                        <Assistant />
                        <DisplayDecision decision={decision} />
                    </div>
                    <DisplayButtons decision={decision} onAnswer={answer} disabled={busy} />
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
