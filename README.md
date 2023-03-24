### morse.py uses two main functions (1) encode and (2) decode which both convert characters and symbols to morse code and vice versa

* When the program is run it prints out the binary tree used to decode the morse code in the decode function.

![binary tree](./binary-tree.png)

* And then gives the user the option to (E) encode or (D) decode, and enter the characters accordingly 


### Task 2 was to implement the two functions mentioned and make sure they work properly, and that can be seen through the image below

###### as shown in the picture in order to create spaces the "/" character must be inserted when decoding
![user option](./terminal-output.png)


### Task 3 was to create a simple assert test (in main.py) for the two functions implemented and another file (morseunit.py) that used the unittest library

##### In morseunit.py, it was asked to create tests for the encode and decode function. Also added tests for verifying the empty and non-empty nodes of the implemented binary tree.

1. output of main.py
![assert test](./assert-test.png)

2. output of morseunit.py

These are the tests that were purposely made to fail
![unit tests](./unit-test.png)


### Task 4 was to add a set of morse encodings of frequently used symbols, and added tests for these symbols that are also included in the morseunit.py file


