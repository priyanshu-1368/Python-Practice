def check_employee(**kwargs):
    required_fields = ["name", "department", "salary"]
    missing_fields = [field for field in required_fields if field not in kwargs]
    
    if missing_fields:
        print("Missing required fields:", missing_fields)
    else:
        print("All required employee details provided:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

check_employee(name="Alice", department="IT")
check_employee(name="Bob", department="HR", salary=50000)