# TSYP12-INSAT-ECOBOT

# Intelligent waste detection system
This project demonstrates waste detection using a YOLOv8 (You Only Look Once) object detection model. It identifies recyclable, non-recyclable, and hazardous waste items in a webcam stream.

the original dataset:
https://universe.roboflow.com/ai-project-i3wje/waste-detection-vqkjo/model/3


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

![screenshot2](screenshot2.png)

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [YOLO Documentation](https://github.com/ultralytics/yolov5)