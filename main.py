from morse import morse

if __name__ == "__main__":
    e = morse.encode('us')
    print('encoded: %s' %e)
    d = morse.decode(e)
    print('decoded: %s' %d)
    assert morse.encode('us') == '..- ...', print("Should be ..- ...")
    assert morse.decode('..- ...') == 'US', print("Should be US")
    print("Everything passed.")
