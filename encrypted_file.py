#First Encryption and Decryption Using the Vigenere Cypher
key = input("Enter your Key:  ")
message = input("Enter your message:  ")


#Current constraints it returns the message in capitals 
#Used sites, W3SCHOOLS AND GEEKSFORGEEKS

def Encrypt(key, message):
    msg = ""
    Encrypted_message = []
    key_split = []
    message_split = []
    #Adding the key and message into the array 
    initial_key_split = list(key)
    initial_message_split = list(message)

