# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

from collections import Counter


def find_anagram(word, anagram):
    # [assignment] Add your code here
        if (Counter(word.casefold()) == Counter(anagram.casefold())):
            print("True")
        # elif(Counter(word) != Counter(anagram)):
        #         print("False")
        else: print("False")
        return


inp1 = (input("Enter your first word: "))
inp2 = (input("Enter your first word: "))

find_anagram(inp1,inp2)
