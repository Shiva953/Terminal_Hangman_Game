#HANGMAN_GAME

import random
import requests
import json

class Hangman:
    def greet(self):
        print("Welcome To The Hangman Game!")

    def acceptAndCheck(self):
        response = requests.get('https://random-word-api.herokuapp.com/all')
        list = json.loads(response.text)
        word = list[random.randint(0,len(list)-1)]
        word.upper()
        l = len(word)
        str,s='',''
        c,i=0,0
        w = word
        limit = l+(2*random.randint(1,l))
        print("The word is of",(l),"letters")
        print("You have got",(limit),"tries")
        while(i<l):
            str = str + "_"
            i+=1
            
        while(str!=word):
            a = input("Enter Your Guessed Letter : ")
            a.upper()
            c+=1
            if(c<=limit):
                if (a in word): 
                    x = w.index(a)
                    s = str[0:x] + w[x] + str[(x+1):l]
                    str = s
                    if(w.count(a)>1):
                        w = w[0:w.index(a)] + "_" + w[(w.index(a)+1):l]
                    else:
                        pass 
                print(str)
            else:
                print("Maximum number of tries exceeded. You lost!")
                print("The word was", word)
                break

        if(str==word):
            print("Congratulations,You Won!")

ob = Hangman()
ob.greet()
ob.acceptAndCheck()