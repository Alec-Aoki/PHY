x = int(input())
y = int(input())
z = int(input())
n = int(input())

list = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if ((i+j+k) != n)]
print(list, end='')

#for i in range(0, x+1):
#    for j in range(0, y+1):
#        for k in range(0, z+1):
#            if((i+j+k) != n):
#                if((i == x) and (k == z)):
#                    print("[", i, ",", j, ",", k, "]")
#                else:
#                    print("[", i, ",", j, ",", k, "],", end='')