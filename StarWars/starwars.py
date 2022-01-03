
import time

# Python program to
# demonstrate readline()
# Using readline()
file1 = open('starwars.txt', 'r')
count = 0
 
while True:
    count += 1
 
    # Get next line from file
    line = file1.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    CRED = '\033[93m'
    CEND = '\033[40m'
    print(CRED+"{}".format(line.strip())+CRED)
    time.sleep(0.3)
file1.close()