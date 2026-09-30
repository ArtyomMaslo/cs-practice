limit = float(input())
n = int(input())

bad = 0
over = 0
ok = 0
total = 0.0
maxi = 0.0
first = True

for i in range(n):
  s = input()
  if s == "error":
    bad = bad + 1
  else:
    x = float(s)
    ok = ok + 1
    total = total + x
    if first:
      maxi = x
      first = False
    elif x > maxi:
      maxi = x
    if x > limit:
      over = over + 1

avg = total / ok 
print(n)
print(bad)
print(over)
print(f"{maxi:.f}")
print(f"{avg:.f}")
