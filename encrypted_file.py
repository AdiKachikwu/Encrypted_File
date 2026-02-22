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

    ##Uppercasing the key and message 
    for i in range(len(initial_key_split)):
        key_split.append(initial_key_split[i].upper())
    
    for i in range(len(initial_message_split)):
        message_split.append(initial_message_split[i].upper())


    #Function for Vigenere Cypher
    for i in range(len(message_split)):
        #Calculation of Vigenere Cypher
        encrypted_key = ((ord(key_split[i % len(key_split)]) - (ord("A") - 1)) + (ord(message_split[i]) - (ord("A") - 1))) % 26
        chr_encrypted_key = chr((encrypted_key) + ord("A"))
        Encrypted_message.append(chr_encrypted_key)
    
    #Just so that the outputed message comes in a string instead of a list
    for i in range(len(Encrypted_message)):
        msg_initial = str(Encrypted_message[i])
        new_msg = msg +""+ msg_initial
        msg = new_msg 
        
        
    print(msg)

def Decryption():
    decrypted_msg = ""
    Decrypted_message = []

    decrpt_key_split = []
    decrypt_message_split = []

    input_key = input("Enter your key: ")
    decrypt_message = input("Input your encrypted message: ")

    initial_decryptkey_split = list(input_key)
    initial_decryptmessage_split = list(decrypt_message)

    ##Uppercasing the key and message 
    for i in range(len(initial_decryptkey_split)):
        decrpt_key_split.append(initial_decryptkey_split[i].upper())
    
    for i in range(len(initial_decryptmessage_split)):
        decrypt_message_split.append(initial_decryptmessage_split[i].upper())
    
    #Function of using Viginere Cypher to Decrypt the key and message
    for i in range(len(decrypt_message_split)):
        decrypted_key = ((ord(decrypt_message_split[i]) - (ord("A") - 1)) - (ord(decrpt_key_split[i % len(decrpt_key_split)]) - ord("A") - 1)) % 26
        chr_decrypted_key = chr((decrypted_key) + ord("A"))
        Decrypted_message.append(chr_decrypted_key)

    #Just so that the outputed message comes in a string instead of a list
    for i in range(len(Decrypted_message)):
        msg_initial = str(Decrypted_message[i])
        new_msg = decrypted_msg +""+ msg_initial
        decrypted_msg = new_msg 
    
    print(decrypted_msg)
    print(Decrypted_message)


    
    

Encrypt(key, message)
Decryption()    
    






