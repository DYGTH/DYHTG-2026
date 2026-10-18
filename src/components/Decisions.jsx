import { LeftArrowButton, RightArrowButton, NoButton, YesButton } from './BinaryButtons';
import { useState, useEffect } from 'react';


function getDecision() {
  const [decision, setDecision] = useState(null);
    useEffect(() => {
    fetch("http://localhost:8000/decision")
      .then(res => res.json())
      .then(data => setDecision(data.stats))
      .catch(err => console.error('Failed to load decision:', err));
    }, []);
    console.log(decision);
  return decision;
}

export function DisplayDecision({ decision }) {
  return (
    <section>
        <h3>{ decision.type } </h3>
        <p>{ decision.title }</p>
        <p>{ decision.description }</p>
    </section>
  );
}

export function DisplayButtons() {
    decision = getDecision();
    if (decision.type == "binary") {
      return(<div><YesButton/><NoButton/></div>);
    } else if (decision.type == "scalar") {
      return(<div><LeftArrowButton/><RightArrowButton/></div>);
    } else {
      return(<div><LeftArrowButton/><RightArrowButton/></div>)
    }
}

