marks = 0
marksList = []
count = 0
passMarkCount = 0


def histogram(items):
    output = ''
    output2 = ''
    output3 = ''
    output4 = ''
    for n in items:

        if n >= 70:
            output = output + "*"

        elif n >= 40:
            output2 += '*'
        elif n >= 30:
            output3 += '*'
        elif n >= 0:
            output4 += '*'

    confirm = str(input("Enter H for horizontal Histogram Printing or V for vertical Histogram printing"))
    if confirm.lower() == 'H'.lower():
        print('0-29 ' + output4)
        print('30-39 ' + output3)
        print('40-69 ' + output2)
        print('70-100 ' + output)
    else:
        header = ['0-29', '30-39', '40-69', '70-100']
        print(' '.join(header))
        for x in range(max(len(output4), len(output3), len(output2), len(output))):
            print(" {0}     {1}     {2}     {3}".format(
                '*' if x < len(output4) else ' ',
                '*' if x < len(output3) else ' ',
                '*' if x < len(output2) else ' ',
                '*' if x < len(output) else ' '
            ))


total = 0
while marks >= 0:
    try:
        marks = int(input("Enter Marks "))
    except ValueError:
        print("non-Integer isnt allowed please Re enter.")
        continue
    if marks > 100:
        print("Invalid marks")
        continue
    elif marks > 0:
        marksList.append(marks)

    else:
        print(marksList)

        histogram(marksList)
        for n in marksList:

            total += n

            if n >= 40:
                passMarkCount += 1

count = len(marksList)
avg = total / count
print("Average", avg)
print("Number of students with a pass mark", passMarkCount)
print("Highest mark", max(marksList))
print("Lowest mark", min(marksList))
