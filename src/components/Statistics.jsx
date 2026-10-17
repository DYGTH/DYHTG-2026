import { useState, useEffect } from 'react';

export function Statistics() {
    
    const [statistics, setStatistics] = useState(null);
    useEffect(() => {
    fetch("../api/fake_stats.json")
      .then(res => res.json())
      .then(data => setStatistics(data))
      .catch(err => console.error('Failed to load statistics:', err));
    }, []);
    if (!statistics) return <div>Loading...</div>;
    return (
    //     <div className="w-full">
    //   {/* Events container */}
    //   <div className="flex flex-col rounded-sm overflow-hidden bg-[#7dd854]/[0.06] border border-[#7dd854]/10">
    //     {events.map((statistic, index) => (
    //       <div><p>statistic</p></div>
    //     ))}
    //   </div>
    // </div>
    <pre>{JSON.stringify(statistics, null, 2)}</pre>
    )
}