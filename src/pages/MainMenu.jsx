import { YesButton } from "../components/BinaryButtons"
import { NoButton } from "../components/BinaryButtons"



export default function MainMenu() {
    return (
        
        <div style = {{
            display: "flex",
            flexDirection: "column",
            justifyContent:"center",
            // textAlign:"center",
            alignItems: "center",
            position: 'absolute',
            minHeight: "100vh",
            gap: "20px",
            width: "100%"
            }}>

            <h1> Start game? </h1>

            <div style ={{
                display:"flex",
                flexDirection: "row",
                gap: "20px",

            }}>

            <YesButton/>
            <NoButton/>
            </div>
        </div>
    )

}
