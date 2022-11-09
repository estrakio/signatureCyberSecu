from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization


with open("clePrive.pem", "rb") as fichierClePriv:
    clePrive = serialization.load_pem_private_key(
        fichierClePriv.read(),
        password=b'bonjour',
    )

f = open("message.txt", "rb")
message = f.read()

print(message)

signature = clePrive.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

signatureMessage = open("signatureMessage.txt", "wb")
signatureMessage.write(signature)
signatureMessage.close()

