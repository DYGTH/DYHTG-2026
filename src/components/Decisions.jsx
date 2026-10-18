import { LeftArrowButton, RightArrowButton, NoButton, YesButton } from './BinaryButtons';
import { SpeechBubble } from './SpeechBubble';

export function DisplayDecision({ decision }) {
  if (!decision) {
    return <SpeechBubble text="Waiting for the next decision..." />;
  }
  return (
    <SpeechBubble badge={decision.type} title={decision.title} text={decision.description} />
  );
}

export function DisplayButtons({ decision, onAnswer, disabled }) {
    if (!decision) {
      return null;
    }
    if (decision.type == "binary") {
      return(<div className="actions"><YesButton disabled={disabled} onClick={() => onAnswer(true)}/><NoButton disabled={disabled} onClick={() => onAnswer(false)}/></div>);
    }
    return(<div className="actions"><LeftArrowButton disabled={disabled} onClick={() => onAnswer(-1)}/><RightArrowButton disabled={disabled} onClick={() => onAnswer(1)}/></div>);
}
