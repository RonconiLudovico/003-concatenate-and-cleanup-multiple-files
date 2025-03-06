import sys

def read_files(files):
    for file in files:
        with open(file, 'r') as new_f:
            lines = new_f.readlines()
            for line in lines:
                return line


def concatenate_files(files):
    new_file = "new_file.txt"
    with open(new_file, 'w') as f_new:
        for i in files:
            with open(i, 'r') as f:
                lines = f.readlines()

                for line in lines:
                    f_new.write(line)
    

def clean_dataset(files):
    pass

            

def main():
    try:
        command = sys.argv[1]
    except IndexError:
        print("Accepted commands are: < read >, < link >, < clean >")
        sys.exit(1)

    original_files = ["products1.txt", "products2.txt", "products3.txt"]
    
    
    if command == "read":
        read_files(original_files)

    elif command == "link":
        concatenate_files(original_files)
    
    elif command == "clean":
        clean_dataset(original_files)
    
    else:
        sys.exit()



if __name__ == "__main__":
    main()