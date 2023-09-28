### Use of Continues loop


while True:
    line = input("Enter your Words: ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done")