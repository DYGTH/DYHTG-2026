import { useState, useEffect } from 'react';

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

export function Statistics() {
  const [statistics, setStatistics] = useState(DEFAULT_STATS);

  useEffect(() => {
    fetch("http://localhost:8000/stats")
      .then(res => res.json())
      .then(data => {
        console.log("Full API response:", data);
        
        if (data.stats && Object.keys(data.stats).length > 0) {
          setStatistics(data.stats);
        } else {
          console.warn("Backend returned empty stats, keeping DEFAULT_STATS");
        }
      })
      .catch(err => console.error('Failed to load statistics:', err));
  }, []);

  return (
    <div>
      {statistics ? (
        <ul>
          {Object.entries(statistics).map(([key, value]) => (
            <li key={key}>
              <strong>{key}:</strong> {value}
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading JSON data...</p>
      )}
    </div>
  );
}