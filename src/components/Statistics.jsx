const DEFAULT_STATS = {
  population: 1000,
  money: 1000,
  food: 1000,
  happiness: 100,
  factories: 1,
  farms: 1,
  pollution: 0,
  wild_land: 100,
};

const ICONS = {
  population: "👥",
  money: "💰",
  food: "🌾",
  happiness: "😊",
  factories: "🏭",
  farms: "🚜",
  pollution: "☁️",
  wild_land: "🌲",
};

const LOW_IS_BAD = ["money", "food", "happiness", "wild_land"];

function formatLabel(key) {
  return key.replace(/_/g, " ");
}

function formatValue(value) {
  return Number.isInteger(value) ? value.toLocaleString() : value.toFixed(1);
}

export function Statistics({ statistics }) {
  const shown = statistics && Object.keys(statistics).length > 0 ? statistics : DEFAULT_STATS;

  return (
    <div className="hud">
      {Object.entries(shown).map(([key, value]) => (
        <div key={key} className={LOW_IS_BAD.includes(key) && value <= 0 ? "stat stat-low" : "stat"}>
          <span className="stat-icon">{ICONS[key] ?? "📊"}</span>
          <div>
            <span className="stat-label">{formatLabel(key)}</span>
            <span className="stat-value">{formatValue(value)}</span>
          </div>
        </div>
      ))}
    </div>
  );
}
