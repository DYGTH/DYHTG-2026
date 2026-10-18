export function SpeechBubble({ speech }){
    return (
        <div style= {{

             backgroundColor: "lightgrey",
             width: "250px",
             border: "5px solid chocolate",
             padding: "30px ",
             margin: "20px" ,
            //  marginRight: "190px",
        }}> <p>{speech}</p>
            
         </div>
    )
}