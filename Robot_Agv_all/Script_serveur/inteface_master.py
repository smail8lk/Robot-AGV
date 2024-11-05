import minimalmodbus
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Dictionnaire associant chaque adresse à sa description
address_description = {
    271: "Présence charge sur chariot",
    272: "Ordre lancement mission",
    273: "Mission terminée sans erreur",
    274: "Mission terminée avec erreur",
    275: "Demande d'initialisation de chariot",
    276: "Défaut contacteur principal",
    277: "Défaut décharge batterie",
    278: "Mode automatique sélectionné",
    279: "Mode semi-automatique sélectionné",
    280: "Chariot en manuel",
    281: "Radar actif",
    282: "Pare choc enclenché",
    283: "Sortie de bande",
    284: "Défaut d'isocentrage",
    285: "Défaut charge débordante sur le chariot",
    286: "Défaut de prise",
    287: "Défaut de dépose"
}

def read_modbus_address(instrument, address):
    value = instrument.read_register(address, functioncode=3)
    return value

def check_state(address):
    # Remplacer 'COM1' par le nom de votre port série et 1 par l'adresse de l'appareil
    instrument = minimalmodbus.Instrument('COM1', 1)  
    # Configurer les paramètres de communication
    instrument.serial.baudrate = 9600
    instrument.serial.bytesize = 8
    instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.serial.timeout = 1  # Temps d'attente en secondes
    value = read_modbus_address(instrument, address)
    return "Activé" if value == 1 else "Arrêté"

def create_interface():
    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("TP de pilotage du robot AGV")
    root.geometry("800x600")  # Taille de l'interface augmentée
    """
    #* Ajouter les logos et le titre
    logo1_image = Image.open("C:\\Users\\Lenovo\\Desktop\\ROBOT_AGV\\um6p.png")
    logo1_image = logo1_image.resize((100, 100), Image.ANTIALIAS)
    logo1_photo = ImageTk.PhotoImage(logo1_image)
    logo1_label = ttk.Label(root, image=logo1_photo)
    logo1_label.grid(row=0, column=0, padx=10, pady=10)

    logo2_image = Image.open("C:\\Users\\Lenovo\\Desktop\\ROBOT_AGV\\gti_logo.png")
    logo2_image = logo2_image.resize((100, 100), Image.ANTIALIAS)
    logo2_photo = ImageTk.PhotoImage(logo2_image)
    logo2_label = ttk.Label(root, image=logo2_photo)
    logo2_label.grid(row=0, column=2, padx=10, pady=10)
     """
    title_label = ttk.Label(root, text="TP de pilotage du robot AGV", font=("Helvetica", 16))
    title_label.grid(row=0, column=1, padx=10, pady=10)#*
     
    # Créer un cadre pour les boutons à gauche
    frame_left = ttk.Frame(root)
    frame_left.grid(row=1, column=0, padx=10, pady=10)

    # Créer un cadre pour les boutons à droite
    frame_right = ttk.Frame(root)
    frame_right.grid(row=1, column=2, padx=10, pady=10)

    # Créer un bouton pour chaque état du chariot
    buttons_left = {}  # Dictionnaire pour stocker les boutons à gauche
    buttons_right = {}  # Dictionnaire pour stocker les boutons à droite
    for address, description in address_description.items():
        if address in [271, 275]:  # États à afficher à droite
            frame = frame_right
            var = tk.IntVar()
            button = ttk.Checkbutton(frame, text=description, variable=var)
            button_text = "Activer"  # Texte pour le bouton d'activation
            button_command = lambda a=address, v=var: write_state_message(a, v.get())  # Commande pour activer
        else:
            frame = frame_left
            button_text = "Lire"  # Texte pour le bouton de lecture
            button_command = lambda a=address: read_state_message(a)  # Commande pour lire
            button = ttk.Button(frame, text=description, command=button_command)

        button.grid(row=address, column=0, sticky="w", pady=5)
        buttons_left[address] = button if frame == frame_left else buttons_right  # Stocker le bouton dans le dictionnaire approprié

        # Associer une fonction à chaque bouton
        button.config(command=button_command)

    # Ajouter un Combobox pour les modes à droite
    mode_combobox = ttk.Combobox(frame_right, values=["Mode automatique", "Mode semi-automatique", "Chariot en manuel"])
    mode_combobox.grid(row=0, column=0, padx=10, pady=10)
    mode_combobox.current(0)  # Sélectionner le premier élément par défaut

    # Label pour afficher l'état
    state_label = ttk.Label(frame_left, text="")
    state_label.grid(row=len(address_description) + 1, column=0, sticky="w", pady=5)

    # Fonction pour lire et afficher l'état
    def read_state_message(address):
        state = check_state(address)
        state_label.config(text=f"{address_description[address]} : {state}")

    # Fonction pour écrire l'état
    def write_state_message(address, value):
        # Vous pouvez ajouter ici le code pour écrire l'état
        state = "Activé" if value == 1 else "Arrêté"
        state_label.config(text=f"{address_description[address]} : {state}")

    # Lancer la boucle principale
    root.mainloop()

if __name__ == "__main__":
    create_interface()
