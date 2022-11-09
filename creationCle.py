from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# Script python s'occupant de générer les Clée privé et public dans les fichiers.

# Try/except permettant de voir si tout ce passe correctement
try:
    #Génération de la paire de clé
    cle = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    # Initialisation du mot de passe de la clé privé
    mdpCle = b'bonjour'

    # Création de la clé privé
    clePriv = cle.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.PKCS8,
        encryption_algorithm = serialization.BestAvailableEncryption(mdpCle)
    )

    # Stockage de la clé privé dans un fichier
    privFile = open("clePrive.pem", "w")
    privFile.write(str(clePriv.decode()))
    privFile.close()

    # Création de la clé publique
    clePub = cle.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format= serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Stockage de la clé publique dans un fichier
    pubFile = open("clePublic.pem", "w")
    pubFile.write(str(clePub.decode()))
    pubFile.close()

    print("la création des clées c'est produite normalement")

# Permet d'afficher un message d'erreur si jamais un problème survient
except:
    print("Une erreur c'est produite")