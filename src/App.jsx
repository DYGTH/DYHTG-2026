import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";import './App.css'
import MainMenu from './pages/MainMenu'
import GamePage from "./pages/GamePage";
import ErrorBoundary from "./components/ErrorBoundary";
import React, { Component } from "react";

class App extends Component {
    render() {
        const bg = {
            backgroundImage: `url("src/assets/game_bg.png")`,
            height: "100vh",
            // marginTop: "-70px",
            backgroundSize: "cover",
            backgroundRepeat: "no-repeat",
        };
        return (
            <ErrorBoundary>
    <div style={bg}>
 <Router>
      <Routes>
          <Route path="/" element={<MainMenu />} />
            <Route path="/GamePage" element={<GamePage />} />
      </Routes>
    </Router>
    
    <audio controls loop>
    <source src="/Choice Game Music.wav" type="audio/wav" />
</audio>
    </div>
   
    </ErrorBoundary> 
        );
    }
}

export default App;


// function App() {

//   return (
//     <ErrorBoundary>
    
//     <Router>
//       <Routes>
//           <Route path="/" element={<MainMenu />} />
//             <Route path="/GamePage" element={<GamePage />} />
//       </Routes>
//     </Router>
    
//     </ErrorBoundary> 
  
//   )
// }

// export default App;
