class morse_tree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def encode():
        print("Not complete")
    def decode():
            print("not complete")


root = morse_tree('start')


#Left side (E)
root.left = morse_tree('E')

#Left side (E) - First level - (Under E)
root.left.left = morse_tree('I')
root.left.right = morse_tree('A')

#Left side (E) - Second level - (Under I)
root.left.left.left = morse_tree('S')
root.left.left.right = morse_tree('U')

#Left side (E) - Second level - (under A)
root.left.right.left = morse_tree('R')
root.left.right.right = morse_tree('W')

#Left side (E) - Third level - (Under S)
root.left.left.left.left = morse_tree('H')
root.left.left.left.right = morse_tree('V')

#Left side (E) - Third level - (Under U)
root.left.left.right.left = morse_tree('F')
#root.left.left.right.right = morse_tree('blank')

#Left side (E) - Third level - (Under R)
root.left.right.left.left = morse_tree('L')
#root.left.right.left.right = morse_tree('blank')

#Left side (E) - Third level - (Under W)
root.left.right.right.left = morse_tree('P')
root.left.right.right.right = morse_tree('J')

#Left side (E) - Fourth level - (under H)
root.left.left.left.left.left = morse_tree('5')
root.left.left.left.left.right = morse_tree('4')

#Left side (E) - Fourth level - (under V)
root.left.left.left.right.right = morse_tree('3')
#root.left.left.left.right.left = morse_tree('blank')

#Left side (E) - Fourth level - (under F)
#root.left.left.right.left.left = morse_tree('blank')
#root.left.left.right.left.right = morse_tree('blank')

#Left side (E) - Fourth level - (under blank)
#root.left.left.right.right.left = morse_tree('blank')
root.left.left.right.right.right = morse_tree('2')

#Left side (E) - Fourth level - (Under L)
#root.left.right.left.left.left = morse_tree('blank')
#root.left.right.left.left.right = morse_tree('blank')

#Left side (E) - Fourth level - (Under blank)
root.left.right.left.right.left = morse_tree('+')
#root.left.right.left.right.right = morse_tree('blank')

#Left side (E) - Fourth level - (Under P)
#root.left.right.right.left.left = morse_tree('blank')
#root.left.right.right.left.right = morse_tree('blank')

#Left side (E) - Fourth level - (Under J)
root.left.right.right.right.left = morse_tree('blank')
root.left.right.right.right.right = morse_tree('1')

#Right side (T)
root.right = morse_tree('T')

#Right side (T) - First level - (under T)
root.right.left = morse_tree('N')
root.right.right = morse_tree('M')

#Right side (T) - Second level - (under N)
root.right.left.left = morse_tree('D')
root.right.left.right = morse_tree('K')

#Right side (T) - Second level - (under M)
root.right.right.left = morse_tree('G')
root.right.right.right = morse_tree('O')

#Right side (T) - Third level - (under D)
root.right.left.left.left = morse_tree('B')
root.right.left.left.right = morse_tree('X')

#Right side (T) - Third level - (under K)
root.right.left.right.left = morse_tree('C')
root.right.left.right.right = morse_tree('Y')

#Right side (T) - Third level - (under G)
root.right.right.left.left = morse_tree('Z')
root.right.right.left.right = morse_tree('Q')

#Right side (T) - Third level - (under O)
#root.right.right.right.left = morse_tree('blank')
#root.right.right.right.right = morse_tree('blank')

#Right side (T) - Fourth level - (under B)
root.right.left.left.left.left = morse_tree('6')
root.right.left.left.left.right = morse_tree('=')

#Right side (T) - Fourth level - (under X)
root.right.left.left.right.left = morse_tree('/')
#root.right.left.left.right.right = morse_tree('blank')

#Right side (T) - Fourth level - (under C)
#root.right.left.right.left.left = morse_tree('blank')
#root.right.left.right.left.right = morse_tree('blank')

#Right side (T) - Fourth level - (under Y)
#root.right.left.right.right.left = morse_tree('blank')
#root.right.left.right.right.right = morse_tree('blank')

#Right side (T) - Fourth level - (under Z)
root.right.right.left.left.left = morse_tree('7')
#root.right.right.left.left.right = morse_tree('blank')

#Right side (T) - Fourth level - (under Q)
#root.right.right.left.right.left = morse_tree('blank')
#root.right.right.left.right.right = morse_tree('blank')

#Right side (T) - Fourth level - (under left blank under O)
root.right.right.right.left.left = morse_tree('8')
#root.right.right.right.left.right = morse_tree('blank')

#Right side (T) - Fourth level - (under right blank under O)
root.right.right.right.right.left = morse_tree('9')
root.right.right.right.right.right = morse_tree('0')