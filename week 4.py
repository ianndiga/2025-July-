# File Read & Write with Error Handling

# Ask the user for the input file name
input_filename = input("Enter the name of the file to read: ")

try:
    # Try to open and read the file
    with open(input_filename, "r") as file:
        content = file.read()

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Ask for the new output file name
    output_filename = input("Enter the name of the new file to save: ")

    # Write the modified content to the new file
    with open(output_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"File has been read from '{input_filename}' and saved to '{output_filename}' successfully!")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read '{input_filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")