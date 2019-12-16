# Return True if the substrings 'John' and 'Mary' appear the same number of
# times in the given string: otherwise return False
# String comparison should be case insensitive

class WordCount:

    @staticmethod
    def john_mary(str):
        str = str.lower()
        str = str.split('&')
        counter_john = 0
        counter_mary = 0
        for word in str:
            if word == "john":counter_john +=1
            if word == "mary":counter_mary +=1
        if counter_john == counter_mary: return True
        return False

print(WordCount.john_mary('John&Mary'))
