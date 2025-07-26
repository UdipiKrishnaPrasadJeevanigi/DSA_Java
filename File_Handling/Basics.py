def create_simple_file():
    file_name = "sample_file.txt"

    with open(file_name, 'w') as file:
        file.write("Hello Krishna Prasad!\n")
        file.write("This is a sample file created by python")
    
    print(f"✓ Created file: {file_name}")
    return file_name


if __name__ == "__main__":
    print("=====File Creation Examples====")

    file1 = create_simple_file()

    print("\nFiles Created Succesfully")
    print("You can view the files to see changes")