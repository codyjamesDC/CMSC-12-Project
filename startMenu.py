import random
from loadingSheet import readSheet

def menu():
    text()
    
    lowWords = eachWord()       #Import the list of all words
    answerSheet = readSheet()   #Import the dictionary
    correctGuess = {}           #Initialization for checking of guesses
    
    mistakes = 0

    gridActive = False          #Switching between a grid with answers and a grid with words only
    
    random.shuffle(lowWords)    #Shuffle the words at the beginning

    while True:
        if gridActive:
            giveUp(answerSheet)
            break
        else:
            showGrid(lowWords, correctGuess, answerSheet)
            lives(mistakes)
        
        print(f"""
            [1] Guess
            [2] Shuffle
            [3] Give up
            [4] Exit
            """)
        option = input("Choose your option: ")
        if option == "1":
            mistakes, correctGuess = guess(lowWords, mistakes, correctGuess, answerSheet)
            if mistakes == 4:                                           #When lives are all lost print the answer
                gridActive = True
                print("You are out of lives")
                print("The answers are ")
            elif len(correctGuess) == 4:                                #Checks if four key-value pairs exists
                print("Congratulations! You've found all categories.")
                gridActive = True
        elif option == "2":
            shuffle(lowWords)
        elif option == "3":
            print("The answers are: ")
            gridActive = True
        elif option == "4":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please try again.")

def giveUp(answerSheet):        
    print("* ================================================================================ *")
    for category, words in answerSheet.items():             #Iterates the key and values of the dictionary of answers
        theCategory = f"| {category:^80} |"                 #Centered
        print(theCategory)
        rowContent = ""
        for word in words:                                  #Get the valuess of the current category
            formattedWord = f"{word:^20}"
            rowContent += formattedWord
        print(f"| {rowContent:^60} |")
    print("* ================================================================================ *")
    
def shuffle(lowWords):
    random.shuffle(lowWords)                #Shuffle the list
    return lowWords

def guess(lowWords, mistakes, correctGuess, answerSheet):
    guess = []
    
    for i in range(4):                  #Four inputs
        while True:
            word = input(f"Enter input #{i + 1}: ").capitalize()               #Capitizalize each word for better comparison
            if word in guess:                   #Avoid duplication
                print("Word is already chosen")
                continue
            
            wordCorrectGuess = False
            for values in correctGuess.values():    #Checks if it is already guessed
                if word in values:
                    wordCorrectGuess = True
                    break
                
            if wordCorrectGuess:
                print("Word was already guessed")
                continue
            
            wordFound = False
            for eachWord in lowWords:       #Checks if the word exists in the list of words
                if word == eachWord:
                    wordFound = True
                    break
            
            if wordFound:               
                guess.append(word)
                break
            else:
                print("Input not in grid")

    while True:
        submit = input("Submit (y/n): ").lower()                #Asks the user to submit the guessed words or not
        if submit == "y":
            guess.sort()                                        #Sorts the list
            
            maxMatchCount = 0                                   #Initialization
            bestKey = ""                                        #Initialization
            
            for key, values in answerSheet.items():             #Get the category and its corresponding words
                matchCount = 0                                  #Initialization
                for word in guess:
                    if word in values:
                        matchCount += 1
                        
                if matchCount > maxMatchCount:
                    maxMatchCount = matchCount
                    bestKey = key
            
            finalCount = 0
            
            if maxMatchCount > 0:                               #Checks how many words are similar to the values of the key
                for word in guess:
                    if word in answerSheet[bestKey]:
                        finalCount += 1    
                        
            if finalCount == 4:
                print(f"Congrats! You found the right words for the {bestKey}")
                correctGuess[bestKey] = guess
                break
            elif finalCount == 3:
                print("One away!")
                mistakes += 1
                break
            elif finalCount <= 2:
                print("Wrong answer!")
                mistakes += 1
                break
        elif submit == "n":
            break
        else:
            print("Invalid input. Please try again.")

    return mistakes, correctGuess

def lives(mistakes):
    remainingMistakes = " ".join("X" * (4 - mistakes))
    print("Mistakes Remaining: ", remainingMistakes)
    
def showGrid(lowWords, correctGuess, answerSheet):
    print("* ================================================================================ *")
    guessedWords = []
    remainingWords = []
    
    for category, value in answerSheet.items():                     #Get the key or category in the answer sheet
        if category in correctGuess:                                
            print(f"| {category:^80} |")
            rowContent = ""
            for word in correctGuess[category]:                     #Prints the value of the category that were guessed correctly
                formattedWord = f"{word:^20}"
                rowContent += formattedWord
            print(f"| {rowContent:^80} |")

    for category, value in answerSheet.items():                     #Get the value of the category that were guessed correctly
        if category in correctGuess:                                
            for word in correctGuess[category]:
                guessedWords.append(word)
    
    for word in lowWords:                                           #Checks the words in list of all words and if they are guessed correctly
        if word not in guessedWords:
            remainingWords.append(word)

    if len(remainingWords) > 0:
        for i in range(0, len(remainingWords), 4):                  #Generate a sequence of indices from 0 with an increment of 4
            print(f"| {"":80} |")
            row = remainingWords[i:i + 4]                           #Get 4 words from the list
            rowContent = ""
            for word in row:                                        #Combine words into a single string
                formattedWord = f"{word:^20}"
                rowContent += formattedWord
            print(f"| {rowContent:^80} |")
    print("* ================================================================================ *")
    
def listingSheet(): #List within a list
    sheet = readSheet()
    wordList = []
    for list in sheet.values():
        wordList.append(list)
    return wordList

def eachWord(): #Normal cases
    wordList = listingSheet()
    wordCatalog = []
    for list in wordList:
        for word in list:
            wordCatalog.append(word)
    return wordCatalog

def text():
    print("""

                            ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
                            ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
                            ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
                            ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
                            ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
                            ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝

                                                ████████╗░█████╗░
                                                ╚══██╔══╝██╔══██╗
                                                ░░░██║░░░██║░░██║
                                                ░░░██║░░░██║░░██║
                                                ░░░██║░░░╚█████╔╝
                                                ░░░╚═╝░░░░╚════╝░

███╗░░██╗██╗░░░██╗████████╗     ░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
████╗░██║╚██╗░██╔╝╚══██╔══╝     ██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
██╔██╗██║░╚████╔╝░░░░██║░░░     ██║░░╚═╝██║░░██║██╔██╗██║██╔██╗██║█████╗░░██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
██║╚████║░░╚██╔╝░░░░░██║░░░     ██║░░██╗██║░░██║██║╚████║██║╚████║██╔══╝░░██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
██║░╚███║░░░██║░░░░░░██║░░░     ╚█████╔╝╚█████╔╝██║░╚███║██║░╚███║███████╗╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
╚═╝░░╚══╝░░░╚═╝░░░░░░╚═╝░░░     ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░""")

menu()