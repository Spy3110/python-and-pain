#binary to ASCII converter and vice versa

# build functions 
def binary_to_ascii(n):
 for i in n:
    print(chr(int(i,2)), end= "") #chr() converts ascii to character

def ascii_to_binary(n):
  for i in n:
    print(bin(ord(i))[2:].zfill(8), end = " ") #ord() converts character to ascii and bin() converts ascii to binary


#take input
print("---WELCOME TO THE DEPRESSED BINARY VERSE---")

user_input = input("Press 1 to convert binary to ASCII and 0 to ASCII to binary. Dont depress me more...")

if user_input == "1":
 potato_binary = input("Enter the binary.\n").split()
 binary_to_ascii(potato_binary) #function call
elif user_input == "0":
  tomato_ascii = list(input("Enter the word.\n"))
  ascii_to_binary(tomato_ascii)
else:
  print("Do you know why binary numbers are in depression? Because nobody understands us (´。＿。｀)")