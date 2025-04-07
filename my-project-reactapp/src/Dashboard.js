import React, { useState, useEffect } from 'react';
import StatusBox from './StatusBox';

function Dashboard() {
    const [data, setData] = useState({});
    const [ip, setIp] = useState("192.168.68.54");
    const [port, setPort] = useState("502");
    const [error, setError] = useState("");

    const updateModbusSettings = () => {
        fetch(`http://localhost:5000/update_data?ip=${ip}&port=${port}`)
            .then(response => response.json())
            .then(data => {
                console.log('Settings updated:', data);
                setData(data);
                setError("");
            })
            .catch(error => {
                console.error('Error al actualizar Modbus settings:', error);
                setError("Failed to update Modbus settings. Please try again.");
            });
    };

    useEffect(() => {
        const interval = setInterval(() => {
            updateModbusSettings(); // Actualiza automáticamente cada 2 segundos
        }, 2000);

        return () => clearInterval(interval); // Limpia el intervalo al desmontar el componente
    }, []); // Ejecuta solo una vez al montar el componente

    useEffect(() => {
        updateModbusSettings(); // Reacciona a los cambios en IP o puerto
    }, [ip, port]); // Observa cambios en ip y port



    const isValidIp = (ip) => /^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$/.test(ip);

    const isValidPort = (port) => parseInt(port) > 0 && parseInt(port) < 65536;

    const handleIpChange = (e) => {
        const newIp = e.target.value;
        if (isValidIp(newIp)) {
            setIp(newIp);
            setError("");
        } else {
            setError("Invalid IP address format.");
        }
    };

    const handlePortChange = (e) => {
        const newPort = e.target.value;
        if (isValidPort(newPort)) {
            setPort(newPort);
            setError("");
        } else {
            setError("Invalid port number. Must be between 1 and 65535.");
        }
    };

    return (
        <div>
            {/* Encabezado principal con nuevo diseño */}
            <header className="header">
                <h1>Failure Prediction Dashboard</h1>
            </header>

            <h1>Connection Settings for Modbus</h1>

            <div className="status-box">
                <h3>Modbus Settings</h3>
                <div className="config-container">
                    <label className="config-label">
                        Modbus IP:
                        <input
                            type="text"
                            value={ip}
                            onChange={handleIpChange}
                            className="config-input"
                        />
                    </label>
                    <label className="config-label">
                        Modbus Port:
                        <input
                            type="text"
                            value={port}
                            onChange={handlePortChange}
                            className="config-input"
                        />
                    </label>
                    {error && <p className="error-message">{error}</p>}
                </div>
            </div>

            <hr className="divider" />

            <div className="status-container">
                <StatusBox
                    title="Emergency Stop Status"
                    id="emergencyStatusText"
                    children={data.emergency_stop_status || 'Loading...'}
                />
                <StatusBox
                    title="System Status"
                    id="systemStatusText"
                    children={data.system_status || 'Loading...'}
                />
            </div>
            <div className="status-container">
                <StatusBox title="Potentiometer Values">
                    <p>Air temperature: {data.air_temperature || 'Loading...'} K</p>
                    <p>Process temperature: {data.process_temperature || 'Loading...'} K</p>
                    <p>Rotational speed: {data.rotational_speed || 'Loading...'} rpm</p>
                    <p>Torque: {data.torque || 'Loading...'} Nm</p>
                    <p>Tool wear: {data.tool_wear || 'Loading...'} min</p>
                </StatusBox>
                <div className="right-column">
                    <StatusBox
                        title="Prediction"
                        id="predictionText"
                        children={data.prediction || 'Loading...'}
                    />
                    <StatusBox
                        title="Message"
                        id="toolWearMessageText"
                        children={data.message || 'Loading...'}
                    />
                </div>
            </div>
        </div>
    );
}

export default Dashboard;
