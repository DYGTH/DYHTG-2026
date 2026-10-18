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

export function Statistics({ statistics }) {
  const shown = statistics && Object.keys(statistics).length > 0 ? statistics : DEFAULT_STATS;

  return (
    <div>
      <ul>
        {Object.entries(shown).map(([key, value]) => (
          <li key={key}>
            <strong>{key}:</strong> {value}
          </li>
        ))}
      </ul>
    </div>
  );
}
