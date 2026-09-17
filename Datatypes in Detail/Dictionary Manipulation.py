student = {"name": "Alice", "age": 20, "grade": "A"}

# Print the keys and values
print("Keys:", student.keys())
print("Values:", student.values())
# Alternatively, print both together: print(student.items())

# Add a new key: "city": "Delhi"
student["city"] = "Delhi"

# Update "age" to 21
student["age"] = 21

# Delete the "grade" key
del student["grade"]
# Alternative: student.pop("grade")

print("Updated Dictionary:", student)