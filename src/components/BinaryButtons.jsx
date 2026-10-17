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
        width: "300px",
        height: "100px ",
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

export function YesButton() {
    const [ clicked, setClicked] =useState(false);

    function handleClick(){
        setClicked(true);
        setTimeout(() => {
            setClicked(false)
     }, 1000);

    }
    return (<button 
        onClick = {handleClick}
        style =  {{
        width: "300px",
        height: "100px",
        background: clicked? "#3D9910" : "#5EDC1F",
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

export function LeftArrowButton() {
    return (<button class="width: 0;
	height: 0;
	border-top: 25px solid transparent;
	border-right: 50px solid #555;
	border-bottom: 25px solid transparent;"></button>)
}

export function RightArrowButton() {
    return (<button class="width: 0;
	height: 0;
	border-top: 25px solid transparent;
	border-left: 50px solid #555;
	border-bottom: 25px solid transparent;"></button>)
}