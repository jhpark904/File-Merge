# PROGRAMMING ASSIGNMENT 07
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def main():
    """The program does the following:
    - it inserts all the content from file2.txt to the beginning of file1.txt
    
    Note: After execution of the your program, only file1.txt is updated, file2.txt does not change."""
    #WRITE YOUR PROGRAM HERE
    
    f1 = open('file1.txt', 'r')
    content1 = f1.read()       #save the content of file1
    f1.close()      #close to reopen in write mode later
    f2 = open('file2.txt', 'r')
    content2 = f2.read()
    f1 = open('file1.txt', 'w')     #write mode to start with file2 content
    f1.write(content2 + content1)
    f1.close()
    f2.close()
    

#Call the main() function
main()
