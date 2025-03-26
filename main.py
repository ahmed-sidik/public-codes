def linearGenerator(n, a, c, Xo, M):
    array = []
    seed = Xo
    for _ in range(n):
        x = (a * seed + c) % M
        seed = x
        array.append(x)
    return array

def countGenerated(array, M):
    proportionArr = [0] * 10
    for number in array:
        proportionArr[int(number*10/M)]+=1

    print(proportionArr)

n = 100000
a = 69069
c = 1
Xo = 15
M = 2**31

generatedArr = linearGenerator(n,a,c,Xo,M)
countGenerated(generatedArr, M)

def registerGenerator(p, q, n):
    startingArr = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    generatedArr2 = []
    for _ in range(n):
        pBit = startingArr[p-1]
        qBit = startingArr[q-1]
        xoredValue = (pBit + qBit) % 2
        startingArr.pop()
        startingArr.insert(0,xoredValue)
        GeneratedNumber = 0
        for i in range(31):
            power = 2**i
            GeneratedNumber += startingArr[i] * power

        generatedArr2.append(GeneratedNumber)

    return generatedArr2

n = 100000
p = 7
q = 3
generatedArr2 = registerGenerator(p, q, n)
#print(generatedArr2)
countGenerated(generatedArr2, M)

