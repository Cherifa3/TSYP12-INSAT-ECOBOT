# TSYP12-INSAT-ECOBOT

## Overview
The TSYP12-INSAT-ECOBOT is an intelligent waste detection robot powered by sustainable hydrogen energy. Combining cutting-edge AI and renewable energy, it provides a practical solution for waste management while promoting environmental sustainability.

---

## Features

**AI-Powered Waste Detection**
**Sustainable Energy System**
**Smart Navigation and Detection**
**Waste Collection Mechanism**
**Environmental Impact**
---

# Intelligent waste detection system
This part demonstrates waste detection using a YOLOv8 (You Only Look Once) object detection model. It identifies recyclable and non-recyclable  items in a webcam stream (the interface just to demonstrate our model).

the original dataset:
taco-trash-dataset

# to use the interface 
## Setup

*Clone the Repository:*
git clone https://github.com/Cherifa3/TSYP12-INSAT-ECOBOT.git
cd .\AI\waste-detection 
*Install Dependencies:*
pip install -r requirements.txt
*Run the Application*
streamlit run app.py
Open your web browser and navigate to the provided URL (usually http://localhost:8501). You will see the Waste Detection app.

## Project Structure

- app.py: Main application file containing Streamlit code.
- helper.py: Helper functions for waste detection using the YOLO model.
- settings.py: Configuration settings, including the path to the YOLO model and waste types.

## Classifying Waste Items


- **RECYCLABLE** = ["Aluminium foil", "Aluminium blister pack", "Clear plastic bottle", "Glass bottle", "Metal bottle cap", "Food Can", "Aerosol", "Drink can", "Toilet tube", "Egg carton", "Drink carton", "Corrugated carton", "Pizza box", "Paper cup", "Glass jar", "Magazine paper", "Normal paper", "Paper bag", "Scrap metal", "Pop tab"]

-**NON_RECYCLABLE** = ["Battery", "Carded blister pack", "Other plastic bottle", "Plastic bottle cap", "Broken glass", "Other carton", "Meal carton", "Disposable plastic cup", "Foam cup", "Glass cup", "Other plastic cup", "Food waste", "Plastic lid", "Metal lid", "Other plastic", "Tissues", "Wrapping paper", "Plastified paper bag", "Plastic film", "Six pack rings", "Garbage bag", "Other plastic wrapper", "Single-use carrier bag", "Polypropylene bag", "Crisp packet", "Spread tub", "Tupperware", "Disposable food container", "Foam food container", "Other plastic container", "Plastic gloves", "Plastic utensils", "Rope & strings", "Shoe", "Squeezable tube", "Plastic straw", "Paper straw", "Styrofoam piece", "Unlabeled litter", "Cigarette"]

## Screenshots
![alt text](<Capture d'écran 2024-12-22 221832.png>)
![alt text](<Capture d'écran 2024-12-22 221802-1.png>)

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [YOLO Documentation](https://github.com/ultralytics/yolov5)

  #### Hydrogen Fuel Cell System

The hydrogen fuel cell system is designed to efficiently generate electricity through an electrochemical reaction between hydrogen and oxygen. It features a regulation system to maintain optimal power generation and distribution to all components.

**Key Features**

1- H2 Regulation System

2- Fuel Cell Stack:

Converts hydrogen and oxygen into electricity via an electrochemical process.

Integrated with a heat exchanger and pump to manage temperature.

3- Energy Management System (EMS):

Combines the fuel cell stack with a battery to optimize power distribution.

Uses a DC-DC converter and H-bridge for voltage regulation.

4-Battery Integration:

Stores surplus energy to handle peak loads.

Works in tandem with the fuel cell stack for reliable power output.

5- Cooling System:

Heat exchanger and pump maintain the system's thermal stability.

**The global representation of the system**
![470887365_1249050322823418_1920506554673619779_n (1)](https://github.com/user-attachments/assets/e2008edc-dbb2-4a55-9a9e-137792c60e49)


**MATLAB Simulations:**

![466067293_585842687496879_6021450026104014461_n](https://github.com/user-attachments/assets/c243afdf-907f-4ddf-aa0b-ebc3e0aedfd3)
![467334823_1316917022797834_8580974688384073418_n (1)](https://github.com/user-attachments/assets/40cc5edc-fafb-4165-a12e-d971be393c15)

