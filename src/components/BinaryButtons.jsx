import {useState} from "react";

export function NoButton() {
    const [ clicked, setClicked] =useState(false);

    function handleClick(){
        setClicked(true);
        setTimeout(() => {
            setClicked(false)
     }, 1000);

    }
    return (<button 
        // onClick = { () => setClicked(true)}
        onClick = {handleClick}
        style =  {{
        width: "120px",
        height: "70px ",
        background: clicked ? "#A51020" :"#DC143C ",
        borderRadius: "10px",
        fontSize: "30px",
        // alignments
        alignself: "center",
        marginLeftt: "20px",
        //placeItems: " center",
        // justifyContent: "center",
        // alighItems: "center",  
        }}> No </button>)
}

export function YesButton({onClick}) {
    //const [ clicked, setClicked] =useState(false);

    //function handleClick(){
    //    setClicked(true);
    //    setTimeout(() => {
    //        setClicked(false)
    // }, 1000);

    //}
    return (<button 
        onClick = {onClick} 
        style =  {{
        width: "120px",
        height: "70px",
        background: "#5EDC1F", 
        // clicked? "#3D9910" 
        borderRadius: "10px",
        fontSize: "30px",
        // alignment
        alignself: "center",
        marginRight: "20px",

     }}> Yes </button>)

}

// 
export function UpArrowButton() {
    return (<button></button>)
}

export function DownArrowButton() {
    return (<button></button>)
}

export function LeftArrowButton({ onClick }) {
    return (<button onClick={onClick}>&larr;</button>)
}



export function RightArrowButton({ onClick }) {
    return (<button onClick={onClick}>&rarr;</button>)
}