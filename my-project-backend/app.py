from flask import Flask, jsonify, request, render_template
from pymodbus.client import ModbusTcpClient
import joblib
import pandas as pd
import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


# Load model, preprocessor, and encoder from the "models" folder
loaded_model = joblib.load(os.path.join('models', 'trained_model.pkl'))
preprocessor = joblib.load(os.path.join('models', 'preprocessor.pkl'))
label_encoder = joblib.load(os.path.join('models', 'label_encoder.pkl'))

# Variable to simulate the emergency stop state
emergency_stop_active = False

# Function to prepare input data
def prepare_input_data(input_data, preprocessor, label_encoder):
    # Define the column names expected by the model
    columns = ['Type', 'Air temperature [K]', 'Process temperature [K]',
               'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
    
    # Create a DataFrame with the input data
    input_df = pd.DataFrame([input_data], columns=columns)
    
    # Encode the 'Type' column using the label encoder
    input_df['Type'] = label_encoder.transform(input_df['Type'])
    
    # Transform the input data using the preprocessor
    return preprocessor.transform(input_df)

# Path to serve the index.html file from the "templates" folder
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_data')
def update_data():
    ip = request.args.get('ip', '192.168.68.54')
    port = int(request.args.get('port', 502))

    # Connect to the Modbus client
    client = ModbusTcpClient(ip, port=port)
    if not client.connect():
        return jsonify({"error": "Failed to connect to Modbus server"}), 500

    try:
        # Read potentiometer values from Modbus input registers
        response = client.read_input_registers(address=0, count=5, slave=1)
        if response and not response.isError():
            air_temp = response.registers[0] / 10.0
            process_temp = response.registers[1] / 10.0
            rotational_speed = response.registers[2] / 10.0
            torque = response.registers[3] / 10.0
            tool_wear = response.registers[4] / 10.0
        else:
            return jsonify({"error": "Error reading potentiometer values"}), 500

        # Check emergency stop status (Input 3)
        input_status = client.read_discrete_inputs(address=3, count=1, slave=1)  # Read Input 3
        emergency_status = 'ACTIVE' if input_status and not input_status.isError() and not input_status.bits[0] else 'INACTIVE'

        # Check system status (Coil 0)
        output = client.read_coils(address=0, count=1, slave=1)  # Read Coil 0
        system_status = 'ON' if output and not output.isError() and output.bits[0] else 'OFF'

        # Prepare data for prediction
        input_example = ['M', air_temp, process_temp, rotational_speed, torque, tool_wear]
        processed_input = prepare_input_data(input_example, preprocessor, label_encoder)

        # Predict using the loaded model
        output = loaded_model.predict(processed_input)
        prediction = 'Failure' if output[0] == 1 else 'No Failure'

        # Generate a message based on the prediction and tool wear
        message = generate_message(prediction, tool_wear)

        # Close the Modbus connection and return data
        return jsonify({
            'air_temperature': air_temp,
            'process_temperature': process_temp,
            'rotational_speed': rotational_speed,
            'torque': torque,
            'tool_wear': tool_wear,
            'prediction': prediction,
            'message': message,
            'emergency_stop_status': emergency_status,
            'system_status': system_status
        })

    finally:
        client.close()

@app.route('/emergency_stop')
def emergency_stop():
    global emergency_stop_active
    emergency_stop_active = not emergency_stop_active

    # Return the current state of the emergency stop
    return jsonify({'success': True if emergency_stop_active else False})

# Function to generate message based on prediction and tool wear
def generate_message(prediction, tool_wear):
    if prediction == 'Failure':
        message = "Motor with possible failure detected. Activate emergency stop!"
        if tool_wear > 10000:  # Threshold for high wear
            message += " This indicates that the failure is likely due to prolonged usage."
        else:
            message += " This suggests the failure might be caused by another factor (e.g., mechanical stress)."
    else:
        if tool_wear > 10000:
            message = "Although no failure is predicted, the tool wear is extremely high. A maintenance check should be scheduled immediately."
        elif tool_wear > 5000:
            message = "Although no failure is predicted, the tool wear is significant. Consider scheduling a maintenance check soon."
        else:
            message = "The tool wear is within acceptable limits. No immediate maintenance is needed."
    return message

if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 at port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)

