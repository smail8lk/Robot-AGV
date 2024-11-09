import socket

def run_modbus_client():
    HOST = '127.0.0.1'  # Adresse IP du serveur
    PORT = 65432  # Port utilisé par le serveur

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Connecté au serveur.")

        while True:
            # Demander à l'utilisateur de saisir une commande Modbus
            command = input("Entrez une commande (read_register, write_register <adresse>): ")
            
            # Vérifier si la commande est valide
            if validate_command(command):
                # Envoyer la commande au serveur
                client_socket.sendall(command.encode())
                
                # Recevoir la réponse du serveur
                response = client_socket.recv(1024).decode()
                print("Réponse du serveur:", response)
            else:
                print("Commande invalide. Veuillez réessayer.")

def validate_command(command):
    # Vérifie si la commande est dans le bon format
    # Pour simplifier, nous supposons qu'une commande valide doit commencer par "read_register" ou "write_register"
    valid_commands = ["read_register", "write_register"]
    parts = command.split(" ")
    if len(parts) >= 2 and parts[0] in valid_commands:
        # Si c'est une commande d'écriture, vérifiez qu'une adresse est fournie
        if parts[0] == "write_register" and len(parts) == 2:
            # Vérifier si l'adresse est un entier
            try:
                address = int(parts[1])
                return True
            except ValueError:
                return False
        # Si c'est une commande de lecture, pas besoin d'adresse
        elif parts[0] == "read_register":
            return True
    return False


def encode_mission(loading_station, unloading_station):
    # Encoder la mission selon les instructions fournies
    w20 = 2  # Nombre d'opérations
    w21 = (loading_station << 8) + unloading_station
    w22 = 0  # Autres opérations, ici pas besoin
    w23 = 0  # Autres opérations, ici pas besoin
    return w20, w21, w22, w23

def calculate_crc(data):
    # Calculer le CRC pour les données fournies
    # Par souci de simplicité, supposons un CRC simple basé sur la somme des octets
    crc = sum(data) & 0xFFFF  # Limiter le CRC à 16 bits
    return crc

def main():
    run_modbus_client()

if __name__ == "__main__":
    main()
