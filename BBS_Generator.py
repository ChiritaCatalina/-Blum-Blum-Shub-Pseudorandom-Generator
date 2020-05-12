# import tkinter module 
from tkinter import *
  
# import other necessery modules 
import random 
import time 
import datetime 
import math
import random

def decompose(n):
    exponentOfTwo = 0

    while n % 2 == 0:
        n = n // 2  # using / turns large numbers into floats
        exponentOfTwo += 1

    return exponentOfTwo, n


def isWitness(possibleWitness, p, exponent, remainder):
    if pow(possibleWitness, remainder, p) == 1:
        return False

    if any(pow(possibleWitness, 2**i * remainder, p) == p - 1 for i in range(exponent)):
        return False

    return True


def probablyPrime(p, accuracy=100):
    if p == 2 or p == 3:
        return True
    if p < 2 or p % 2 == 0:
        return False

    exponent, remainder = decompose(p - 1)

    for _ in range(accuracy):
        possibleWitness = random.randint(2, p - 2)
        if isWitness(possibleWitness, p, exponent, remainder):
            return False

    return True


if __name__ == "__main__":
    n = 1

    while not probablyPrime(n, accuracy=100):
        n = random.getrandbits(512)


# creating root object 
root = Tk() 
  
# defining size of window 
root.geometry("1200x6000") 
  
# setting up the title of window 
  
Tops = Frame(root, width = 1000, relief = RAISED) 
Tops.pack(side = TOP) 
  
f1 = Frame(root, width = 35, height = 6, relief = RAISED) 
f1.pack(side = LEFT) 

  
lblInfo = Label(Tops, font = ('helvetica', 20, 'bold'),text = "The Blum-Blum-Shub Pseudorandom Generator", 
                              fg = "Black", bd = 2, anchor='w') 
                       
lblInfo.grid(row = 0, column = 0) 
lblInfo = Label(Tops, font=('arial', 15, 'bold'), fg = "Steel Blue", bd = 2, anchor = 'w') 
lblInfo.grid(row = 1, column = 0) 
  

Msg = StringVar() 
Result = StringVar() 
  
# exit function 
def qExit(): 
    root.destroy() 
    
    
# Function to reset the window 
def Reset():  
    Msg.set("") 
    Result.set("") 
  
  
#Label pentru mesaj 
lblMsg = Label(f1, font = ('arial', 16, 'bold'), 
         text = "Number of bytes", bd = 16, anchor = "w") 
           
lblMsg.grid(row = 0, column = 0) 
  
txtMsg = Entry(f1, font = ('arial', 16, 'bold'), 
         textvariable = Msg, bd = 4, insertwidth = 2, 
                bg = "powder blue", justify = 'center') 
                  
txtMsg.grid(row = 0, column = 1) 

##Label pentru rezultat
lblService = Label(f1, font = ('arial', 16, 'bold'), 
             text = "The Result", bd = 16, anchor = "n") 
               
lblService.grid(row = 1, column = 0) 
  
txtService = Entry(f1, font = ('arial', 16, 'bold'),  
             textvariable = Result, bd = 4, insertwidth = 2, 
                       bg = "powder blue", justify = 'center') 
                         
txtService.grid(row = 1, column = 1) 


def Ref(): 
    print("Number of bytes = ", (Msg.get())) 
    clear =int(Msg.get())
    clear2 = int(clear/4)
    log2 = math.log2(clear2)
    logaritm = round(log2)
    
    message = 2
    Result.set(message)
    
    import random


    def goodPrime(p):
        return p % 4 == 3 and probablyPrime(p, accuracy=100)
    

    def findGoodPrime(numBits=512):
        candidate = 1
        while not goodPrime(candidate):
            candidate = random.getrandbits(numBits)
        return candidate


    def makeModulus():
        return findGoodPrime() * findGoodPrime()


    def parity(n):
        return sum(int(x) for x in bin(n)[2:]) % 2


    class BlumBlumShub(object):
        def __init__(self, seed=None):
            self.modulus = makeModulus()
            self.state = seed if seed is not None else random.randint(2, self.modulus - 1)
            self.state = self.state % self.modulus

        def seed(self, seed):
            self.state = seed

        def bitstream(self):
            while True:
                yield parity(self.state)
                self.state = pow(self.state, 2, self.modulus)

        def bits(self, n=30):
            outputBits = ''
            for bit in self.bitstream():
                outputBits += str(bit)
                if len(outputBits) == n:
                    break

            return outputBits

    
    generator = BlumBlumShub()
    hist = [0] * 2**logaritm
    for i in range(10000):
        value = int(generator.bits(logaritm), 2)
        hist[value] += 1
     
    print(hist)
    
    with open('file.txt', 'w') as file:
        for x in hist:
            file.write("%i\n" % x)
    Result.set(hist) 
 # Show message button 
btnTotal = Button(f1, padx = 30, pady = 8, bd = 16, fg = "black", 
                        font = ('arial', 16, 'bold'), width = 10, 
                       text = "Show the numbers", bg = "powder blue", 
                         command = Ref).grid(row = 7, column = 1) 
  
# Reset button 
btnReset = Button(f1, padx = 16, pady = 8, bd = 16, 
                  fg = "black", font = ('arial', 16, 'bold'), 
                    width = 10, text = "Reset", bg = "green", 
                   command = Reset).grid(row = 7, column = 2) 
  
# Exit button 
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,  
                 fg = "black", font = ('arial', 16, 'bold'), 
                      width = 10, text = "Exit", bg = "red", 
                  command = qExit).grid(row = 7, column = 3) 

# keeps window alive 
root.mainloop() 
