# ruleid: silent-exception-suppression
try:
    raise ValueError
except:
    pass

try:
    raise ValueError
except:
    print("we ded")
