myfile = open("Titanic.csv", "r")

menR = 0
womenR = 0
allM = 0
allW = 0
menAge = []
womenAge = []
class1 = []
class3 = []
outlinerA = []
outlinerF = []


for i in range(892):
    out = myfile.readline()
    out = out.split(',')
    

    if out[5] == "male":
        allM += 1
        if out[6] != "":
            menAge.append(float(out[6]))
    if out[5] == "female":
        allW += 1
        if out[6] != "":
            womenAge.append(float(out[6]))
    if out[1] == "0" and out[5] == "male":
        menR += 1
    if out[1] == "0" and out[5] == "female":
        womenR += 1
    

    if out[2] == "1" and out[6] != "":
        class1.append(float(out[6]))
    if out[2] == "3" and out[6] != "":
        class3.append(float(out[6]))



q1_1 = menR*100 / allM
q1_2 = womenR*100 / allW
print("Ratio of men >> ",round(q1_1), "%\nRatio of women >> ", round(q1_2), "%")

q2_1 = sum(menAge)/len(menAge)
q2_2 = sum(womenAge)/len(womenAge)
print("\nMen average age >> ", round(q2_1), "\nWomen average age >> ", round(q2_2))

q3_1 = sum(class1)/len(class1)
q3_2 = sum(class3)/len(class3)
print("\nClass 1 average age >> ", round(q3_1), "\nClass 3 average age >> ", round(q3_2))

myfile.close()