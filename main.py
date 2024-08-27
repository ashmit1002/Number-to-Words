numbers = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
tens = {0: "", 1: "Ten", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}

isTeen = False
teens = {1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 5: "Fifteen", 6: "Sixteen", 7: "Seventeen", 8: "Eighteen", 9: "Nineteen"}
position = {0: "", 1: "", 2: "Hundred", 3: "", 4: "", 5: "Hundred", 6: "", 7: "", 8: "Hundred", 9: "", 10: "", 11: "Hundred", 12: ""}

segment = {0: "", 1: "Thousand", 2: "Million", 3: "Billion", 4: "Trillion"}

N = input("Input a number N = ")
N = int(N)
num = str(N)
size = len(num) - 1

result = ""
for i in num:
    chunk = ""
    tenMult = 10 ** size
    suffix = ""
    if isTeen == True:
        if size % 3 == 0:
            chunkNum = size / 3
            chunk = segment[chunkNum]
        suffix = position[size]
        if suffix != "":
            result += teens[int(i)] + " " + suffix + " " + chunk + " "
        else:
            result += teens[int(i)] + " " + chunk + " "
        isTeen = False
        N = N % tenMult
        size -= 1
        continue

    if size % 3 == 1:
        result = result[:-1]
        if size % 3 == 0:
            chunkNum = size / 3
            chunk = segment[chunkNum]
        if int(i) == 1:
            isTeen = True
            N = N % tenMult
            size -= 1
            continue
        result += tens[int(i)] + " " + chunk
    else:
        if size % 3 == 0:
            chunkNum = size / 3
            chunk = segment[chunkNum]
        if N / tenMult >= 1:
            suffix = position[size]
        if suffix != "":
            result += numbers[int(i)] + " " + suffix + " " + chunk + " "
        else:
            result += numbers[int(i)] + " " + chunk + " "
    N = N % tenMult
    size -= 1
print(result)