import rsa
import hashlib

publicKey, privateKey = rsa.newkeys(1024)

message = input("Quel message souhaitez vous crypter ? ")

signature = rsa.sign(message.encode(), privateKey, "SHA-256")


verif = rsa.verify(message.encode(), signature, publicKey) == "SHA-256"

print(f"Le message : {message} équivaut sous forme de signature  à  : {signature} ")
print(f"\n le résultat de la vérification est: {verif} ")