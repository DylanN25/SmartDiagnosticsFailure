import React from 'react';

function StatusBox({ title, children, id }) {
    return (
        <div className="status-box" id={id}>
            <h3>{title}</h3>
            <div>{children}</div>
        </div>
    );
}

export default StatusBox;
