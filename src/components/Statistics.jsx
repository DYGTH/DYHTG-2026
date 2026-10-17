import { useState, useEffect } from 'react';

export function Statistics() {
    
    const [statistics, setStatistics] = useState(null);
    useEffect(() => {
    fetch("../api/fake_stats.json")
      .then(res => res.json())
      .then(data => setStatistics(data))
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
    )
}