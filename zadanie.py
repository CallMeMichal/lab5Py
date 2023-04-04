slownik = {"GRADED":"","MAILED":""}
filepath = "students.txt"
with open(filepath) as file_object:
    for line in file_object:
        line.split(",")
        slownik.items().__and__(line)
        print(line.rstrip())


