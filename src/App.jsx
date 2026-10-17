import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";import './App.css'
import MainMenu from './pages/MainMenu'
import GamePage from "./pages/GamePage";
import ErrorBoundary from "./components/ErrorBoundary";


function App() {

  return (
    <ErrorBoundary>
    <Router>
      <Routes>
          <Route exact path="/" element={<MainMenu />} />
          <Route path="/game" element={<GamePage />} />
      </Routes>
    </Router>
    </ErrorBoundary>
  )
}

export default App
