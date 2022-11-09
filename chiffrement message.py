from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

# Script python s'occupant de générer la signature du fichier "message.txt".

#Récupération De la clé privé depuis son fichier et la retransforme en objet
with open("clePrive.pem", "rb") as fichierClePriv:
    clePrive = serialization.load_pem_private_key(
        fichierClePriv.read(),
        password=b'bonjour',
    )
#Récupération du texte
f = open("message.txt", "rb")
message = f.read()

print(message)

# Création de la signiature du message
signature = clePrive.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

#Stockage de la signature dans un fichier
signatureMessage = open("signatureMessage.txt", "wb")
signatureMessage.write(signature)
signatureMessage.close()

