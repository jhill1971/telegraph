# telegraph
# James Hill 2021

# Dictionary
def telegram(plaintext):
    morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
             'D': '-..', 'E': '.', 'F': '..-.',
             'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..',
             'M': '--', 'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.',
             'S': '...', 'T': '-', 'U': '..-',
             'V': '...-', 'W': '.--', 'X': '-..-',
             'Y': '-.--', 'Z': '--..', ' ': '.....',
             '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
             '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..'}

    return ' '.join(morse[i] for i in plaintext.upper())


print("Enter your message. Restrict punctuation to , . or ?")
message = input("message: ")
print(telegram(message))
