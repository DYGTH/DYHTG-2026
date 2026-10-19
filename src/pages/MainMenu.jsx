import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { YesButton, NoButton } from "../components/BinaryButtons";
import mainPageImg from "./mainPage.jpg";

export default function MainMenu() {
    const nav = useNavigate();
    const [declined, setDeclined] = useState(false);

    return (
        <div
            className="page menu"
            style={{
                backgroundImage: `url(${mainPageImg})`,
                backgroundSize: "cover",
                backgroundPosition: "center bottom",
            }}
        >
            <h1 className="title">Mr. President</h1>

            <div className="panel">
                <h2>Start game?</h2>
                <p className="muted">
                    {declined ? "The nation can wait. For now." : "The country needs a leader."}
                </p>
                <div className="actions">
                    <YesButton onClick={() => nav("/GamePage")} />
                    <NoButton onClick={() => setDeclined(true)} />
                </div>
            </div>
        </div>
    );
}
