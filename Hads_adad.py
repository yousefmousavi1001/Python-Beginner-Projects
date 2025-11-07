import random
while True:
      try:
           low =int(input("low :"))
           high =int(input("high :"))
           adad_random = random.randint(low, high)
      except:
          print("please enter a number")
      for i in range(5):
            hads = int(input(f"hads{i+1}: "))
            if hads>adad_random:
                print("smaller than!")
            elif hads < adad_random:
                 print("bigger than!")
            elif hads==adad_random:
                  print("perfect,you won(❁´◡`❁)")
                  break
            else:
                print("finish!")
