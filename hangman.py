                                                                            #Hangman Game

#importing the libraries
import random





#List of words.
word_list = ['horse','door','song','rip','backbone','bomb','treasure','garbage','park','pirate','ski','state','whistle','palace',
        'baseball','coal','queen','dominoes','photograph','computer','hockey','aircraft','hot','dog','salt','pepper','key','iPad',
        'whisk','frog','lawnmower','mattress','pinwheel','cake','circus','battery','mailman','cowboy','password','bicycle',
        'skate','electricity','lightsaber','thief','teapot','deep','spring','nature','shallow','toast','outside','America',
        'roller','blading','gingerbread','man','bowtie','half','spare','wax','light','bulb','platypus','music']







#The word to be found.
word = random.choice(word_list)
#Guessed word
guessed_word = list('*'*len(word))
#guessed letters
guessed_letters=[]







#function to replace '*' with the guessed letter.
def replace(guess):
    replacing_indices=[index for index,value in enumerate(word) if value==guess]
    global guessed_word
    for i in replacing_indices:
            guessed_word[i]=guess
    






#Starting the game
print('Entering the Game')
print('word = {}\n'.format(''.join(guessed_word)))





#Getting the no.of attempts to find the word from the user.
chance = 0
while not int(chance) in range(1,16):
    try:
        chance = int(input("Enter the no.of attempts you need to guess the word [1-15]"))
    except:
        print('Enter between 1 and 15')
turn = 1






#Guessing begins
while turn<=chance:
    #prints the word and the guessed letters.
    print('\nword = ',''.join(guessed_word))
    print('Guessed Letters: ', ','.join(guessed_letters))
    guess = input("turn {}\t".format(turn))



    #Executed when the letter has been already guessed.
    if guess in guessed_letters:
        print("Already Guessed\n")
        continue
    guessed_letters.append(guess)


    
    #Executed when the user finds the entire word.
    if guess == word:
        print("You found the word.\nSuccess!!!\nGame Over")
        exit(0)
        


    #Executed when the user guesses the letters in the word.
    if guess in word and len(guess)!=0:
        print('Wow! {} is in the word'.format(guess))
        replace(guess)
        
    else:
        print("Sorry!!! Better Luck Next Time")
        turn+=1
    

    #Exits, When user finds the word.
    if '*' not in guessed_word:
        print("Success!!!\nGame Over")
        exit(0)
    

#User looses the Game.
print('Game Over\nYou Loose\nThe word is "{}"'.format(word))
exit(0)
