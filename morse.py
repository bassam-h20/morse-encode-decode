class morse:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #function that decodes morse code and outputs text, characters and symbols according to the binary tree implemented
    def decode(msg: str) -> str:
        # Split message into words space as delimiter
        words = msg.split(" ") 
        decoded_msg = ""
        for word in words:
             # Split each word into individual morse code letters using single space as delimiter
            letters = word.split()
            for letter in letters:
                node = root
                for symbol in letter:
                    # Traverse left if dot
                    if symbol == ".": 
                        node = node.left
                    # Traverse right if dash
                    elif symbol == "-": 
                        node = node.right
                    elif symbol == "/":
                        decoded_msg += " "
                    else:
                        return ("Invalid Input")
                        break
                if node.data is not None:
                    decoded_msg += node.data
        return decoded_msg
    
    #same functionality as decode() but uses a string representation of a binary heap instead
    #to decode morse code
    def decode_bt(msg: str) -> str:
        # % symbols are for empty/blank nodes
        tree = "-@ETIANMSURWDKGOHVF%L%PJBXCYZQ%%54%3%%%2%%+%%%%16=/%%%%%7%%%8%90"
        i = 1
        words = msg.split(" ")
        decoded_msg = ""
        for word in words:
            letters = word.split()
            for letter in letters:
                for symbol in letter:
                    if symbol == ".":
                        i = 2 * i # move to the left child
                    elif symbol == "-":
                        i = 2 * i + 1 # move to the right child
                    elif symbol == "/":
                        decoded_msg += " "
                    else:
                        return ("Invalid Input")
                        break
                if tree[i] == "@":
                    decoded_msg += ""
                else:
                    decoded_msg += tree[i]
                i = 1
        return decoded_msg

    #decodes morse code that encoded extended morse code from a ham radio conversation
    def decode_ham(msg: str) -> str:
        decoded_msg = morse.decode(msg)
        print("full-text: ",decoded_msg.lower())
        morse_receiver, second_part_message = decoded_msg.split("DE", 1)
        morse_sender, morse_content, _= second_part_message.split("=")
        final_msg_display = "Decoded:\nMessage from: "+morse_sender.lower()+"\nMessage to: "+morse_receiver.lower()+"\nMessage content: "+morse_content.replace("/", " ").lower()
        return final_msg_display


    
    
    #function takes letters, characters, symbols and outputs morse code according to the "morse_dict" dictionary
    def encode(msg: str) -> str:
        encoded_msg = ""
        for letter in msg.upper():
                #check if letter is not defined in dictionary
                if letter not in morse_dict:
                    return ("Invalid input")
                    break
                else:
                    encoded_msg += morse_dict.get(letter.upper(), '') + ' '
        return (encoded_msg.strip())
    
    #encodes extended morse code for a ham radio converstation    
    def encode_ham(sender: str, receiver: str, msg: str) -> str:
        morse_receiver = morse.encode(receiver)
        morse_sender = morse.encode(sender)
        morse_msg = morse.encode(msg)
        encoded_msg2 = f"{morse_receiver} -.. . {morse_sender} -...- {morse_msg} -...- -.--."
        return encoded_msg2
    

    

    #function that prints the binary tree implemented, includes all characters and symbols added to the binary tree
    def print_tree(node, level = 0):
        if node is not None:
            print(" " * level, end="")
            print(f"{node.data} -")
            if node.left is not None or node.right is not None:
                morse.print_tree(node.left, level+4)
                morse.print_tree(node.right, level+4)



root = morse('')
#Left side (E)
root.left = morse('E')

#Left side (E) - First level - (Under E)
root.left.left = morse('I')
root.left.right = morse('A')

#Left side (E) - Second level - (Under I)
root.left.left.left = morse('S')
root.left.left.right = morse('U')

#Left side (E) - Second level - (under A)
root.left.right.left = morse('R')
root.left.right.right = morse('W')

#Left side (E) - Third level - (Under S)
root.left.left.left.left = morse('H')
root.left.left.left.right = morse('V')

#Left side (E) - Third level - (Under U)
root.left.left.right.left = morse('F')
root.left.left.right.right = morse('')

#Left side (E) - Third level - (Under R)
root.left.right.left.left = morse('L')
root.left.right.left.right = morse(' ')

#Left side (E) - Third level - (Under W)
root.left.right.right.left = morse('P')
root.left.right.right.right = morse('J')

#Left side (E) - Fourth level - (under H)
root.left.left.left.left.left = morse('5')
root.left.left.left.left.right = morse('4')

#Left side (E) - Fourth level - (under V)
root.left.left.left.right.right = morse('3')
root.left.left.left.right.left = morse(' ')

#Left side (E) - Fourth level - (under F)
root.left.left.right.left.left = morse(' ')
root.left.left.right.left.right = morse(' ')

#Left side (E) - Fourth level - (under )
root.left.left.right.right.left = morse(' ')
root.left.left.right.right.right = morse('2')

#Left side (E) - Fourth level - (Under L)
root.left.right.left.left.left = morse(' ')
root.left.right.left.left.right = morse(' ')

#Left side (E) - Fourth level - (Under )
root.left.right.left.right.left = morse('+')
root.left.right.left.right.right = morse(' ')

#Left side (E) - Fourth level - (Under P)
root.left.right.right.left.left = morse(' ')
root.left.right.right.left.right = morse(' ')

#Left side (E) - Fourth level - (Under J)
root.left.right.right.right.left = morse(' ')
root.left.right.right.right.right = morse('1')

#Right side (T)
root.right = morse('T')

#Right side (T) - First level - (under T)
root.right.left = morse('N')
root.right.right = morse('M')

#Right side (T) - Second level - (under N)
root.right.left.left = morse('D')
root.right.left.right = morse('K')

#Right side (T) - Second level - (under M)
root.right.right.left = morse('G')
root.right.right.right = morse('O')

#Right side (T) - Third level - (under D)
root.right.left.left.left = morse('B')
root.right.left.left.right = morse('X')

#Right side (T) - Third level - (under K)
root.right.left.right.left = morse('C')
root.right.left.right.right = morse('Y')

#Right side (T) - Third level - (under G)
root.right.right.left.left = morse('Z')
root.right.right.left.right = morse('Q')

#Right side (T) - Third level - (under O)
root.right.right.right.left = morse(' ')
root.right.right.right.right = morse(' ')

#Right side (T) - Fourth level - (under B)
root.right.left.left.left.left = morse('6')
root.right.left.left.left.right = morse('=')

#Right side (T) - Fourth level - (under X)
root.right.left.left.right.left = morse('/')
root.right.left.left.right.right = morse(' ')

#Right side (T) - Fourth level - (under C)
root.right.left.right.left.left = morse(' ')
root.right.left.right.left.right = morse(' ')

#Right side (T) - Fourth level - (under Y)
root.right.left.right.right.left = morse(' ')
root.right.left.right.right.right = morse(' ')

#Right side (T) - Fourth level - (under Z)
root.right.right.left.left.left = morse('7')
root.right.right.left.left.right = morse(' ')

#Right side (T) - Fourth level - (under Q)
root.right.right.left.right.left = morse(' ')
root.right.right.left.right.right = morse(' ')

#Right side (T) - Fourth level - (under left  under O)
root.right.right.right.left.left = morse('8')
root.right.right.right.left.right = morse(' ')

#Right side (T) - Fourth level - (under right  under O)
root.right.right.right.right.left = morse('9')
root.right.right.right.right.right = morse('0')

#Additional Symbols
root.left.right.left.right.left.right = morse(".")
root.right.right.left.left.right.right = morse(",")
root.left.left.right.right.left = morse("?")
root.left.right.right.right.right.left = morse("'")
root.right.left.right.left.right.right = morse("!")
root.right.left.right.right.left = morse("(")
root.right.left.right.right.left.right = morse(")")
root.left.right.left.left.left = morse("&")
root.right.right.right.left.left.left = morse(":")
root.right.left.right.left.right.left = morse(";")
root.right.left.left.left.left.right = morse("-")
root.left.left.right.right.left.right = morse("_")
root.left.right.left.left.right.left = morse('"')
root.left.left.left.right.left.left = morse("")
root.left.left.left.right.left.right = morse("")
root.left.left.left.right.left.left.right = morse("$")
root.left.left.right.left.right = morse("¿")
root.right.right.left.left.left.right = morse("¡")


#python dicrtionart to decode morse code
morse_dict = {
#First level
"E" : ".",
"T" : "-",
#Second level
"I" : "..",
"A" : ".-",
"N" : "-.",
"M" : "--",
#Third level
"S" : "...",
"U" : "..-",
"R" : ".-.",
"W" : ".--",
"D" : "-..",
"K" : "-.-",
"G" : "--.",
"O" : "---",
#Fourth Level
"H" : "....",
"V" : "...-",
"F" : "..-.",
"" : "..--",
"L": ".-..",
"" : ".-.-",
"P" : ".--.",
"J" : ".---",
"B" : "-...",
"X" : "-..-",
"C" : "-.-.",
"Y" : "-.--",
"Z" : "--..",
"Q" : "--.-",
"" : "---.",
"" : "----",
#Fifth Level
"5" : ".....",
"4" : "....-",
"" : "...-.",
"3" : "...--",
"" : "..-..",
"" : "..-.-",
"" : "..--.",
"2" : "..---",
"" : ".-...",
"" : ".-..-",
"+" : ".-.-.",
"" : ".-.--",
"" : ".--..",
"" : ".--.-",
"" : ".---.",
"1" : ".----",
"6" : "-....",
"=" : "-...-",
"/" : "-..-.",
"" : "-..--",
"" : "-.-..",
"" : "-.-.-",
"" : "-.--.",
"" : "-.---",
"7" : "--...",
"" : "--..-",
"" : "--.-.",
"" : "--.--",
"8" : "---..",
"" : "---.-",
"9" : "----.",
"0" : "-----",
#TASK 4 - additional symbols (. , ? ' ! ( ) & : ; + - _ " $ ¿ ¡)
".": ".-.-.-",
",":"--..--",
"?":"..--.",
"'":".----.",
"!":"-.-.--",
"(":"-.--.",
")":"-.--.-",
"&":".-...",
":":"---...",
";":"-.-.-.",
"-":"-....-",
"_":"..--.-",
'"' : ".-..-.",
"$":"...-..-",
"¿":"..-.-",
"¡":"--...-",
#space
" ": " "
}

if __name__ == "__main__":
    print("Morse code binary tree:")
    morse.print_tree(root)
    print("\n\n")
    
    while True:
        #user prompts for user to choose which operation to use
        option = input("q\n- Encode(E) or Decode(D) or Decode with Binary Heap(DB)\n- Extended Encode(E2) or Extended Decode(D2): ").upper()
        if option == 'E':
            user_input = input("\nEnter the characters you wish to encode: ")
            user_encoded = morse.encode(user_input)
            print("Encoded Result:", user_encoded,"\n")
        
        elif option == 'D':
            user_input = input("\nEnter the morse code you wish to decode: ")
            user_decoded = morse.decode(user_input)
            print("Decoded Result:", user_decoded,"\n")
        
        elif option == 'DB':
            user_input = input("\nEnter Morse code you wish to decode: ")
            user_decoded = morse.decode_bt(user_input)
            print(user_decoded)

        elif option == 'E2':
            sender = input("\nEnter the sender's name: ")
            receiver = input("Enter the receiver's name: ")
            user_input = input("Enter the charactsers you wish to encode in extended morse code: ")
            user_ext_encoded = morse.encode_ham(sender, receiver, user_input)
            print("Encoded result:",user_ext_encoded)
        
        elif option == 'D2':
            user_input = input("\nEnter the extended morse code you wish to decode: ")
            user_ext_decoded = morse.decode_ham(user_input)
            print(user_ext_decoded)

        else:
            print("Error: Enter valid input")