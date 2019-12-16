# Write a function that, given a list and a target sum, returns zero-based indices of any two
# distinct elements whose sum is equal to the target sum. If there are no such elements, the
# function should return (-1,-1)

# For example, find_two_sum([1,3,5,7,9], 12) should return a tuple containing any of the following pairs of indices:
# - 1 and 4(3+9=12)
# - 2 and 3(5+7=12)
# - 3 and 2(7+5=12)
# - 4 and 1(9+3=12)

class TwoSum:
    @staticmethod
    def find_two_sum(numbers, target_sum):
        targets = ()

        for index in range(0, len(numbers)):
            numberTmp = numbers[index]
            index2 = 0
            for number in numbers:
                sumTmp = number + numberTmp
                if sumTmp == target_sum:
                    target = []
                    target.append(index)
                    target.append(index2)
                    targets = targets + (target,)
                index2 = index2 + 1
        if not targets:
            targets = (-1,-1)
            return targets

        return targets

print(TwoSum.find_two_sum([1,3,5,7,9],12))
