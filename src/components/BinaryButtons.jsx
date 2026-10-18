import { useState } from "react";
import greenButtonImg from "../assets/green_button.png";
import greenButtonPressedImg from "../assets/green_button_pressed.png";
import redButtonImg from "../assets/red_button.png";
import redButtonPressedImg from "../assets/red_button_pressed.png";

export function NoButton({ onClick }) {
    const [clicked, setClicked] = useState(false);

    function handleClick() {
        if (onClick) onClick();
        setClicked(true);
        setTimeout(() => {
            setClicked(false);
        }, 1000);
    }

    return (
        <button 
            onClick={handleClick}
            style={{
                width: "120px",
                height: "70px",
                backgroundImage: `url(${clicked ? redButtonPressedImg : redButtonImg})`,
                backgroundSize: "cover",
                backgroundRepeat: "no-repeat",
                backgroundPosition: "center",
                border: "none",
                outline: "none",
                backgroundColor: "transparent",
                WebkitTapHighlightColor: "transparent",
                borderRadius: "10px",
                fontSize: "30px",
                alignSelf: "center",
                marginLeft: "20px",
            }}
        >
            No
        </button>
    );
}

export function YesButton({ onClick }) {
    const [clicked, setClicked] = useState(false);

    function handleClick() {
        if (onClick) onClick();
        setClicked(true);
        setTimeout(() => {
            setClicked(false);
        }, 1000);
    }

    return (
        <button 
            onClick={handleClick}
            style={{
                width: "120px",
                height: "70px",
                backgroundImage: `url(${clicked ? greenButtonPressedImg : greenButtonImg})`,
                backgroundSize: "cover",
                backgroundRepeat: "no-repeat",
                backgroundPosition: "center",
                border: "none",
                outline: "none",
                backgroundColor: "transparent",
                WebkitTapHighlightColor: "transparent",
                borderRadius: "10px",
                fontSize: "30px",
                alignSelf: "center",
                marginLeft: "20px",
            }}
        >
            Yes 
        </button>
    );
}

export function UpArrowButton() {
    return (<button></button>);
}

export function DownArrowButton() {
    return (<button></button>);
}

export function LeftArrowButton({ onClick }) {
    const [clicked, setClicked] = useState(false);

    function handleClick() {
        if (onClick) onClick();
        setClicked(true);
        setTimeout(() => {
            setClicked(false);
        }, 1000);
    }

    return (
        <button 
            onClick={handleClick}
            style={{
                width: "300px",
                height: "100px",
                background: clicked ? "#3D9910" : "#5EDC1F",
                borderRadius: "10px",
                fontSize: "30px",
                alignSelf: "center",
                marginRight: "20px",
            }}
        > 
            &larr; 
        </button>
    );
}

export function RightArrowButton({ onClick }) {
    const [clicked, setClicked] = useState(false);

    function handleClick() {
        if (onClick) onClick();
        setClicked(true);
        setTimeout(() => {
            setClicked(false);
        }, 1000);
    }

    return (
        <button 
            onClick={handleClick}
            style={{
                width: "300px",
                height: "100px",
                background: clicked ? "#A51020" : "#DC143C",
                borderRadius: "10px",
                fontSize: "30px",
                alignSelf: "center",
                marginLeft: "20px",
            }}
        > 
            &rarr; 
        </button>
    );
}