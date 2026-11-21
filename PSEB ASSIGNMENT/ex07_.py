bill =int(input("Enter bill amount:"))
discount=0
if bill >= 5000:
    discount=bill * 0.10
    print(f"your bill is:{bill}")
    print("your discount is:",discount)

elif bill >=2000 and bill <4999:
    discount=bill * 0.05
    print(f"your bill is:{bill}")
    print("your discount is:",discount)
else:
    print("your amount",bill)
    print("your discount is:",discount)


