from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# Script python s'occupant de générer les Clée privé et public dans les fichiers.


cle = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
mdpCle = b'bonjour'

clePriv = cle.private_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PrivateFormat.PKCS8,
    encryption_algorithm = serialization.BestAvailableEncryption(mdpCle)
)

print(clePriv.splitlines())

privFile = open("clePrive.pem", "w")
privFile.write(str(clePriv.decode()))
privFile.close()

clePub = cle.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format= serialization.PublicFormat.SubjectPublicKeyInfo
)

print(clePub)

pubFile = open("clePublic.pem", "w")
pubFile.write(str(clePub.decode()))
pubFile.close()