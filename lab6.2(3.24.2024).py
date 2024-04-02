## Lab 6 Part 2
## Open First Input File
flag = True
while flag == True:
    try:
        in1 = input("Enter The Path and Name of the First File: ")
        names_file1 = open(in1, 'r')
        flag = False
    except OSError:
        print("Error: file(s) not found or could not be opened")
        print("Please re-enter\n")
## Open Second Input File
flag = True
while flag == True:
    try:
        in2 = input("Enter The Path and Name of the Second File: ")
        names_file2 = open(in1, 'r')
        flag = False
    except OSError:
        print("Error: file(s) not found or could not be opened")
        print("Please re-enter\n")
## Open Output File
flag = True
while flag:
    try:
        out = input("Enter the path and name of the ouput file: ")
        out_file = open(out, 'w')
        flag = False
    except OSError:
        print("Error: File(s) not found or could not be opened. Please Re-enter")

## Ass names form both files to the output file
try:
    print("Names Processing Started")
    ## Add names from file 1
    for name in names_file1:
        out_file.write(str(name))
        
    names_file1.close()
    ## Add names from file 2
    for name in names_file2:
        out_file.write(str(name))
    names_file2.close()
    ## Final Messsage
    print("Process Complete")
    ## Print In Case Of Error
except IOError:
    print("Problem Reading or writing files. Program Terminating")
    nameslist1.close()
    nameslist2.close()
    allnames.close()
