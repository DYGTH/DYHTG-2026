import { useState } from "react";
import greenButtonImg from "../assets/green_button.png";
import greenButtonPressedImg from "../assets/green_button_pressed.png";
import redButtonImg from "../assets/red_button.png";
import redButtonPressedImg from "../assets/red_button_pressed.png";
import leftButtonImg from "../assets/left_arrow.png";
import rightButtonImg from "../assets/right_arrow.png";

function ImageButton({ image, pressedImage = image, label, text, round, onClick, disabled }) {
    const [pressed, setPressed] = useState(false);

    return (
        <button
            className={round ? "image-button image-button-round" : "image-button"}
            aria-label={label}
            disabled={disabled}
            onClick={onClick}
            onPointerDown={() => setPressed(true)}
            onPointerUp={() => setPressed(false)}
            onPointerLeave={() => setPressed(false)}
            style={{ backgroundImage: `url(${pressed ? pressedImage : image})` }}
        >
            <span className="image-button-label">{text}</span>
        </button>
    );
}

export function YesButton(props) {
    return <ImageButton image={greenButtonImg} pressedImage={greenButtonPressedImg} label="Yes" text="Yes" round {...props} />;
}

export function NoButton(props) {
    return <ImageButton image={redButtonImg} pressedImage={redButtonPressedImg} label="No" text="No" round {...props} />;
}

export function LeftArrowButton(props) {
    return <ImageButton image={leftButtonImg} label="Decrease" {...props} />;
}

export function RightArrowButton(props) {
    return <ImageButton image={rightButtonImg} label="Increase" {...props} />;
}
