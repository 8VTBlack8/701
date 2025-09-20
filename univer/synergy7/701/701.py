def is_palindrome():
    input_string = input("Введите строку:")
    if input_string == input_string[::-1]:
        print("yes")
    else:
        print("no")
if __name__ == "__main__":
    is_palindrome()

