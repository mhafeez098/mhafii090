def main():
    # Ask the user for input
    user_input = input("Enter some text: ")

    # Open a file in write mode
    with open("user_input.txt", "w") as file:
        # Write the user's input to the file
        file.write(user_input)

    print("Input saved to user_input.txt")

if __name__ == "__main__":
    main()