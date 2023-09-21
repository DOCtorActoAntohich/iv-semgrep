def read_lines(file):
    # ruleid: raw-open-call
    file = open(file, "r")
    lines = file.readlines()
    file.close()

    return lines


# ruleid: raw-open-call
with open("secret.txt", "w") as file:
    file.write("top secret!!!")
