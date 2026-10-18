export function NoButton({ onClick }) {
    return (<button onClick={onClick} style =  {{
        width: "500px",
        height: "100px ",
        background: "#DC143C ",
        borderRadius: "10px",
        // alignments
        alignself: "center",
        marginLeftt: "20px",
        //placeItems: " center",
        // justifyContent: "center",
        // alighItems: "center",  
        }}> No </button>)
}

export function YesButton({ onClick }) {
    return (<button onClick={onClick} style =  {{
        width: "500px",
        height: "100px",
        background: "#5EDC1F",
        borderRadius: "10px",
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