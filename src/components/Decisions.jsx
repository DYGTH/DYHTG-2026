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

function ScaleAmount({ amount, confirmMs }) {
  if (amount === null) {
    return (
      <div className="amount">
        <span className="amount-value">0</span>
        <span className="amount-hint">Use the left and right arrow keys</span>
      </div>
    );
  }
  return (
    <div className="amount">
      <span className="amount-value">{amount > 0 ? `+${amount}` : amount}</span>
      <div className="amount-timer">
        <div key={amount} className="amount-timer-fill" style={{ animationDuration: `${confirmMs}ms` }} />
      </div>
    </div>
  );
}

export function DisplayButtons({ decision, onAnswer, onNudge, amount, confirmMs, disabled }) {
    if (!decision) {
      return null;
    }
    if (decision.type == "binary") {
      return(<div className="actions"><YesButton disabled={disabled} onClick={() => onAnswer(true)}/><NoButton disabled={disabled} onClick={() => onAnswer(false)}/></div>);
    }
    return(<div className="actions"><LeftArrowButton disabled={disabled} onClick={() => onNudge(-1)}/><ScaleAmount amount={amount} confirmMs={confirmMs}/><RightArrowButton disabled={disabled} onClick={() => onNudge(1)}/></div>);
}
