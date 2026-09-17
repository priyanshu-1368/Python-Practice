text = input("Enter any string: ")
reversed_text = text[::-1]

is_palindrome = (text == reversed_text)

print(f"Reversed string: {reversed_text}")
print(f"Is it a palindrome? {is_palindrome}")