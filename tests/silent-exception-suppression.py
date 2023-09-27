# ruleid: silent-exception-suppression
try:
    raise ValueError
except:
    pass

# It still suppresses the error, but at least it does something.
# ok: silent-exception-suppression
try:
    raise ValueError
except:
    print("we ded")
