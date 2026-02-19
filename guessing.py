import random
while True:
 try:
  hello = int(input("Enter a number so that computer will pickup a random number from your range starting from zero to your valid number: "))
  break
 except Exception as e:
  print("Please enter a valid integer value")
random_number = random.randint(0,hello)
print("---------------------------GAME_STARTS------------------------------")
print("Computer is picking up a random number and you have to guess it")
guess = 0
while True:
 guess += 1
 me = (input("Guess THE NUMBER Or Press Q for Quit : "))
 if(me.lower()=="q"):
  break
 me = int(me)
 if(me==random_number):
  print("---SUCCESS :))----CORRECT ANSWER --------")
  break
 elif(me>random_number):
  print("Your number is bigger!!, GUESS A SMALLER NUMBER:)")
 elif(me<random_number):
  print("Your number is Smaller!!, GUESS A Bigger NUMBER:)")
 else:
  print("Invalid Choice....:(")
print(f"You have guessed it in {guess} attempts: ")

print("----------------------GAME OVER--------------")
