
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
subMark2_letter = "A-"
subMark3_letter = "A"
subMark4_letter = "A-"
subMark5_letter = "A"
subMark6_letter = "A-"

subMark1_portion = 10.0
subMark2_portion = 35.0
subMark3_portion = 15.0
subMark4_portion = 15.0
subMark5_portion = 15.0
subMark6_portion = 10.0


subMark1 = conversionLetterToScore(subMark1_letter)
subMark2 = conversionLetterToScore(subMark2_letter)
subMark3 = conversionLetterToScore(subMark3_letter)
subMark4 = conversionLetterToScore(subMark4_letter)
subMark5 = conversionLetterToScore(subMark5_letter)
subMark6 = conversionLetterToScore(subMark6_letter)


scoreMark1 = subMark1 * (subMark1_portion / 100.0)
scoreMark2 = subMark2 * (subMark2_portion / 100.0)
scoreMark3 = subMark3 * (subMark3_portion / 100.0)
scoreMark4 = subMark4 * (subMark4_portion / 100.0)
scoreMark5 = subMark5 * (subMark5_portion / 100.0)
scoreMark6 = subMark6 * (subMark6_portion / 100.0)

print("1.Academic challenge/originality" + "\t\t\t" + str(int(subMark1_portion)) + "%" + "    " + subMark1_letter + "\t" + str(scoreMark1))
print("2.Analysis / research" + "\t\t\t\t\t" + str(int(subMark2_portion)) + "%" + "    " + subMark2_letter + "\t" + str(scoreMark2))
print("3.Critial reflection and conclusion" + "\t\t\t" + str(int(subMark3_portion)) + "%" + "    " + subMark3_letter + "\t" + str(scoreMark3))
print("4.Clarity of expression and readability" + "\t\t\t" + str(int(subMark4_portion)) + "%" + "    " + subMark4_letter + "\t" + str(scoreMark4))
print("5.Construction and presentation of the document" + "\t\t" + str(int(subMark5_portion)) + "%" + "    " + subMark5_letter + "\t" + str(scoreMark5))
print("6.Reference and bibliography" + "\t\t\t\t" + str(int(subMark6_portion)) + "%" + "    " + subMark6_letter + "\t" + str(scoreMark6))

total_marks = scoreMark1 + scoreMark2 + scoreMark3 + scoreMark4 + scoreMark5 + scoreMark6

print(total_marks)
