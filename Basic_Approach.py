import time
import tracemalloc
import sys


class sequenceAlignment():

    alpha = {'AA': 0, 'CC': 0, 'GG': 0, 'TT': 0, 'AC': 110, 'CA': 110, 'AG': 48, 'GA': 48, 'AT': 94, 'TA': 94,
             'CG': 118, 'GC': 118, 'CT': 48, 'TC': 48, 'GT': 110, 'TG': 110}

    def stringGenerator(self, string, listOfIndex):
        # print("string:", string)
        # print("listOfIndex:", listOfIndex)
        stringList = list(string)
        for i in listOfIndex:
            stringList = stringList[0:i + 1] + stringList + stringList[i + 1:]
            # print("stringList:", stringList)
        return "".join(stringList)

    def seqAlignment(self, string1, string2):

        dp = [[0] * (len(string2) + 1) for i in range(len(string1) + 1)]
        gapPenalty = 30
        for i in range(0, len(string2) + 1):
            dp[0][i] = i * gapPenalty

        for i in range(1, len(string1) + 1):
            dp[i][0] = i * gapPenalty

        for i in range(1, len(string1) + 1):
            for j in range(1, len(string2) + 1):
                string = string1[i - 1] + string2[j - 1]
                dp[i][j] = min(dp[i - 1][j - 1] + self.alpha[string],
                               dp[i-1][j] + gapPenalty, dp[i][j-1] + gapPenalty)

        i, j = len(string1), len(string2)
        x = ""
        y = ""

        while i and j:

            # print("string:", string)
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
        return x, y, dp[len(string1)][len(string2)]


if __name__ == '__main__':
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
    obj = sequenceAlignment()
    string1 = obj.stringGenerator(alphabet1, index1)
    string2 = obj.stringGenerator(alphabet2, index2)
    #print("pssize:", len(string1) + len(string2))
    start = time.time()
    tracemalloc.start()
    Output = obj.seqAlignment(string1, string2)
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
    f.write(" " + Output[0][len(Output[0]) - 50:] + "\n")
    f.write(Output[1][:50].rstrip('\n'))
    f.write(" " + Output[1][len(Output[1]) - 50:] + "\n")
    f.write(str(float(Output[2])) + "\n")
    f.write(str(float("{:.3f}".format(timeTaken))) + "\n")
    f.write(str(float(memoryTaken/1000)))
    f.close()
