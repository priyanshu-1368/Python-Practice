fruits = "apple,banana,grapes".split(",")
print("Converted to List:", fruits)

words = ["Python", "is", "awesome"]
print("Converted to Sentence:", *words, sep=" ")

multiline_text = """This is line one    
This is line two
This is line three"""
for line in multiline_text.splitlines():
    print(line)