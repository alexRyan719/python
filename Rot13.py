# Level 5 Kata - Code Wars
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be 
# returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
# Please note that using encode is considered cheating.


def rot13(message):
    cipher_text = ""
    new_value = 0
    new_char = ""
    is_upper = False
    
    letter_dict = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
    number_dict = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    
    # You can also make lists instead of a second dictionary, but I preferred to access two dictionaries.
    
    for char in message:
        if char.isalpha():
            if char.isupper():
                is_upper = True
                char = char.lower()
            else:
                is_upper = False
            new_value = number_dict[char] + 13
            if new_value > 25:
                new_value -= 26
            new_char = letter_dict[new_value]
            if is_upper == True:
                new_char = new_char.upper()
            cipher_text += new_char
        else:
            cipher_text += char
    
    return cipher_text
