nums = [3, 1, 3, 2, 1, 5]
uniqueNum = []
for n in nums:
    if n not in uniqueNum:
        uniqueNum.append(n)
        print(uniqueNum,"unique num is")
