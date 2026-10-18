import { Assistant } from "../components/Assistant";
import { LeftArrowButton, YesButton } from "../components/BinaryButtons";
import { RightArrowButton, NoButton } from "../components/BinaryButtons";
import { SpeechBubble } from "../components/SpeechBubble";
import { Statistics } from "../components/Statistics";

export default function GamePage() {
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
             <SpeechBubble speech="Mr. President. We are in a demo. Should we ship to prod?" />
            <Assistant/>
            <YesButton/>
            <NoButton/>
        </div>
    )

}