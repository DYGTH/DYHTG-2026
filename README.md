# DYHTG-2026: Resources Game

A turn-based civilisation game about managing resources against pollution. You run a growing civilisation, and every turn you make a few decisions. Grow too fast and the pollution you create comes back to hurt you. The game ends when your population reaches zero.

## What the game is

Each turn you get a handful of decisions, answered with a slider ("scales"):

- **Buy / sell** food, wood and stone.
- **Build / demolish** factories, farms, sawmills and quarries (they cost money, wood, stone and land, and they pollute).
- **Tame / free wild land** to make it buildable, at the cost of more pollution.
- **Random special events** (25% chance per turn): a drought, a wood fungus or a mineshaft collapse cuts production for a few turns, and you choose whether to buy the resource or build to fix it.

At the end of each turn the civilisation updates (production, population, happiness) and its buildings add to the world's pollution. Happiness and population decide how many moves you get next turn. Depollutinators are the only building that reduces pollution.

## Architecture

```
React frontend  --HTTP/JSON-->  FastAPI backend  -->  exposure.py  -->  game engine
 (Vite, :5173)                    (:8000)             (bridge)          (apps/src/game.py)
```

The game engine is a plain Python loop that blocks while it waits for the player's choice. The backend runs it in a background thread. `exposure.py` is the hand-off point: the engine puts the current decision and stats there, and the API reads them and writes the player's answer back.

| Part | Where | Tech |
| --- | --- | --- |
| Frontend | [src/](src/) | React 19, Vite, React Router, Tailwind CSS |
| HTTP API | [apps/backend/app/](apps/backend/app/) | FastAPI, Pydantic, Uvicorn |
| Game engine | [apps/src/](apps/src/) | Plain Python (game loop, decisions, save/load) |
| Game models | [apps/src/shared_types/](apps/src/shared_types/) | Civilisation, World, Decision, Choice, stats |
| Packaging | Dockerfile, Dockerfile.backend, docker-compose.yml | Docker, nginx |

### API

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/health` | Health check |
| GET | `/stats` | Current civilisation stats |
| GET | `/turn` | Current turn number |
| GET | `/decision` | The decision waiting for the player (404 if none) |
| POST | `/decision` | Send the answer, body `{"choise_answer": <number>}`. Returns `alive` and the new `stats` |

Interactive docs are at http://localhost:8000/docs when the backend is running.

## Running it

### With Docker

```
docker compose up --build
```

Frontend at http://localhost:5174, API at http://localhost:8000.

### Without Docker

Backend (from the repo root):

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd apps/backend
uvicorn app.main:app --port 8000
```

Frontend (in a second terminal, from the repo root):

```
npm install
npm run dev
```

Open http://localhost:5173. The frontend expects the API at `http://localhost:8000`.

## Project layout

```
src/                 React app (pages, components, assets)
apps/backend/app/    FastAPI app (routes, schemas, game_service)
apps/src/            Game engine and bridge to the API
save/                Saved game state (pickle files)
public/              Static files, including the soundtrack
```
