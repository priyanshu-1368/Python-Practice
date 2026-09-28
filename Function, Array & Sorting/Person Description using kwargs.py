def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

describe_person(name="John", age=28, city="New York")