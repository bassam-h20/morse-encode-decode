class morse:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def encode(self, word):
        return 0
    def decode(self, morse_code):
        return 0


root = morse('start')


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
root.left.left.right.right = morse('blank')

#Left side (E) - Third level - (Under R)
root.left.right.left.left = morse('L')
root.left.right.left.right = morse('blank')

#Left side (E) - Third level - (Under W)
root.left.right.right.left = morse('P')
root.left.right.right.right = morse('J')

#Left side (E) - Fourth level - (under H)
root.left.left.left.left.left = morse('5')
root.left.left.left.left.right = morse('4')

#Left side (E) - Fourth level - (under V)
root.left.left.left.right.right = morse('3')
root.left.left.left.right.left = morse('blank')

#Left side (E) - Fourth level - (under F)
root.left.left.right.left.left = morse('blank')
root.left.left.right.left.right = morse('blank')

#Left side (E) - Fourth level - (under blank)
root.left.left.right.right.left = morse('blank')
root.left.left.right.right.right = morse('2')

#Left side (E) - Fourth level - (Under L)
root.left.right.left.left.left = morse('blank')
root.left.right.left.left.right = morse('blank')

#Left side (E) - Fourth level - (Under blank)
root.left.right.left.right.left = morse('+')
root.left.right.left.right.right = morse('blank')

#Left side (E) - Fourth level - (Under P)
root.left.right.right.left.left = morse('blank')
root.left.right.right.left.right = morse('blank')

#Left side (E) - Fourth level - (Under J)
root.left.right.right.right.left = morse('blank')
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
root.right.right.right.left = morse('blank')
root.right.right.right.right = morse('blank')

#Right side (T) - Fourth level - (under B)
root.right.left.left.left.left = morse('6')
root.right.left.left.left.right = morse('=')

#Right side (T) - Fourth level - (under X)
root.right.left.left.right.left = morse('/')
root.right.left.left.right.right = morse('blank')

#Right side (T) - Fourth level - (under C)
root.right.left.right.left.left = morse('blank')
root.right.left.right.left.right = morse('blank')

#Right side (T) - Fourth level - (under Y)
root.right.left.right.right.left = morse('blank')
root.right.left.right.right.right = morse('blank')

#Right side (T) - Fourth level - (under Z)
root.right.right.left.left.left = morse('7')
root.right.right.left.left.right = morse('blank')

#Right side (T) - Fourth level - (under Q)
root.right.right.left.right.left = morse('blank')
root.right.right.left.right.right = morse('blank')

#Right side (T) - Fourth level - (under left blank under O)
root.right.right.right.left.left = morse('8')
root.right.right.right.left.right = morse('blank')

#Right side (T) - Fourth level - (under right blank under O)
root.right.right.right.right.left = morse('9')
root.right.right.right.right.right = morse('0')


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
"0" : "-----"
}