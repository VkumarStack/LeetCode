from sys import stdin

def fieldTrip(str1, str2):
    index1 = 0
    index2 = 0
    final = ""
    while (index1 < len(str1)) and (index2 < len(str2)):
        if (str1[index1] < str2[index2]):
            final = final + str1[index1]
            index1 = index1 + 1
        elif (str1[index1] > str2[index2]):
            final = final + str2[index2]
            index2 = index2 + 1
        else:
            final = final + str1[index1] + str1[index1]
            index1 = index1 + 1
            index2 = index2 + 1
    if (index1 < len(str1)):
        final = final + str1[index1:]
    elif (index2 < len(str2)):
        final = final + str2[index2:]
    return final
    
lines = ""
count = 0
for line in stdin:
    lines += line
    count = count + 1
    if count == 2:
        break

print(fieldTrip(lines.splitlines()[0], lines.splitlines()[1]))