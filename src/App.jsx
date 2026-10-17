import React from "react";
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";import './App.css'
import MainMenu from './pages/MainMenu'
import GamePage from "./pages/GamePage";


function App() {

  return (
    <Router>
      <Routes>
          <Route exact path="/" element={<MainMenu />} />
          <Route path="/game" element={<GamePage />} />
      </Routes>
    </Router>
  )
}

export default App
