import string
#Define the alphabet
alphabet = list(string.ascii_letters)
#input plaintext and key
plain_text = input("Enter plain Text : ")
key = input("key : ")
#initialize variable
cipher_text = [ ]
i = 0
#Encrypt the plain text
for char in plain_text:
    if char in alphabet:
        index = alphabet.index(char)
        key_index = alphabet.index(key[i%len(key)])
        ans = (index+key_index)%26
        cipher_text.append(alphabet[ans])
        i+=1
    else:
        cipher_text.append(char)
        
#Output
print("The Cipher text is : ", "".join(cipher_text))
