# Level 5 Kata - Code Wars
# How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13)
# is frequently used to obfuscate jokes on USENET.

# Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

# rot13("EBG13 rknzcyr.") == "ROT13 example.";
# rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"

def rot13(message):
    letter_dict = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",
                   17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
    number_dict = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,
                   "r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
   
    cipher_text = ""
    new_char = ""
    new_value = 0
    is_cap = False
   
    for char in message:
        if char.isalpha():
            if char.isupper():
                is_cap = True
                char = char.lower()
            else:
                is_cap = False
            new_value = number_dict[char] + 13
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
