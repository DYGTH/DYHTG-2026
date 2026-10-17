import { YesButton } from "../components/BinaryButtons"
import { NoButton } from "../components/BinaryButtons"



export default function MainMenu() {
    return (
        
        <div style = {{
            //display: "flex",
            justifyContent:"center",
            textAlign:"center",
            alignItems: "center",
            position: 'absolute',
            top: "30%",
            left: "16%"
            }}>

            <h1>Start Game?</h1>
            <YesButton/>
            <NoButton/>
        </div>
    )

}