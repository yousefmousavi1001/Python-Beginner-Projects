import random

list_name=["yousef","younes","setia","setare","tahere"
    ,"mahdi","fateme","hasti","mani","nafas","yashar","yamal","parmida",]
random_name=random.choice(list_name).lower()
guess_counter=len(random_name)
guess_list=["-"]*guess_counter
curent_guess=" ".join(guess_list)
print(curent_guess)
while guess_counter>0:
    guess = input("Enter a char : \n ")
    if guess.isalpha():
        if guess in random_name:
            if guess in guess_list:
                print("you have guessed befor,try again")
            else :
                for idx,char in enumerate(random_name):
                    if char==guess:
                        guess_list[idx]=guess
                curent_guess = " ".join(guess_list)
                print(f"Perfect!,{curent_guess}")

                if  "-" not  in guess_list:
                    print("you won,(❁´◡`❁)")
                    break
        else:
            guess_counter-=1
            print(f"wrong!,remainder is guesses {guess_counter}")
    else:
        print("please enter a valid character")
