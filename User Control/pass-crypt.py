#!/usr/bin/python
import crypt
def hashpass():
        salt = raw_input("Add some salt: ")
        password = raw_input("Password: ")
        password_verify = raw_input("Verify Password: ")
        if password == password_verify:
                print crypt.crypt(password, salt)
        else:
                print ("Passwords did not match!\n")
                hashpass()
hashpass()
