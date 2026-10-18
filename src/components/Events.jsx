import { LeftArrowButton, RightArrowButton, NoButton, YesButton } from './BinaryButtons';
import { useState, useEffect } from 'react';


function getEvent() {
  const [event, setEvent] = useState(null);
    useEffect(() => {
    fetch("http://localhost:8000/events")
      .then(res => res.json())
      .then(data => setEvent(data.stats))
      .catch(err => console.error('Failed to load event:', err));
    }, []);
    console.log(event);
  return event;
}

export function DisplayEvent({ event }) {
  return (
    <section>
        <h3>{ event.type } </h3>
        <p>{ event.title }</p>
        <p>{ event.description }</p>
    </section>
  );
}

export function DisplayButtons() {
    event = getEvent();
    if (event.type == "binary") {
      return(<div><YesButton/><NoButton/></div>);
    } else if (event.type == "scalar") {
      return(<div><LeftArrowButton/><RightArrowButton/></div>);
    } else {
      return(<div><LeftArrowButton/><RightArrowButton/></div>)
    }
}

