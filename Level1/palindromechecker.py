def is_palindrome(text):
    
    # Remove spaces and convert to lowercase for comparison
    cleaned_text = text.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        "madam",
        "racecar",
        "hello",
        "A man a plan a canal Panama",
        "12321",
        "123456",
        "civic",
        "noon",
        "python"
    ]
    
    for test in test_cases:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")
