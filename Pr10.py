# Program 10: File Handling

file = open("sample.txt", "w")
file.write("Hello, Python!")
file.close()

file = open("sample.txt", "r")
content = file.read()
file.close()

print("File Content:", content)