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

    def additional_symbol_test(self):
        self.assertEqual(morse.decode(":"), "---...")


if __name__ == "__main__":
    unittest.main()
    