def modify_content(content):
    # Example modification: convert to uppercase
    return content.upper()

try:
    filename = input("📄 Enter the filename to read (e.g., input.txt): ")
    with open(filename, 'r') as file:
        content = file.read()

    modified = modify_content(content)

    with open('output.txt', 'w') as file:
        file.write(modified)

    print("✅ File has been read and modified successfully. Check 'output.txt'.\n")
    print("📤 Modified Content:\n")
    print(modified)

except FileNotFoundError:
    print("❌ Error: File not found. Please check the filename and try again.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
