import React, { useState, useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSpinner } from '@fortawesome/free-solid-svg-icons';
import "@fortawesome/fontawesome-svg-core/styles.css";
import './App.css';  // Assuming you added the CSS in App.css

const App = () => {
  const [ws, setWs] = useState(null);
  const [message, setMessage] = useState("");
  const [received, setReceived] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setWs(new WebSocket('ws://localhost:8000/ws'));
  }, []);

  useEffect(() => {
    if (ws) {
      ws.onmessage = evt => {
        setReceived(evt.data);
        setLoading(false);
      };
    }
  }, [ws]);

  const handleChange = (e) => {
    setMessage(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && message.trim() !== "") {
      handleSubmit();
    }
  };

  const handleSubmit = () => {
    if (ws && message.trim() !== "") {
      setLoading(true);
      ws.send(message);
      setMessage("");
    }
  };

  const handlePredefinedSubmit = () => {
    if (ws) {
      setLoading(true);
      ws.send('...and then?');
    }
  };

  return (
    <div className="container py-5">
      <h1 className="mb-4">Storytime with Evandor the Fablemaster</h1>
      <div className="card">
        <div className="card-body">
          <p className="card-text"><b>Evandor:</b> {received}</p>
        </div>
        <div className="input-group">
          <input
            className="form-control"
            value={message}
            onChange={handleChange}
            onKeyPress={handleKeyPress}
            placeholder="Say something..."
          />
          <div className="input-group-append">
            <button
              className="btn btn-primary"
              onClick={handleSubmit}
              disabled={loading}
            >
              Submit
            </button>
            <button
              className="btn btn-secondary"
              onClick={handlePredefinedSubmit}
              disabled={loading}
            >
              ...and then?
            </button>
          </div>
        </div>
        {loading && (
          <div className="text-center mt-3">
            <FontAwesomeIcon
              icon={faSpinner}
              style={{ 
                marginRight: '0.5rem',
                animation: 'spin 2s linear infinite'
              }}
            />
            Thinking...
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
