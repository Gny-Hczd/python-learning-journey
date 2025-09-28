a = 2
count = 0
n=10001
while count<=n:
    for i in range(2, a):
        if a % i == 0:
            break
    else:
        count+=1
    if count==n:
                print(f"{count}.prime: {a}")
                break
    a+=1