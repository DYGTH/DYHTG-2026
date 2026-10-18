import { LeftArrowButton, RightArrowButton, NoButton, YesButton } from './BinaryButtons';

export function DisplayDecision({ decision }) {
  if (!decision) {
    return <p>Waiting for the next decision...</p>;
  }
  return (
    <section>
        <h3>{ decision.type } </h3>
        <p>{ decision.title }</p>
        <p>{ decision.description }</p>
    </section>
  );
}

export function DisplayButtons({ decision, onAnswer }) {
    if (!decision) {
      return null;
    }
    if (decision.type == "binary") {
      return(<div><YesButton onClick={() => onAnswer(true)}/><NoButton onClick={() => onAnswer(false)}/></div>);
    }
    return(<div><LeftArrowButton onClick={() => onAnswer(-1)}/><RightArrowButton onClick={() => onAnswer(1)}/></div>);
}
