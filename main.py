# Loads colorama module #
from colorama import Fore, Back, Style


### Functions ###

def getLetter():
 
  # Create a variable to hold the letter with a dummy value
  letter = ""
    
  # Until the user enters a string with ONE character...
  while(len(letter) != 1):
 
    # Prompt the user to enter a letter
    print()
    letter = input("Enter a Letter: ")
    print()
    letter = letter.upper() 
    guesses.append(letter)
        
  # Return the letter
  return letter  


# Create a function that displays the secret word
def displaySecretWord(wordReveal, guesses):
  
  # Go through each letter in the secret word, and determine HOW we display it
  for letter in wordReveal:
       
    # If this letter (from the secret word) has been guessed, display the letter        
    if(letter in guesses):
      
      print(letter, end=" ")
     
      
    # Otherwise, display an underscore ( _ )
    else:      
      print("_", end=" ")   
                 
    
# Create a function that determines if the user has won the game
def hasUserWon(wordReveal, guesses):
 
  # Let's use an "Innocent Until Proven Guilty" Algorithm...
  # ...and create a variable that is set to "True"
  won = True
 
  # Go through each letter in the secret word
  for letter in wordReveal:
 
    # Check if the letter has been guessed
    if(letter not in guesses):
 
      # If it has NOT been guessed, set the variable we created to False, and stop the loop
      won = False
      break
 
    
  return won
  

### Main Program ###

wordReveal = "BETTER"
letter = ""
guesses = []
strikes = 0
maxStrikes = 5


while((not hasUserWon(wordReveal, guesses)) and (strikes < maxStrikes)):
  letter = getLetter()  
  displaySecretWord(wordReveal, guesses)
  # print(end="    ")
  # print(guesses)
  
  if(letter in wordReveal):
    print(end="    ")
    print("Good choice!")
          
  else:
    strikes += 1
    print(end="    ")
    print(f"{letter} is not in the word.")
    print()
    print(f"You have {strikes} strike(s). If you get 5, you lose!")
      
  hasUserWon(wordReveal, guesses)      

if(hasUserWon(wordReveal, guesses) and (strikes < maxStrikes)):
  print()
  print(Fore.GREEN + Style.BRIGHT + "Grats. You win.")
  print(Style.RESET_ALL)
else:
  print()  
  print(Fore.RED + Style.BRIGHT + "Game over. You lose.")
  print(Style.RESET_ALL)
