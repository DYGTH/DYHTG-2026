import { useEffect, useRef } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import MainMenu from "./pages/MainMenu";
import GamePage from "./pages/GamePage";
import ErrorBoundary from "./components/ErrorBoundary";
import gameBg from "./assets/game_bg.png";

function App() {
    const audioRef = useRef(null);

    useEffect(() => {
        const audio = audioRef.current;
        if (!audio) return;

        const playAudio = () => {
            if (audio.paused) {
                audio.play().catch(() => {});
            }
        };

        const promise = audio.play();
        if (promise !== undefined) {
            promise.catch(() => {
                window.addEventListener("pointerdown", playAudio, { once: true });
                window.addEventListener("keydown", playAudio, { once: true });
            });
        }
    }, []);

    return (
        <ErrorBoundary>
            <div className="app" style={{ backgroundImage: `url(${gameBg})` }}>
                <audio ref={audioRef} loop autoPlay style={{ display: "none" }}>
                    <source src="/Choice Game Music.wav" type="audio/wav" />
                </audio>
                <Router>
                    <Routes>
                        <Route path="/" element={<MainMenu />} />
                        <Route path="/GamePage" element={<GamePage />} />
                    </Routes>
                </Router>
            </div>
        </ErrorBoundary>
    );
}

export default App;