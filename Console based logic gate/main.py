#CONSOLE BASED LOGIC GATES

import random

def AND(a, b):
    return int(a and b)

def OR(a, b):
    return int(a or b)

def NOT(a):
    return int(not a)

def NAND(a, b):
    return int(not (a and b))

def NOR(a, b):
    return int(not (a or b))

def XOR(a, b):
    return int((a and not b) or (not a and b))

def XNOR(a, b):
    return int((a and b) or (not a and not b))

roasts = [
    "💀 Congrats, genius. You discovered a number that doesn’t exist in digital logic.",
    "Bro... it's literally 0 or 1. Even a potato could've done it.",
    "Invalid input. I award you no points, and may your GPA rest in peace.",
    "Are you inventing quantum logic, or just trolling me?",
    "⚡ ERROR: IQ not found. Try again, mortal."
]


while True:
    try:
        A = int(input("Enter the value of A: "))
        B = int(input("Enter the value of B: "))

        if A not in (0,1) or B not in (0, 1):  # manual check
            raise ValueError("Input must be 0 or 1.")  
        
        #then print 
        print("NOT A:", NOT(A)) 
        print("AND:", AND(A,B)) 
        print("OR:", OR(A,B))   
        print("NAND:", NAND(A,B))
        print("NOR:",NOR(A,B))
        print("XOR:", XOR(A,B))
        print("XNOR:", XNOR(A,B)) 
        break 

    except ValueError as e:
        print(random.choice(roasts))




