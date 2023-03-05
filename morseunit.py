import unittest
from morse import morse

class TestMorse(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(morse.encode('us'), '..- ...')
    
    def test_decode(self):
        self.assertEqual(morse.decode('..- ...'), 'US')        
    
    def test_encode_custom_1(self):
        self.assertEqual(morse.encode('n'), '..-')
        print("passed successfully")


if __name__ == "__main__":
    unittest.main()
    