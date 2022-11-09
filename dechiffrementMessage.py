from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

with open("clePublic.pem", "rb") as fichierClePub:
    clePublic = serialization.load_pem_public_key(
        fichierClePub.read(),
    )

f = open("signatureMessage.txt", "rb")
signature = f.read()

f = open("message.txt", "rb")
message = f.read()


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
except:
    print("La signature ne correspond pas au message !")




