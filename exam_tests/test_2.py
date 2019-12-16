# Write the function to slice the ruple between the given start (inclusive)
# and end (exclusive) Indexes, and join the resulting range of values a
# comma delimited string
# Example>
# TupleSlice.tuple_slice(1, 4, (76, 34, 13, 64, 12)) should return "34, 13, 64"

class TupleSlice:
    @staticmethod
    def tuple_slice(startIndex, endIndex, tup):
        string = '"'
        tup = tup[startIndex:endIndex]
        total_numbers = len(tup)
        cont = 0
        string2 = str(tup)
        # string2 = string2[1:len(string2)-1]
        string2 = string2.replace('(', '"')
        string2 = string2.replace(')', '"')
        string2 = string2.replace(' ', '')
        print("Solution 1")
        print(string2)
        print("Solution 2")
        for number in tup:
            string = string + str(number)
            cont += 1
            if cont < endIndex - 1:
                string = string + ","
        string = string + '"'
        return string


print(TupleSlice.tuple_slice(1, 4, (76, 34, 13, 64, 12)))
