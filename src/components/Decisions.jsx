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

function PendingChoice({ label, idle, confirmMs }) {
  if (label === null) {
    return (
      <div className="amount">
        <span className="amount-value">{idle}</span>
        <span className="amount-hint">Use the left and right arrow keys</span>
      </div>
    );
  }
  return (
    <div className="amount">
      <span className="amount-value">{label}</span>
      <div className="amount-timer">
        <div key={label} className="amount-timer-fill" style={{ animationDuration: `${confirmMs}ms` }} />
      </div>
    </div>
  );
}

export function DisplayButtons({ decision, onAnswer, onNudge, amount, confirmMs, disabled }) {
    if (!decision) {
      return null;
    }
    if (decision.type == "binary") {
      const label = amount === null ? null : amount < 0 ? "Yes" : "No";
      return(<div className="actions"><YesButton selected={label === "Yes"} disabled={disabled} onClick={() => onAnswer(true)}/><PendingChoice label={label} idle="?" confirmMs={confirmMs}/><NoButton selected={label === "No"} disabled={disabled} onClick={() => onAnswer(false)}/></div>);
    }
    return(<div className="actions"><LeftArrowButton disabled={disabled} onClick={() => onNudge(-1)}/><PendingChoice label={amount === null ? null : amount > 0 ? `+${amount}` : `${amount}`} idle="0" confirmMs={confirmMs}/><RightArrowButton disabled={disabled} onClick={() => onNudge(1)}/></div>);
}
