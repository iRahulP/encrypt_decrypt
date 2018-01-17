#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:01:32 2018

@author: iRahulP
"""

ch = int(raw_input("1.Encrypt,2.Decrypt:"))
if ch == 1:
    s = raw_input("Enter Your Name for Encryption in Lower Case: ")
    Enc= list(s)
    Encrypted =[]
    Decrypted =[]   
    AlphaNum={"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
    Numerics= list(sorted(AlphaNum.values()))
    Alphabets= list(sorted(AlphaNum.keys()))

    def encrypt(k):
        p=((k+3)%26)
        return Alphabets[p]
    


    for i in xrange(0,len(s)):
        if Enc[i] in Alphabets:
            k= AlphaNum[Enc[i]]
            Encrypted.append(encrypt(k))
        else:
            print("Please enter input according to given Directions!")
        
        
    resultinc="".join(Encrypted)
    print "Encrypted Text :",resultinc


elif ch == 2:
    d= raw_input("Enter the Encrypted data to decrypt,Strictly in Lower Case:")
    dec= list(d)

    def decrypt(k):
        p=((k-3)%26)
        return Alphabets[p]


    for i in xrange(0,len(d)):
        if dec[i] in Alphabets:
            k= AlphaNum[dec[i]]
            Decrypted.append(decrypt(k))
        else:
            print("Please enter input according to given Directions!")
        
    resultdec="".join(Decrypted)
    print "Encrypted Text :",resultdec

else:
    print("Wrong Input Error!")