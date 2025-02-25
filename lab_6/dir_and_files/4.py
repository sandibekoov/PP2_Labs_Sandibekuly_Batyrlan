file_path = input()

try:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))
except FileNotFoundError:
    print("File not found.")
