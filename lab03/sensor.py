limit = float(input)
n = int(input())

print(n)

bad = 0

for i in range(n):
  s = input(n)
  if s == "error":
    bad = bad + 1

print(bad)
