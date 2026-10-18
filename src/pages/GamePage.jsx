import { useState, useEffect } from "react";
import { Assistant } from "../components/Assistant";
import { LeftArrowButton, YesButton } from "../components/BinaryButtons";
import { RightArrowButton, NoButton } from "../components/BinaryButtons";
import { SpeechBubble } from "../components/SpeechBubble";
import { Statistics } from "../components/Statistics";
import { DisplayButtons, DisplayDecision } from "../components/Decisions";

const API = "http://localhost:8000";

export default function GamePage() {
    const [statistics, setStatistics] = useState(null);
    const [decision, setDecision] = useState(null);
    const [alive, setAlive] = useState(true);

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

    const answer = value =>
        fetch(`${API}/decision`, {
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
            .catch(err => console.error("Failed to send choice:", err));

    return (


        <div style = {{
            minHeight: "100vh",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            position: "relative",
            padding: "20px",
            boxSizing: "border-box",
        }}>


            <div style = {{   
            textAlign: " center",         
            }}>

            <h2>Statistics</h2>
            <Statistics/>
            </div>


            <div script = {{ 
                display: "flex",
                flexDirection: "column",
                justifyContent:"center",
                // textAlign:"center",
                alignItems: "center",
                position: 'absolute',
                minHeight: "100vh",
                gap: "20px",
                width: "100%"}}> 

            <SpeechBubble speech="Mr. President. We are in a demo. Should we ship to prod?" />
            </div>



            <div script= {{ 
                    display: "flex",
                    flexDirection: "row",
                    justifyContent: "center",
                    gap: "20px"}}> 
            <YesButton/>
            <NoButton/>
            </div>

        </div>
    )

}
