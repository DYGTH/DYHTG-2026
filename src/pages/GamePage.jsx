import { YesButton } from "../components/BinaryButtons"
import { NoButton } from "../components/BinaryButtons"
import SpeechBubble from "../components/SpeechBubble"

export default function GamePage() {
    return (
        <div>
            <SpeechBubble />
            <YesButton/>
            <NoButton/>
        </div>
    )

}