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
    

    
    

Encrypt(key, message)    
    






