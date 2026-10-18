import { Assistant } from "../components/Assistant";
// import { LeftArrowButton, YesButton } from "../components/BinaryButtons";
// import { NoButton } from "../components/BinaryButtons";
import { SpeechBubble } from "../components/SpeechBubble";
import { Statistics } from "../components/Statistics";
import { DisplayButtons, DisplayEvent } from "../components/Events";

export default function GamePage() {
    return (
        <div>
            <h2>Statistics</h2>
            <Statistics/>
             <SpeechBubble speech="Mr. President. We are in a demo. Should we ship to prod?" />
            <Assistant/>
            <DisplayButtons/>
        </div>
    )

}