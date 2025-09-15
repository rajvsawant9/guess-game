import random
n = random.randint(1, 100)
a = -1
guesses = 0
while (a != n):
    guesses +=1
    a = int(input("guess the number: "))
    if (a >n):
        print("lower the number please ")
    else:
        print("higher the number please ")

print (f"you guessed the number {n} correctly in {guesses} attempts")
