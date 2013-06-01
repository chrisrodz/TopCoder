def getmax(I, t):
    gets = [x-x for x in range(1,50)]
    for time,tailpos in zip(t,I):
        for i in range(time,time+tailpos+1):
            gets[i] += 1
    count = max(gets)
    gets.remove(count)
    count += max(gets)
    return count

a = [2, 4, 3, 2, 2, 1, 10]
b = [2, 6, 3, 7, 0, 2, 0]

print getmax(a,b)