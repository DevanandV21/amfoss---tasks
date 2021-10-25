thegirlwhodoesnotexist,sandesh=map(int,input("Enter numbers of both the player . Make sure that you give a space between two numbers: ").split())
for i in range(1,20+1):
  if i%2!=0:
    print(i,end=" ")
print("\nSandesh can choose any number from the above one to make the_girl_who_does_not_exist win the game")
#sandesh=int(input("Sandesh number is:"))
if thegirlwhodoesnotexist%2==0 and sandesh%2==0:
  print("Both of you got EVEN NUMBER")
elif thegirlwhodoesnotexist%2==0 and sandesh%2!=0:
  print("the_girl_who_does_not_exist won the game")
elif thegirlwhodoesnotexist%2!=0 and sandesh%2==0:
  print("Sandesh won the game")
else:
  print("The game is Tie")
