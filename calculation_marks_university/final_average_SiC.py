
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

subMark1_letter = "A"
subMark2_letter = "B"
subMark3_letter = "A-"

subMark1_portion = 30.0
subMark2_portion = 30.0
subMark3_portion = 40.0


subMark1 = conversionLetterToScore(subMark1_letter)
subMark2 = conversionLetterToScore(subMark2_letter)
subMark3 = conversionLetterToScore(subMark3_letter)


scoreMark1 = subMark1 * (subMark1_portion / 100.0)
scoreMark2 = subMark2 * (subMark2_portion / 100.0)
scoreMark3 = subMark3 * (subMark3_portion / 100.0)

print("1.CW1  " + "\t\t\t\t\t" + str(int(subMark1_portion)) + "%" + "    " + subMark1_letter + "\t" + str(scoreMark1))
print("2.CW2" + "\t\t\t\t\t" + str(int(subMark2_portion)) + "%" + "    " + subMark2_letter + "\t" + str(scoreMark2))
print("3.Exam" + "\t\t\t\t\t" + str(int(subMark3_portion)) + "%" + "    " + subMark3_letter + "\t" + str(scoreMark3))

total_marks = scoreMark1 + scoreMark2 +scoreMark3

print(total_marks)
