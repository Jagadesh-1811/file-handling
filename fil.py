
try:
    with open("py.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("Error: The file 'py.txt' was not found.")
