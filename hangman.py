import random
import hstages
word=["apple","beautiful","patoto"]
chosen=random.choice(word)
print(chosen)

list1=[]
for i in range(len(chosen)):
   list1+='_'
print(list1)

game=False
lives=6

while not game:
    
    user=input("Guess a letter:")
    for i in range(len(chosen)):
        letter=chosen[i]
        if letter==user:
            list1[i]=user
    print(list1)
    if user not in chosen:
        lives-=1
        if lives==0:
            game=True
            print("You lose!")
        #print(hstages.stages[lives])
    if '_' not in list1:
        game=True
        print("You win!")
    print(hstages.stages[lives])
    

        
