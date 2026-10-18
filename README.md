# Mr. President

A turn-based nation-management game. You run a small country: every turn the advisor puts a handful of decisions in front of you, and you answer each with the arrow keys. Keep your people fed and happy, don't bury the planet in smog, and stay in office as long as you can. The game ends when your population drops below 1.

The frontend is React + Vite. The backend is a FastAPI service that runs the game engine and exposes it over HTTP.

## Running it

You need Node.js and Python 3.

Backend (from the repo root):

```bash
pip install -r requirements.txt
cd apps/backend
uvicorn app.main:app --port 8000
```

Frontend (from the repo root, in a second terminal):

```bash
npm install
npm run dev
```

Open http://localhost:5173.

Or run both with Docker:

```bash
docker compose up --build
```

This serves the API on port 8000 and the built frontend on http://localhost:5174.

The frontend calls the API at `http://localhost:8000` (hardcoded in [src/pages/GamePage.jsx](src/pages/GamePage.jsx)), and the backend only allows CORS from ports 5173 and 5174.

## How to play

- **Binary decisions** are yes/no. Press ← for Yes or → for No.
- **Scales decisions** let you choose an amount. Press ← or → to nudge it down or up, once per notch.
- Your choice locks in 3 seconds after the last key press. The Yes and No buttons answer immediately, and the arrow buttons nudge the amount like the keys do.
- After each turn you get a summary showing how every stat changed from your choices and from production.

Each turn mixes:

- Build or demolish one of five buildings (factories, farms, sawmills, quarries, depollutinators).
- Buy or sell food, wood or stone at a randomly moody market price.
- Clear wild land for building, or rewild it.
- Policy events from a catalogue of 43 (taxes, loans, immigration, subsidies, festivals and so on). Many have lasting effects that play out over several turns, and some are gambles.
- A crisis, drawn from 12, with a chance of 20% plus 1% per turn, capped at 50%. Crises hit harder as turns go by.

Every turn has three standard decisions (market, land or building) plus 3 to 6 policy events, depending on your population and happiness.

### Stats

| Group | Stats |
| --- | --- |
| Civilisation | population, money, food, wood, stone, happiness, available land |
| Buildings | factories, farms, sawmills, quarries, depollutinators |
| World | pollution, wild land |

Each factory, farm, sawmill and quarry produces 1,000 of its resource per turn. Everyone eats 1 food a turn, and starvation shrinks the population. Buildings cost upkeep and pollute, pollution above 40 hurts happiness and population, and depollutinators clean it up. Happiness drifts towards 75, or towards 10 while people are hungry, and drives population growth.

## HTTP API

| Method | Path | Description |
| --- | --- | --- |
| GET | `/health` | Returns `{"status": "ok"}`. |
| GET | `/stats` | Returns `{"stats": {"population": 1000, "money": 1000, ...}}`. |
| GET | `/turn` | Returns `{"turn": 3}`. |
| GET | `/decision` | Returns the pending decision `{"title", "type", "description"}`, where `type` is `"binary"` or `"scales"`. Responds `404` if there is none yet. |
| POST | `/decision` | Answers the pending decision. Responds `{"alive", "stats", "summary"}`. |

The POST body is `{"choise_answer": true}` for a binary decision (`true` is Yes) or `{"choise_answer": 2}` for a scales decision (positive is up, negative is down, the magnitude is the number of notches). The key is spelled `choise_answer`. A wrong value type returns `400`, and answering when nothing is pending returns `404`.

`summary` is `null` unless the answer finished a turn. When it is set, it looks like:

```json
{
  "turn": 3,
  "stats": {
    "money": { "choices": -800, "production": 1000, "total": 200, "end": 1200 }
  }
}
```

Interactive docs are at http://localhost:8000/docs while the backend is running.

## Project layout

```
src/                     React frontend (pages, components, theme in index.css)
public/                  Music and icons
apps/
  backend/app/           FastAPI app: routes, schemas, game_service
  src/                   Game engine
    game.py                game loop, turn resolution
    decisions_generator.py builds each turn's decisions
    event_catalogue.py     policy events and crises
    effects.py             applies and prices effects
    exposure.py            state shared between engine and API
    save_and_load.py       pickles the game to save/
    shared_types/          Civilisation, World, stats, Decision, Choice
save/                    Autosave written at the end of each turn
```

The engine runs on a background thread that starts with the backend and blocks in [apps/src/exposure.py](apps/src/exposure.py) until the frontend posts an answer. The API reads and writes that module's state through [game_service.py](apps/backend/app/services/game_service.py). There is one game per server process, so restart the backend to start over.

## Development

```bash
npm run lint     # oxlint
npm run build    # production build into dist/
```

## License

GPL-3.0. See [LICENSE](LICENSE).
