s_check = "Hello World"
print("Does it match?:", s_check.startswith("Hello") and s_check.endswith("World"))

garbage_text = "Data123#Science!"
clean_text = "".join([c for c in garbage_text if c.isalpha()])
print("Cleaned text:", clean_text)

print("Python reversed:", "Python"[::-1])