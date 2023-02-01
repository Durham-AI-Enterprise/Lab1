# Take user input for source and destination file names
src_filename = input("Enter the source file name: ")
dst_filename = input("Enter the destination file name: ")

# Open the source file in read mode and the destination file in write mode
with open(src_filename, "r") as src_file, open(dst_filename, "w") as dst_file:
    # Read the contents of the source file
    contents = src_file.read()
    
    # Write the contents of the source file to the destination file
    dst_file.write(contents)
    
print("File copied successfully.")