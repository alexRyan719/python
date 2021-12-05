# Level 6 Kata - Code Wars
# Caesar Ciphers are one of the most basic forms of encryption. It consists of a message and a key, and it shifts the letters of the message for the value of the key.
# Read more about it here: https://en.wikipedia.org/wiki/Caesar_cipher

# Your task
# Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

# Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, numbers, spaces, and so on should remain the same.

# Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!
 
# Examples
# A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

# A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.


def encryptor(key, message):
    letter_dict = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",
                   17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
    number_dict = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,
                   "r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
   
    cipher_text = ""
    new_char = ""
    new_value = 0
    is_cap = False
   
    if key > 26:
        key = key % 26
       
    if key < -26:
        key *= -1
        key = key % 26
        key *= -1

    for char in message:
        if char.isalpha():
            if char.isupper():
                is_cap = True
                char = char.lower()
            else:
                is_cap = False
            new_value = number_dict[char] + key
            if new_value > 25:
                new_value -= 26
            if new_value < 0:
                new_value += 26
            new_char = letter_dict[new_value]
            if is_cap == True:
                new_char = new_char.upper()
            cipher_text += new_char
        else:
            cipher_text += char
    return cipher_text
