# Function to select a word of a specified length from an online word list
def word_picker(long):
    # Import necessary libraries
    import urllib.request
    import random
    answerl = []  # List to hold the letters of the selected word
    # URL containing a word list
    site = "https://content.instructables.com/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
    response = urllib.request.urlopen(site)  # Open the URL and get the response
    txt = response.read()  # Read the content of the response
    words = txt.splitlines()  # Split the text into lines (words)
    # Filter words that have the specified length
    words_6 = list(filter(lambda x: len(x) == int(long), words))
    answer = ""
    while True:
        # Select a random word from the filtered list
        answer = str((random.choice(words_6)))
        # Clean the word by stripping unnecessary characters
        answer = answer.lstrip("b'").rstrip("'")
        answerl.clear()  # Clear the answer list
        x = 0
        # Split the word into individual letters and add to the answer list
        for i in answer:
            answerl.insert(x, i)
            x += 1
        # Ensure the word has unique letters and doesn't end with 's'
        if len(set(answer)) == len(answer) and answerl[-1] != "s":
            return answer  # Return the selected word


# Dictionary to store color codes for terminal text formatting
color_codes = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "gray": "\033[90m",
    "reset": "\033[0m"
}


# f"{color_codes['red']}R{color_codes['reset']}"

# Function to return the best word with unique letters, based on a list of words
def return_best_word(list_of_words, length):
    words_to_return = []  # List to store valid words
    for x in list_of_words:
        temp_list = []  # Temporary list to check unique letters
        for y in x:
            if y not in temp_list:
                temp_list.append(y)  # Add unique letters to temp_list
        if len(temp_list) >= length:  # Ensure word meets the required length
            words_to_return.append(x)
    if len(words_to_return) > 1:
        return words_to_return[0]  # Return the first valid word
    else:
        return return_best_word(list_of_words, length - 1)  # Recurse if no word meets the condition


# Function to remove the first occurrence of a specific letter in a list
def remove_letter(list, letter):
    for x in range(len(list)):
        if list[x] == letter:
            list[x] = ""  # Replace the letter with an empty string
            return list
    return list  # Return the list if letter not found


# Function to check if a word exists in the specified file or URL
def check_word(word, path, len_of_word):
    if len_of_word == 5:  # Check if the word is 5 letters long
        import re
        path = str(path)  # Convert path to string
        f = open(path, "r")
        with open(path, 'r', encoding='utf-8') as f:
            fread = f.read()
        words = re.findall(r'>(\w\w\w\w\w)</a>', fread)  # Use regex to find 5-letter words in the file
        for x in words:
            if x.upper() == word.upper():  # Check if the word matches (case-insensitive)
                return True
    else:
        import urllib.request
        site = "https://content.instructables.com/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
        response = urllib.request.urlopen(site)  # Fetch word list from the URL
        txt = response.read()
        words = txt.splitlines()
        words = [item.decode('utf-8') for item in words]  # Decode byte data into strings
        for x in words:
            if x.upper() == word.upper():  # Check if the word matches (case-insensitive)
                return True
    return False  # Return False if the word is not found


# Function to prompt user to guess a word
def guessing_word(len_of_word):
    guess = input("Guess: ")
    if guess == "exit game":  # Check if user wants to exit
        return True, "exitg"
    elif check_word(guess, 'C:\\Users\\Rishik\\PycharmProjects\\pythonProject\\Wordle\\5_Letter_Words.html',
                    len_of_word):
        return True, guess  # Return the valid guess
    else:
        print("Guess a proper word!")  # Prompt again if the word is invalid
        return guessing_word(len_of_word)  # Recursively prompt for another guess


# Main function to play the Wordle game
def wordle(board, answer, len_of_word):
    from tabulate import tabulate  # Import tabulate for displaying the board
    #print(answer)  # Display the correct answer
    amount_of_guesses = 0  # Initialize guess count
    while amount_of_guesses < len(board):  # Limit guesses based on board size
        #x, word_guess = guessing_word(len_of_word)  # Get the user's guess
        word_guess = input("Guess: ")
        x = True
        if x:
            if len(word_guess) == len_of_word:  # Ensure the word length is correct
                if word_guess == answer:  # Check if the guess matches the answer
                    new_row = [""] * len_of_word
                    for x in range(len(new_row)):
                        new_row[
                            x] = f"{color_codes['green']}{answer[x]}{color_codes['reset']}"  # Color code for correct letters
                    board[amount_of_guesses] = new_row
                    print(tabulate(board, tablefmt='fancy_grid'))  # Display the updated board
                    print(f"{color_codes['green']}Congrats, you have won!{color_codes['reset']}")
                    return True
                elif word_guess == "exitg":  # Exit the game if requested
                    break
                else:
                    new_row = [""] * len_of_word
                    temp_word_letters = list(answer)
                    # Check for correct, yellow, or gray letters and update the board accordingly
                    for x in range(len(word_guess)):
                        if word_guess[x] == answer[x]:
                            new_row[x] = f"{color_codes['green']}{word_guess[x]}{color_codes['reset']}"
                            temp_word_letters = remove_letter(temp_word_letters, word_guess[x])
                        elif word_guess[x] in temp_word_letters:
                            new_row[x] = f"{color_codes['yellow']}{word_guess[x]}{color_codes['reset']}"
                            temp_word_letters = remove_letter(temp_word_letters, word_guess[x])
                        else:
                            new_row[x] = f"{color_codes['gray']}{word_guess[x]}{color_codes['reset']}"
                    board[amount_of_guesses] = new_row
                    print(tabulate(board, tablefmt='fancy_grid'))  # Display the updated board
                amount_of_guesses += 1
        #bot_suggestion = wordle_bot(board, len_of_word)  # Get suggestion from the bot
        #print(f"The Wordle bot suggests: {bot_suggestion}")  # Display the bot's suggestion

    print(f"{color_codes['red']}You have lost the game the words was{color_codes['reset']} " + answer)


# Function to generate a Wordle bot suggestion based on previous guesses
def wordle_bot(board, len_of_word):
    from functools import reduce
    import re
    lst = []
    # Process the guesses in the board to gather information
    for x in range(len(board)):
        for y in range(len(board[x])):
            if len(board[x][y]) >= 6:
                lst.append(([board[x][y][5]], board[x][y][3]))
    group_size = len_of_word
    # Reduce the list into word guesses
    result = [
        reduce(lambda x, y: x + y, lst[i:i + group_size])
        for i in range(0, len(lst), group_size)
    ]
    # Handle wordle suggestions based on word length and data from files or URL
    if len_of_word == 5:
        path = 'C:\\Users\\Rishik\\PycharmProjects\\pythonProject\\Wordle\\Wordle_Words.html'
        path = str(path)
        with open(path, "r") as f:
            fread = f.read()
            words = re.findall(r'/unscramble/(\w*)', fread)

        with open('C:\\Users\\Rishik\\PycharmProjects\\pythonProject\\Wordle\\possible_wordle_words.txt', "w") as file:
            for x in words:
                file.write(x + '\n')

        with open('C:\\Users\\Rishik\\PycharmProjects\\pythonProject\\Wordle\\possible_wordle_words.txt', "r") as file:
            words = file.readlines()

        indexed_words = [f"{word.strip()}" for word in words]
    elif len_of_word != 5:
        import urllib.request
        site = "https://content.instructables.com/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
        response = urllib.request.urlopen(site)
        txt = response.read()
        words = txt.splitlines()
        words = [item.decode('utf-8') for item in words]
        indexed_words = []
        for x in words:
            if len(x) == len_of_word:
                indexed_words.append(x)

    # Further refine the list of possible words using feedback from previous guesses
    for x in range(len(result)):
        letters = []
        for y in range(len(result[x])):
            if y % 2 == 0:
                letters.append(result[x][y][0])
        word = ''.join(letters)
        indexed_words.remove(word)

    # Functions to filter words based on guessed letters (gray, yellow, green)
    def getWordsExcludingGray(iWord, wordList):
        letters = []
        for x in range(len(iWord)):
            for y in range(len(iWord[x])):
                if iWord[x][y] == "0":
                    letters.append(iWord[x][y - 1])
        lst = []
        for x in range(len(iWord)):
            for y in range(len(iWord[x])):
                if iWord[x][y] == "2" or iWord[x][y] == "3":
                    lst.append([iWord[x][y - 1], int((y - 1) / 2)])

        foo = []
        if lst != None and letters != None:
            for x in lst:
                for y in range(len(letters)):
                    if x[0] == letters[y]:
                        if letters[y] in letters:
                            foo.append(letters[y])
        letters = [letter for letter in letters if letter not in foo]
        words = []
        for x in letters:
            for z in wordList:
                letter = re.search(f'{x}', z)
                if letter != None:
                    words.append(z)

        for word in words:
            if word in wordList:
                wordList.remove(word)
        return wordList

    def getWordsIncludingGreens(iWord, wordList):
        lst = []
        for x in range(len(iWord)):
            for y in range(len(iWord[x])):
                if iWord[x][y] == "2":
                    lst.append([iWord[x][y - 1], int((y - 1) / 2)])

        foo = []
        if len(lst) != 0:
            for x in lst:
                for word in wordList:
                    if word[x[1]] != x[0][0]:
                        foo.append(word)

        for x in foo:
            for z in wordList:
                if x == z:
                    if x in wordList:
                        wordList.remove(x)

        return wordList

    def getWordsIncludingYellows(iWord, wordList):
        letters = []
        for x in range(len(iWord)):
            for y in range(len(iWord[x])):
                if iWord[x][y] == "3":
                    letters.append([iWord[x][y - 1], int((y - 1) / 2)])

        lst = []
        for x in range(len(iWord)):
            for y in range(len(iWord[x])):
                if iWord[x][y] == "0" or iWord[x][y] == "2":
                    lst.append([iWord[x][y - 1], int((y - 1) / 2)])

        foo = []
        if lst != None and letters != None:
            for x in lst:
                for y in range(len(letters)):
                    if x[0] == letters[y]:
                        if letters[y] in letters:
                            foo.append(letters[y])
        letters = [letter for letter in letters if letter not in foo]

        foo = []
        if len(letters) != 0:
            for x in letters:
                for word in wordList:
                    if word[x[1]] == x[0][0] or x[0][0] not in word:
                        foo.append(word)

        for x in foo:
            for z in wordList:
                if x == z:
                    if x in wordList:
                        wordList.remove(x)

        return wordList

    # Filter words and print the remaining possible words
    getWordsIncludingYellows(result, getWordsIncludingGreens(result, getWordsExcludingGray(result, indexed_words)))

    print(indexed_words)

    if len(indexed_words) > 1:
        return return_best_word(indexed_words, len_of_word)  # Return the best word based on filtering
    else:
        return indexed_words[0]  # Return the single remaining word


wordle(board=[["" for _ in range(6)] for _ in range(5)], answer="think", len_of_word=5)
