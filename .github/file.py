import sys
from dbm import error

args = sys.argv
if len(args) == 0:
    print("There where 0 arguments when 1 was expected")
    sys.exit()
file_name = args[0]

try:
    file = open(file_name,"r")
    lines = file.readlines()
    for i in range(lines):
        line = lines[i]
        words = line.split()
        if len(words) != 2:
            print("Line {} has {} numbers when 2 are expected".format(i, len(lines)))
        else:
            try:
                num1 = float(words[0])
                num2 = float(words[1])
                sum = num1 + num2
                print ("{} + {} = {}".format(num1,num2, sum))
            except TypeError:
                print("Line {} does not have 2 numbers".format(i))

            
except FileNotFoundError:
    print("File of the name {} was not found".format(file_name))