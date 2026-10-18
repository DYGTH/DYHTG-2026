import { YesButton } from "../components/BinaryButtons"
import { NoButton } from "../components/BinaryButtons"
import { useNavigate } from "react-router-dom" ;




export default function MainMenu() {
    const nav = useNavigate()

    const navigate = () => {
        nav("/GamePage")

    }
    return (
        
        <div style = {{
            // background image
            backgroundImage: "url(/src/pages/mainPage.jpg)" ,
            backgroundSize: "cover",
            backgroundPosition: "center",
            backgroundRepeat: "no-repeat",



            // general styling position
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

            <YesButton onClick = {navigate}/>
            <NoButton/>
            </div>
        </div>
    )

}
