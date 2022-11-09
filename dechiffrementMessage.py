from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

# Script python s'occupant de vérifié la signature présente dans le fichier "signatureMessage.txt" du fichier "message.txt".

#Récupération De la clé publique depuis son fichier et la retransforme en objet
with open("clePublic.pem", "rb") as fichierClePub:
    clePublic = serialization.load_pem_public_key(
        fichierClePub.read(),
    )
# Récupération de la signature depuis son fichier
f = open("signatureMessage.txt", "rb")
signature = f.read()

# Récupération du message depuis son fichier
f = open("message.txt", "rb")
message = f.read()

#Mise en place d'un try/except pour afficher si la signature est bien celle du message.
try:
    clePublic.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("La vérification c'est bien déroulé la signature du message est valide")

# Message s'affichant uniquement lorsque la signiature du message ne correspond pas au message
except:
    print("La signature ne correspond pas au message !")




