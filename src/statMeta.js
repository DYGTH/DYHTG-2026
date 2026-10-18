export const ICONS = {
  population: "👥",
  money: "💰",
  food: "🌾",
  wood: "🪵",
  stone: "🪨",
  happiness: "😊",
  factories: "🏭",
  farms: "🚜",
  sawmills: "🪚",
  quarries: "⛏️",
  depollutinators: "🌬️",
  available_land: "🏞️",
  pollution: "☁️",
  wild_land: "🌲",
};

export function formatLabel(key) {
  return key.replace(/_/g, " ");
}

export function formatValue(value) {
  return Number.isInteger(value) ? value.toLocaleString() : value.toFixed(1);
}
