def main():

    vowels = "aeiouAEIOU"
    vowel_count = 0

    print("=======Welcome to Garv's Text Analysis Tool!!=======")

    text = input("Enter your text: ")


    if len(text.strip()) == 0:
        print('Please enter some text!')
        return

    for char in text:
        for vowel in vowels:
            if char == vowel:
                vowel_count += 1


    print(f"Reversed Text: {text[::-1]}")

    print(f"Character Count: {len(text)}")

    print(f"Word Count: {len(text.split())}")

    print(f"Uppercase: {text.upper()}")

    print(f"Lowercase: {text.lower()}")

    print(f"Vowel Count: {vowel_count}")

    print(f"First Word: {text.split()[0]}")

    print(f"Last Word: {text.split()[-1]}")

    print(f"Is Palindrome?: {text == text[::-1]}")



if __name__ == '__main__':
    main()
