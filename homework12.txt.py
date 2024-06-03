from pprint import pprint
file_name = "byron.txt"
with open(file_name, mode="rb") as file:
    for line in file:
        print(line)
print(file.closed)










