n = int(input())

#taking multiple inputs from a single line
list = [x for x in input().split()]

#transforming all those inputs from strs to ints
list = [eval(i) for i in list]


list.sort()
#now the highest number in the list is at its end

#we will initialize runnerup as list[n-1] for the specific case when all elements in the list are the same number
runnerup = list[n-1]

for i in range(0, n):
    if (list[i] < list[n-1]):
        #list[n-1] is the last element in the list, aka the highest number
        #whenever we find an element that is lower than that one, we store it in runnerup
        runnerup = list[i]
        #since we are not checking for <=, if we find the highest number, we will break the loop and the number in runnerup will be the highest number lower than the highest number, aka the runner-up

print(runnerup)