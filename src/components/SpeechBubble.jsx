export function SpeechBubble({ badge, title, text }) {
    return (
        <div className="panel bubble">
            {badge && <span className="badge">{badge}</span>}
            {title && <h3 className="bubble-title">{title}</h3>}
            <p className="bubble-text">{text}</p>
        </div>
    );
}
