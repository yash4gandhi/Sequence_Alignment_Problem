import time
import tracemalloc
import sys


class sequenceAlignment:

    alpha = {'AA': 0, 'CC': 0, 'GG': 0, 'TT': 0, 'AC': 110, 'CA': 110, 'AG': 48, 'GA': 48, 'AT': 94, 'TA': 94,
             'CG': 118, 'GC': 118, 'CT': 48, 'TC': 48, 'GT': 110, 'TG': 110}

    def stringGenerator(self, string, listOfIndex):
        stringList = list(string)
        for i in listOfIndex:
            stringList = stringList[0:i + 1] + stringList + stringList[i + 1:]
        return "".join(stringList)

    def spaceEfficientAlignment(self, X, Y, flag):
        dp = []
        gapPenalty = 30
        for i in range(2):
            dp.append([0] * (len(Y) + 1))
        for i in range(len(Y) + 1):
            dp[0][i] = gapPenalty * i

        if flag == 0:
            for i in range(1, len(X) + 1):
                dp[1][0] = i * gapPenalty
                for j in range(1, len(Y) + 1):
                    dp[1][j] = min(dp[0][j - 1] + self.alpha[X[i - 1] + Y[j - 1]],
                                   dp[0][j] + gapPenalty,
                                   dp[1][j - 1] + gapPenalty)
                # dp[0] = dp[1]
                for j in range(len(Y)+1):
                    dp[0][j] = dp[1][j]
        elif flag == 1:
            for i in range(1, len(X) + 1):
                dp[1][0] = i * gapPenalty
                for j in range(1, len(Y) + 1):
                    dp[1][j] = min(dp[0][j - 1] + self.alpha[X[len(X) - i] + Y[len(Y) - j]],
                                   dp[0][j] + gapPenalty,
                                   dp[1][j - 1] + gapPenalty)
                for j in range(len(Y) + 1):
                    dp[0][j] = dp[1][j]
        final = dp[1]

        return final

    def seqAlignment(self, string1, string2):
        dp = []
        gapPenalty = 30
        for i in range(len(string1) + 1):
            dp.append([0] * (len(string2) + 1))

        for i in range(len(string2) + 1):
            dp[0][i] = i * gapPenalty
        for i in range(len(string1) + 1):
            dp[i][0] = i * gapPenalty
        for i in range(1, len(string1) + 1):
            for j in range(1, len(string2) + 1):
                string = string1[i - 1] + string2[j - 1]
                # print("string:", string)
                dp[i][j] = min(dp[i - 1][j - 1] + self.alpha[string],
                               dp[i][j - 1] + gapPenalty, dp[i - 1][j] + gapPenalty)
        i, j = len(string1), len(string2)
        x = ""
        y = ""
        # print("row:", row)
        # print("col:", col)
        while i and j:
            if dp[i][j] == dp[i - 1][j - 1] + self.alpha[string1[i - 1] + string2[j - 1]]:
                x = string1[i - 1] + x
                y = string2[j - 1] + y
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j] + gapPenalty:
                x = string1[i - 1] + x
                y = "_" + y
                i -= 1
            elif dp[i][j] == dp[i][j - 1] + gapPenalty:
                x = "_" + x
                y = string2[j - 1] + y
                j -= 1

        while i:
            x = string1[i - 1] + x
            y = "_" + y
            i -= 1
        while j:
            x = "_" + x
            y = string2[j - 1] + y
            j -= 1
        # print("x:", x)
        # print("y:", y)
        return [x, y, dp[len(string1)][len(string2)]]

    def DandC(self, str1, str2):
        m = len(str1)
        n = len(str2)
        if m < 2 or n < 2:
            return self.seqAlignment(str1, str2)
        else:
            firstHalf = self.spaceEfficientAlignment(str1[:m // 2], str2, 0)
            # print("firstHalf:", firstHalf)
            # print("firstHalf:", len(firstHalf))
            secondHalf = self.spaceEfficientAlignment(str1[m // 2:],
                                                      str2, 1)
            # print("secondHalf:", secondHalf)
            # print("secondHalf:", len(secondHalf))
            newArray = [firstHalf[j] + secondHalf[n - j] for j in range(n + 1)]
            # newArray = firstHalf + secondHalf[::-1]
            # print("newArray:", len(newArray))
            q = newArray.index(min(newArray))
            # print("q:", q)
            callLeft = self.DandC(str1[:len(str1) // 2], str2[:q])
            callRight = self.DandC(str1[len(str1) // 2:], str2[q:])
            l = [callLeft[r] + callRight[r] for r in range(3)]
            # print(l)
        return [callLeft[r] + callRight[r] for r in range(3)]


if __name__ == "__main__":
    filename = sys.argv[-1]
    f = open(filename, 'r')
    alphabet1 = f.readline()
    while alphabet1[-1] in ['\n', '\r']:
        alphabet1 = alphabet1[:-1]
    # print(alphabet1)
    numbers = f.readline()
    while numbers[-1] in ['\n', '\r']:
        numbers = numbers[:-1]
    index1 = []
    while numbers.isnumeric():
        index1.append(int(numbers))
        numbers = f.readline()
        while numbers[-1] in ['\n', '\r']:
            numbers = numbers[:-1]
    # print(index1)
    # print(numbers)
    alphabet2 = numbers
    numbers = f.readline()
    # print(numbers)
    while numbers[-1] in ['\n', '\r']:
        numbers = numbers[:-1]
    # print(int(numbers))
    # print(not numbers.isnumeric())
    index2 = []
    while len(numbers) != 0:
        index2.append(int(numbers))
        numbers = f.readline()
        # print(numbers)
    # print(index2)
    f.close()
    # alphabet1=["ACGT"]
    # alphabet2=["TACG"]
    # index1 = [3, 5, 8, 24, 50, 78, 100, 300]
    # index2 = [1, 3, 7, 19, 30, 20, 90, 68]
    obj = sequenceAlignment()
    string1 = obj.stringGenerator(alphabet1, index1)
    string2 = obj.stringGenerator(alphabet2, index2)
    #print("pssize:",len(string1)+len(string2))
    start = time.time()
    tracemalloc.start()
    Output = obj.DandC(string1, string2)
    memoryTaken = tracemalloc.get_traced_memory()[1]
    #print("memoryTaken:", float(memoryTaken))
    tracemalloc.stop()
    end = time.time()
    timeTaken = end - start
    #print("timeTaken:", float("{:.3f}".format(timeTaken)))
    # print("Seq1:", Output[0])
    # print("Seq2:", Output[1])
    #print("Score:", Output[2])
    f = open("output.txt", 'w')
    f.write(Output[0][:50].rstrip('\n'))
    f.write(" "+Output[0][len(Output[0])-50:] + "\n")
    f.write(Output[1][:50].rstrip('\n'))
    f.write(" " + Output[1][len(Output[1]) - 50:] + "\n")
    f.write(str(float(Output[2])) + "\n")
    f.write(str(float("{:.3f}".format(timeTaken))) + "\n")
    f.write(str(float(memoryTaken/1000)))
    f.close()


