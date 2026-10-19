import { ICONS, formatLabel, formatValue } from "../statMeta";

const GROUPS = [
    { title: "Resources", keys: ["money", "food", "wood", "stone"] },
    { title: "People", keys: ["population", "happiness"] },
    { title: "Buildings", keys: ["factories", "farms", "sawmills", "quarries", "depollutinators"] },
    { title: "Land and climate", keys: ["available_land", "wild_land", "pollution"] },
];

const HIGH_IS_BAD = ["pollution"];

const round = value => Math.round(value * 10) / 10;

function signed(value) {
    const text = formatValue(Math.abs(round(value)));
    if (round(value) > 0) return `+${text}`;
    if (round(value) < 0) return `−${text}`;
    return text;
}

function tone(name, total) {
    if (round(total) === 0) return "none";
    return (total > 0) === HIGH_IS_BAD.includes(name) ? "bad" : "good";
}

function arrow(total) {
    if (round(total) > 0) return "▲";
    if (round(total) < 0) return "▼";
    return "•";
}

function breakdown(change) {
    const parts = [];
    if (round(change.choices) !== 0) parts.push(`choices ${signed(change.choices)}`);
    if (round(change.production) !== 0) parts.push(`production ${signed(change.production)}`);
    return parts.join(" · ") || "no change";
}

function ChangeRow({ name, change }) {
    return (
        <div className={`change change-${tone(name, change.total)}`}>
            <span className="change-icon">{ICONS[name] ?? "📊"}</span>
            <div>
                <span className="change-label">{formatLabel(name)}</span>
                <span className="change-detail">{breakdown(change)}</span>
            </div>
            <div className="change-numbers">
                <span className="change-total">{arrow(change.total)} {signed(change.total)}</span>
                <span className="change-now">now {formatValue(change.end)}</span>
            </div>
        </div>
    );
}

export function TurnSummary({ summary, alive, onContinue }) {
    return (
        <div className="panel summary">
            <div className="summary-head">
                <span className="badge">Turn {summary.turn}</span>
                <h2>Turn complete</h2>
                <p>Here is what changed in your civilisation</p>
            </div>

            {GROUPS.map((group, index) => (
                <section key={group.title} className="summary-group" style={{ "--i": index }}>
                    <h3>{group.title}</h3>
                    <div className="summary-rows">
                        {group.keys.filter(key => summary.stats[key]).map(key => (
                            <ChangeRow key={key} name={key} change={summary.stats[key]} />
                        ))}
                    </div>
                </section>
            ))}

            <button className="link-button" autoFocus onClick={onContinue}>
                {alive ? "Next turn" : "Continue"}
            </button>
        </div>
    );
}
