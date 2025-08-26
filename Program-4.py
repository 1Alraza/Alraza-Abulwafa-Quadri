nums = list(map(int, input("Enter numbers separated by space: ").split()))

res = {}

for i in range(1, 10):
    count = 0
    for num in nums:
        if num % i == 0:
            count += 1
    res[i] = count

print(res)