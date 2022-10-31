r=[]
a=[]
for i in range(9):
    r.append(input())
    
for i in range(len(r)):
    for j in range(9):
        if r[i][j] == "#":
            a.append([i+1, j+1])
print(a)