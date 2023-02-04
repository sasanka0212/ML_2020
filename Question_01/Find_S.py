import csv
num_attributes = 4
a = []
print("\n The Given Training Data Set \n")

with open('PlayTennis.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a.append (row)
        print(row)
        
print("\n The initial value of hypothesis: ")
hypothesis = [0] * num_attributes
print(hypothesis)

for j in range(0,num_attributes):
    hypothesis[j] = a[1][j] 
    
print("\n The row 1 value of hypothesis: ")
print(hypothesis)

print("\n Find S: algorithm for finding most Specific Hypothesis\n")

for i in range(0,len(a)):
    if a[i][num_attributes]=='Yes':
        for j in range(0,num_attributes):
            if a[i][j]!=hypothesis[j]:
                hypothesis[j]='?'
            else :
                hypothesis[j]= a[i][j] 
    print(" For Training instance No:{} the hypothesis is ".format(i), hypothesis)

print("\n The Most Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)
