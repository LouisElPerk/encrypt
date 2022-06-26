#Encrypt and Decrypt files

# import required module
from cryptography.fernet import Fernet

file_name = 'nba.csv'

def init():
    # key generation
    key = Fernet.generate_key()

    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

def encriptar():
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open('C:/Users/elmer/Desktop/encrypt/'+file_name, 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open('C:/Users/elmer/Desktop/encrypt/'+file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def desencriptar():
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open('C:/Users/elmer/Desktop/encrypt/'+file_name, 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open('C:/Users/elmer/Desktop/encrypt/'+file_name, 'wb') as dec_file:
        dec_file.write(decrypted)

if __name__ == "__main__":
    opcion = int(input("Programa para encriptar o desencriptar un archivo:\n\n1.  Encriptar\n2.  Desencriptar\n3.  Salir\n\nOpcion: "))
    if opcion == 1:
        init()
        encriptar()
    elif opcion == 2:
        desencriptar()
    elif opcion == 3:
        print("Gracias por usar el programa")
    else:
        print("Opcion no valida")
        exit()
