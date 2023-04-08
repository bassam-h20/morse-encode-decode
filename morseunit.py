import unittest
from morse import morse
from morse import *
class TestMorse(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(morse.encode('us'), '..- ...')
    
    def test_decode(self):
        self.assertEqual(morse.decode('..- ...'), 'US')        
    
    def test_encode_custom_1(self):
    #the correct result is -. but is changed for it to purposely fail
        self.assertEqual(morse.encode('n'), '..-')

    def test_encode_custom_2(self):
        self.assertEqual(morse.encode('my name is thomas'),'-- -.--   -. .- -- .   .. ...   - .... --- -- .- ...')
    
    def test_encode_custom_3(self):
    # the hashtag symbol (#) is invalid input, therefore fail
        self.assertEqual(morse.encode('#error'), '. .-. .-. --- .-.')

    def test_encode_custom_4(self):
        self.assertEqual(morse.encode('on your left'), '--- -.   -.-- --- ..- .-.   .-.. . ..-. -')

    def test_encode_custom_5(self):
        self.assertEqual(morse.encode('e i s h t m o 0'), '.   ..   ...   ....   -   --   ---   -----')
    
    #testing if decode function will detect "/" and detect a space
    def test_decode_custom_1(self):
        self.assertEqual(morse.decode('.... . .-.. .-.. --- / - .... . .-. .'),'HELLO THERE')

    #"/" not inserted so decode function should not detect a space
    def test_decode_custom_2(self):
        self.assertEqual(morse.decode('-.-. --- -- .--.  ... -.-. ..'),'COMPSCI')

    #Decoded message does not include spaces therefore is incorrect
    def test_decode_custom_3(self):
        self.assertEqual(morse.decode('- .... .. ...  .-- .- ... -.... ..-. ..- -.'),'THISWAS6FUN')

    #Invalid symbol (*) therefore is incorrect
    def test_decode_custom_4(self):
        self.assertEqual(morse.decode('* .... .- .... .-'),'*HAHA')

    def test_decode_custom_5(self):
        self.assertEqual(morse.decode('- .... .. ...   .. ...   .- -.   . -..- - .-. . -- . .-.. -.--   .-.. --- -. --.   -- . ... ... .- --. .   - ---   -.. . -.-. --- -.. .'),'THISISANEXTREMELYLONGMESSAGETODECODE')

    def test_binary_tree_is_empty1(self):
        self.assertEqual(root.left.left.right.right.data, "")
    
    def test_binary_tree_is_empty2(self): 
        self.assertEqual(root.left.right.left.right.data, " ")

    def test_binary_tree_is_not_empty1(self):
        self.assertEqual(root.right.left.left.right.data, "X")

    def test_binary_is_not_empty2(self):
        self.assertEqual(root.left.right.left.right.left.data, "+")


def additional_symbol_test():
    assert morse.decode("---...") == ":", print("Should be :")
    print("Test passed successfully")

def addtional_symbol_test2():
    assert morse.decode(".... . .-.. .-.. --- ...-..- .-- --- .-. .-.. -..") == "HELLO$WORLD", print("Should be HELLO$WORLD")
    print("Test passed successfully")

def additional_symbol_test3():
    assert morse.decode("- .... .. ... ..-.- / .. ... / -. .. -.-. .") == "THIS¿ IS NICE", print("Should be THIS¿ IS NICE")
    print("Test passed successfully")
        
def unit_tests_decode_bt1():
    assert morse.decode_bt("..-") == "U", print("Should be U")
    print("Test passed successfully")

def unit_tests_decode_bt2():
    assert morse.decode_bt("... --- ...") == "SOS", print("Should be SOs")
    print("Test passed successfully")
    
def unit_tests_decode_bt3():
    assert morse.decode_bt(".... . .-.. .-.. --- / - .... . .-. .") == "HELLO THERE", print("Should be HELLO THERE")
    print("Test passed succesfully")

def unit_tests_decode_bt4():
    assert morse.decode_bt("..--") ==  "%", print("Should be % (an empty node)")
    print("Test passed successfully")
    
def unit_tests_decode_bt5():
    assert morse.decode_bt("... -..-. --- -..-. ...") == "S/O/S", print("Should be S/O/S")
    print("Test passed successfully")

def unit_tests_decode_bt6():
    assert morse.decode_bt("... ..- -. -. -.-- -...- -.. .- -.--") == "SUNNY=DAY", print("Should be SUNNY=DAY")
    print("Test passed successfully")

def unit_test_encode_ham1():
    assert morse.encode_ham("s1","computer", "hello") == "-.-. --- -- .--. ..- - . .-. -.. . ... .---- -...- .... . .-.. .-.. --- -...- -.--.", print("Should be -.-. --- -- .--. ..- - . .-. -.. . ... .---- -...- .... . .-.. .-.. --- -...- -.--.")
    print("Test passed successfuly")

def unit_test_encode_ham2():
    assert morse.encode_ham("s-1","c0mpute$","h_llo") == "-.-. ----- -- .--. ..- - . ...-..- -.. . ... -....- .---- -...- .... ..--.- .-.. .-.. --- -...- -.--.", print("Should be -.-. ----- -- .--. ..- - . ...-..- -.. . ... -....- .---- -...- .... ..--.- .-.. .-.. --- -...- -.--.")
    print("Test passed successfully")

def unit_test_decode_ham1():
    assert morse.decode_ham("- .... . -..-. . -.-. .... --- -.. . -... .- ... ... .- -- -..-. .- .-.. .. -...- .--- ..- ... - -..-. .- -..-. -- . ... ... .- --. . -...- -.--.") == "Decoded:\nMessage from: bassam ali\nMessage to: the echo\nMessage content: just a message", print("Should be THE/ECHODEBASSAM/ALI=JUST/A/MESSAGE=(")
    print("Test passed successfully")

if __name__ == "__main__":
    additional_symbol_test()
    addtional_symbol_test2()
    additional_symbol_test3()
    unit_tests_decode_bt1()
    unit_tests_decode_bt2()
    unit_tests_decode_bt3()
    unit_tests_decode_bt4()
    unit_tests_decode_bt5()
    unit_tests_decode_bt6()
    unit_test_encode_ham1()
    unit_test_encode_ham2()
    unit_test_decode_ham1()
    unittest.main()
    