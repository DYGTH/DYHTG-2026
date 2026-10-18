export function Statistics({ statistics }) {
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
