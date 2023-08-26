import React from 'react';

const Terminal = ({text}) => {
  const terminalStyle = {
    backgroundColor: '#000',
    color: '#33FF00',
    padding: '20px',
    borderRadius: '10px',
    fontFamily: 'Courier, monospace',
    fontSize: '16px',
    lineHeight: '24px',
    width: '80%',
    margin: '0 auto',
    textAlign: 'left',
  };

  const promptStyle = {
    color: '#FF4500',
  };

  return (
    <div style={terminalStyle}>
      <span style={promptStyle}>$ </span>
      {text}
    </div>
  );
};

export default Terminal;
