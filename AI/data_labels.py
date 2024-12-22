import os
import shutil

# Chemins vers les images et les annotations
images_dir = "/kaggle/input/tacotrashdataset/data/"  # Répertoire contenant les images
annotations_dir = "/kaggle/working/sortie2/"  # Répertoire contenant les annotations YOLO

# Répertoire de sortie pour le dataset fusionné
output_dir = "/kaggle/working/merged_dataset/"

# Créer le répertoire principal de sortie si nécessaire
os.makedirs(output_dir, exist_ok=True)

# Fonction pour fusionner les images et les annotations
def merge_data(images_dir, annotations_dir, output_dir):
    # Parcourir les dossiers des batches dans images_dir
    for batch_folder in os.listdir(images_dir):
        batch_path = os.path.join(images_dir, batch_folder)

        # Vérifier si c'est bien un dossier de batch
        if os.path.isdir(batch_path):
            print(f"Traitement du dossier batch : {batch_folder}")

            # Créer un sous-dossier pour les images et les annotations de ce batch
            batch_images_dir = os.path.join(output_dir, batch_folder, 'images')
            batch_labels_dir = os.path.join(output_dir, batch_folder, 'labels')
            
            os.makedirs(batch_images_dir, exist_ok=True)
            os.makedirs(batch_labels_dir, exist_ok=True)

            # Parcourir les fichiers d'images dans ce dossier
            for img_file in os.listdir(batch_path):
                # Vérifier si le fichier est une image (formats jpg, jpeg, png, etc.)
                if img_file.lower().endswith((".jpg", ".jpeg", ".png")):
                    img_path = os.path.join(batch_path, img_file)

                    # Copier l'image dans le dossier des images
                    shutil.copy(img_path, os.path.join(batch_images_dir, img_file))
                    print(f"Image copiée : {img_file}")
                    
                    # Générer le nom du fichier d'annotation correspondant
                    txt_file = os.path.splitext(img_file)[0] + ".txt"
                    txt_path = os.path.join(annotations_dir, batch_folder, txt_file)

                    # Vérifier si le fichier d'annotation existe
                    if os.path.exists(txt_path):
                        # Copier l'annotation dans le dossier des labels
                        shutil.copy(txt_path, os.path.join(batch_labels_dir, txt_file))
                        print(f"Annotation copiée pour : {img_file}")
                    else:
                        print(f"Avertissement : Pas d'annotation trouvée pour {img_file}")


merge_data(images_dir, annotations_dir, output_dir)

print("Fusion terminée.")
print(f"Les images sont dans : {output_dir}")