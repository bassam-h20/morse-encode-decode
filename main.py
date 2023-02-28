from morse import morse

def test_encode_us():
    assert morse.encode('us') == '..- ...', print("Should be ..- ...")

def test_decode():
    assert morse.decode('..- ...') == 'US', print("Should be 'us'")


if __name__ == "__main__":
    test_encode_us()
    print("passed first test")
    test_decode()
    print("Everything passed successfully")

    
    
    


    