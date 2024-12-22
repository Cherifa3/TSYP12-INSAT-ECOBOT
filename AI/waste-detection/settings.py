from pathlib import Path
import sys

file_path = Path(__file__).resolve()
root_path = file_path.parent
if root_path not in sys.path:
    sys.path.append(str(root_path))
ROOT = root_path.relative_to(Path.cwd())

# ML Model config

MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'
# Webcam
WEBCAM_PATH = 0


RECYCLABLE = [
    "Aluminium foil",
    "Aluminium blister pack",
    "Clear plastic bottle",
    "Glass bottle",
    "Metal bottle cap",
    "Food Can",
    "Aerosol",
    "Drink can",
    "Toilet tube",
    "Egg carton",
    "Drink carton",
    "Corrugated carton",
    "Pizza box", 
    "Paper cup",  
    "Glass jar",
    "Magazine paper",
    "Normal paper",
    "Paper bag",
    "Scrap metal",
    "Pop tab"
]

NON_RECYCLABLE = [
    "Battery",
    "Carded blister pack",
    "Other plastic bottle",
    "Plastic bottle cap",
    "Broken glass",
    "Other carton",
    "Meal carton", 
    "Disposable plastic cup",
    "Foam cup",
    "Glass cup",
    "Other plastic cup",
    "Food waste",
    "Plastic lid",
    "Metal lid",
    "Other plastic",
    "Tissues",
    "Wrapping paper",  
    "Plastified paper bag",
    "Plastic film",
    "Six pack rings",
    "Garbage bag",
    "Other plastic wrapper",
    "Single-use carrier bag",
    "Polypropylene bag",
    "Crisp packet",
    "Spread tub",
    "Tupperware",
    "Disposable food container",
    "Foam food container",
    "Other plastic container",
    "Plastic gloves",
    "Plastic utensils",
    "Rope & strings",
    "Shoe",
    "Squeezable tube",
    "Plastic straw",
    "Paper straw",
    "Styrofoam piece",
    "Unlabeled litter",
    "Cigarette"
]
