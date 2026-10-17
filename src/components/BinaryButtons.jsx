export function NoButton() {
    return (<button style =  {{
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

export function YesButton() {
    return (<button style =  {{
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