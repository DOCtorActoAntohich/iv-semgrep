works_fine = True
# ok: else-block
if works_fine:
    print("works fine")

s = 0
# ok: else-block
for i in range(100):
    s += i
print(s)


# ok: else-block
while s > 0:
    s -= 1


# ruleid: else-block
if 0 == 5:
    print("what in the goddamn...")
else:
    print("this must not be allowed")


# ruleid: else-block
for i, value in enumerate(range(5, 11)):
    if value % 15 == 14:
        print("found")
        break
else:
    print("not found")

# ruleid: else-block
while s < 100:
    s += 1
else:
    print("dread")

# ruleid: else-block
try:
    print(1)
except:
    print("how")
else:
    print("you idiot")
