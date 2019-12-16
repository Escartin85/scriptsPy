# A palindrome is a word that reads the same backward of forward
# Write a function that checks if a given word is a palindrome. Character case should be ignored.
# Fro example, is_palindrome("Deleveled") should return True as character case should be ignored, resulting in
# "deleveled", which is a palindrome since it reads the same backward and forward.

class Palindrome:

    @staticmethod
    def is_palindrome(word):
        wordTmp = ""
        word = word.lower()
        for letter in word:
            wordTmp = letter + wordTmp
        if wordTmp == word:return True
        return False


print(Palindrome.is_palindrome("Deleveled"))
