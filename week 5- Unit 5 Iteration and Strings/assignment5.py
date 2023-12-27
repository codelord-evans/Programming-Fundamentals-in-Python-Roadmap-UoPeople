def main():
    name = input("Enter your name: ")

    # Display n characters from left
    n = int(input("Enter the number of characters to display from left: "))
    print("First", n, "characters:", name[:n])

    # Count the number of vowels
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in name:
        if char in vowels:
            vowel_count += 1
    print("Number of vowels:", vowel_count)

    # Reverse the name
    reversed_name = name[::-1]
    print("Reversed name:", reversed_name)

if __name__ == "__main__":
    main()