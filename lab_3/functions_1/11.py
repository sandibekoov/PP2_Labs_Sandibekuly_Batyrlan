def is_palindrome():
    word = input().replace(" ", "").lower()
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

is_palindrome()
