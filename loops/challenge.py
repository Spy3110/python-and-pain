for i in range(1,51):
  if i == 1 :
    print("prime")
  elif i%3 == 0 & i%5 == 0:
   print("Frizzbuzz")
  elif i%3 == 0:
   print("Fizz")
  elif i%5 == 0:
   print("Buzz")
  else :
   print(i)