import sys

# Function to read lines from a list of files
def read_files(files):
    for file in files:
        with open(file, 'r') as new_f:
            lines = new_f.readlines()
            for line in lines:
                return line  # This will return only the first line of the first file

# Function to concatenate multiple files into a single file
def concatenate_files(files):
    new_file = "new_file.txt"
    with open(new_file, 'w') as f_new:
        for i in files:
            with open(i, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    f_new.write(line)  # Write each line to the new file

# Placeholder function for cleaning the dataset
def clean_dataset(files):
    pass

# Main function to handle command line arguments and execute corresponding functions
def main():
    try:
        command = sys.argv[1]  # Get the command from the command line arguments
    except IndexError:
        print("Accepted commands are: < read >, < link >, < clean >")
        sys.exit(1)  # Exit if no command is provided

    original_files = ["products1.txt", "products2.txt", "products3.txt"]  # List of original files
    
    if command == "read":
        read_files(original_files)  # Call read_files function

    elif command == "link":
        concatenate_files(original_files)  # Call concatenate_files function
    
    elif command == "clean":
        clean_dataset(original_files)  # Call clean_dataset function
    
    else:
        sys.exit()  # Exit if an unknown command is provided

# Entry point of the script
if __name__ == "__main__":
    main()
