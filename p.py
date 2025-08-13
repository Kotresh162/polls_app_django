n = int(input())
BinaArr = []
while n>0:
    BinaArr.append(n%2)
    n//=2
power = []
power.append(2**(BinaArr[:-1]))
print(power)