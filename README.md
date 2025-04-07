# AI-Driven-Predictive
This project predicts machine failures using the AI4I 2020 dataset. It integrates TPOT for model optimization, SMOTE for data balancing, and React+Flask for real-time data interaction, with visualizations provided by a Jupyter Notebook.
=======
# **Failure Prediction Project**

This project combines a Flask backend for real-time data interaction and a React frontend for user interface, aiming to predict motor failures using machine learning models. It also includes a Jupyter Notebook for model training and analysis.

---

## **How to Run**

1. **Install Dependencies:**
   - For the backend (Flask), navigate to the `my-project-backend` folder and run:
     ```bash
     pip install -r requirements.txt
     ```
   - For the frontend (React), navigate to the `my-project-react` folder and run:
     ```bash
     npm install
     ```

2. **Start the Project:**
   - From the root directory of the project, execute the `start_project.py` file:
     ```bash
     python start_project.py
     ```
   - This script will automatically start both the Flask backend and the React frontend.

3. **Using the Interface:**
   - Open the React application in your browser (default URL: `http://localhost:3000`).
   - Enter the IP address and port of your Modbus server.
   - View real-time data and predictions.

---

## **Features**

- **React Frontend:** Provides a user-friendly interface for monitoring and configuring Modbus server details.
- **Flask Backend:** Handles real-time data fetching and motor failure predictions.
- **Real-Time Monitoring:** Connects to devices via Modbus to fetch sensor data and predict motor failure.
- **Machine Learning:** Utilizes a trained model to classify motor conditions.
- **Customizable:** Allows users to retrain the model with new data as needed.

---

## **Notebook Details**

The Jupyter Notebook is responsible for:

1. **Model Training:**
   - It employs **TPOT (Tree-Based Pipeline Optimization Tool)** to automatically select the best machine learning model for the data.

2. **Data Balancing:**
   - Data is balanced using **SMOTE (Synthetic Minority Oversampling Technique)** to handle class imbalance effectively.

3. **Model Export:**
   - Once trained, the model is saved as `trained_model.pkl`, along with `preprocessor.pkl` and `label_encoder.pkl` in the `models` directory.

### **To Retrain the Model**
- Run the Jupyter Notebook (`my-project-backend/notebooks/model_training.ipynb`) with new data.
- Save the updated model, preprocessor, and encoder in the `my-project-backend/models` directory for future use with the main application.

---


## **Folder Structure**

Prototype/ ├── my-project-backend/        # Contains the Flask backend, models, and notebooks │   ├── app.py                 # Main Python file (Flask application) │   ├── models/                # Contains the trained model, preprocessor, and encoder files │   ├── notebooks/             # Jupyter Notebook for training and analysis │   ├── templates/             # HTML templates for the Flask app │   ├── requirements.txt       # Python dependencies ├── my-project-reactapp/          # React frontend │   ├── public/                # Static assets │   ├── src/                   # React components and logic │   ├── package.json           # Node.js dependencies ├── start_project.py           # Python script to start Flask and React ├── README.md                  # Project documentation



