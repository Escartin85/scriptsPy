
def conversionLetterToScore(subMark_letter):
    if (subMark_letter == "F3"): return 0
    if (subMark_letter == "F2"): return 23
    if (subMark_letter == "F1"): return 37
    if (subMark_letter == "D"): return 43
    if (subMark_letter == "D+"): return 47
    if (subMark_letter == "C"): return 53
    if (subMark_letter == "C+"): return 57
    if (subMark_letter == "B"): return 63
    if (subMark_letter == "B+"): return 67
    if (subMark_letter == "A-"): return 75
    if (subMark_letter == "A"): return 85
    if (subMark_letter == "A+"): return 95

subMark1_letter = "A-"
subMark2_letter = "C"

subMark1_portion = 50.0
subMark2_portion = 50.0


subMark1 = conversionLetterToScore(subMark1_letter)
subMark2 = conversionLetterToScore(subMark2_letter)


scoreMark1 = subMark1 * (subMark1_portion / 100.0)
scoreMark2 = subMark2 * (subMark2_portion / 100.0)

print("1.CW  " + "\t\t\t" + str(int(subMark1_portion)) + "%" + "    " + subMark1_letter + "\t" + str(scoreMark1))
print("2.Test" + "\t\t\t\t\t" + str(int(subMark2_portion)) + "%" + "    " + subMark2_letter + "\t" + str(scoreMark2))

total_marks = scoreMark1 + scoreMark2

print(total_marks)
