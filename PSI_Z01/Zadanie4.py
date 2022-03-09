length = int(input("Length:"))

measure = "|"
numbersUnderMeasure = "0"

for i in range(0, length):
    measure += "....|"
    if i + 1 < 10:
        numbersUnderMeasure += " "
    numbersUnderMeasure += f"   {i + 1}"

print(measure)
print(numbersUnderMeasure)