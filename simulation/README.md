# **Simulation Documentation**

This folder contains files related to the simulation environment, developed using **OpenPLC** and **Factory I/O**. The simulation aims to replicate the operation of a conveyor system, utilizing ladder logic and potentiometers to simulate sensor values.

---

## **OpenPLC Program**

- The program included here is designed to be uploaded to the **OpenPLC Runtime**.
- It is a basic ladder logic program that controls the functionality of a conveyor system.
- The logic uses potentiometers to simulate sensor values, such as temperature and rotational speed, within the system.

---

## **Factory I/O Configuration**

1. **Simulation Environment**:
   - The Factory I/O environment replicates industrial processes with sensors and actuators integrated into the conveyor system.

2. **Modbus Server Setup**:
   - Configure the Modbus Server in Factory I/O.
   - Verify the **IP address** and **Port** used for communication.
   - Ensure the sensors and actuators are properly linked to their respective Modbus addresses.

3. **Variable Assignment**:
   - Compare the variables declared in the **OpenPLC Runtime** program with the ones set in Factory I/O.
   - Make sure the mappings are correct to enable smooth data exchange between the systems.

---

## **How to Use**

1. **Upload the OpenPLC Program**:
   - Open the OpenPLC Runtime and upload the ladder logic program provided in this folder.

2. **Configure Factory I/O**:
   - Set up the Modbus Server with the correct IP address and Port number.
   - Match the variables in Factory I/O to those declared in the OpenPLC Runtime.

3. **Run Simulation**:
   - Start the OpenPLC Runtime and Factory I/O.
   - Observe the conveyor system's operation and verify that sensor values update correctly based on the potentiometer inputs.

---

## **Files in This Folder**

- `openplc_program.st`: The ladder logic program for OpenPLC Runtime.
- `factory_io_environment.factory`: The simulation environment for Factory I/O.

---

Feel free to reach out if you need further clarification or setup instructions. 😊
