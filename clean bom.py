import os
import re

# Dossier cible à nettoyer (traite également les sous-dossiers s'il y en a)
TARGET_DIR = "game/images"

def sanitize_filename(filename):
    # 1. Supprime le BOM Unicode et les espaces invisibles / à largeur nulle
    cleaned = filename.replace("\ufeff", "").replace("\u200b", "").replace("\u200c", "").replace("\u200d", "").replace("\xa0", " ")
    # 2. Retire les espaces parasites au début et à la fin
    cleaned = cleaned.strip()
    return cleaned

def clean_directory(directory):
    if not os.path.exists(directory):
        print(f"Erreur : Le dossier '{directory}' n'existe pas.")
        return

    renamed_count = 0
    total_files = 0

    for root, _, files in os.walk(directory):
        for name in files:
            total_files += 1
            clean_name = sanitize_filename(name)

            if clean_name != name:
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, clean_name)

                # Évite d'écraser un fichier existant par accident
                if os.path.exists(new_path):
                    print(f"[ATTENTION] Conflit : '{clean_name}' existe déjà. Fichier ignoré.")
                    continue

                os.rename(old_path, new_path)
                print(f"[CORRIGÉ] Caractère invisible retiré : '{clean_name}'")
                renamed_count += 1

    print("\n" + "=" * 40)
    print("BILAN DU NETTOYAGE")
    print("=" * 40)
    print(f"Fichiers scannés : {total_files}")
    print(f"Fichiers renommés : {renamed_count}")
    print("=" * 40)

if __name__ == "__main__":
    clean_directory(TARGET_DIR)