from ultralytics import YOLO
import time
import streamlit as st
import cv2
import settings
import threading

# Fonction pour vider les placeholders après un délai
def sleep_and_clear_success():
    time.sleep(7)
    st.session_state['recyclable_placeholder'].empty()
    st.session_state['non_recyclable_placeholder'].empty()

# Charger le modèle YOLO
def load_model(model_path):
    model = YOLO(model_path)
    return model

# Classifier les types de déchets détectés
def classify_waste_type(detected_items):
    recyclable_items = set(detected_items) & set(settings.RECYCLABLE)
    non_recyclable_items = set(detected_items) & set(settings.NON_RECYCLABLE)
    return recyclable_items, non_recyclable_items

# Retirer les tirets des noms de classe pour un affichage clair
def remove_dash_from_class_name(class_name):
    return class_name.replace("_", " ")

# Affichage des cadres détectés avec une logique de "persistence"
def _display_detected_frames(model, st_frame, image):
    image = cv2.resize(image, (640, int(640 * (9 / 16))))
    
    if 'detected_items' not in st.session_state:
        st.session_state['detected_items'] = {}

    if 'recyclable_placeholder' not in st.session_state:
        st.session_state['recyclable_placeholder'] = st.sidebar.empty()
    if 'non_recyclable_placeholder' not in st.session_state:
        st.session_state['non_recyclable_placeholder'] = st.sidebar.empty()

    res = model.predict(image, conf=0.6)
    names = model.names
    current_detected_items = set()

    # Récupérer les objets détectés et leur ajouter un timestamp
    for result in res:
        for box in result.boxes:
            class_name = names[int(box.cls)]
            current_detected_items.add(class_name)
            st.session_state['detected_items'][class_name] = time.time()

    # Supprimer les objets non vus récemment (par exemple, après 5 secondes)
    st.session_state['detected_items'] = {
        key: value for key, value in st.session_state['detected_items'].items()
        if time.time() - value <= 5
    }

    # Mettre à jour les placeholders pour les objets recyclables et non recyclables
    recyclable_items, non_recyclable_items = classify_waste_type(st.session_state['detected_items'].keys())

    if recyclable_items:
        detected_items_str = "\n- ".join(remove_dash_from_class_name(item) for item in recyclable_items)
        st.session_state['recyclable_placeholder'].markdown(
            f"<div class='stRecyclable'>Recyclable items:\n\n- {detected_items_str}</div>",
            unsafe_allow_html=True
        )
    else:
        st.session_state['recyclable_placeholder'].markdown("")

    if non_recyclable_items:
        detected_items_str = "\n- ".join(remove_dash_from_class_name(item) for item in non_recyclable_items)
        st.session_state['non_recyclable_placeholder'].markdown(
            f"<div class='stNonRecyclable'>Non-Recyclable items:\n\n- {detected_items_str}</div>",
            unsafe_allow_html=True
        )
    else:
        st.session_state['non_recyclable_placeholder'].markdown("")

    # Afficher les résultats avec bounding boxes
    res_plotted = res[0].plot()
    st_frame.image(res_plotted, channels="BGR")

# Fonction principale pour jouer le flux webcam
def play_webcam(model):
    source_webcam = settings.WEBCAM_PATH
    if st.button('Detect Objects'):
        try:
            vid_cap = cv2.VideoCapture(source_webcam)
            st_frame = st.empty()
            while vid_cap.isOpened():
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(model, st_frame, image)
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))
