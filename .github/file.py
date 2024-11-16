import sys
from dbm import error

# Task 2
args = sys.argv
if len(args) == 1:
    print("There where 0 arguments when 1 was expected")
    sys.exit()
file_name = args[1]

try:
    file = open(file_name,"r")
    lines = file.readlines()
    for i in range(len(lines)):
        line = lines[i]
        words = line.split()
        if len(words) != 2:
            print("Line {} has {} numbers when 2 are expected".format(i + 1, len(words)))
        else:
            try:
                num1 = float(words[0])
                num2 = float(words[1])
                sum = num1 + num2
                print ("{} + {} = {}".format(num1,num2, sum))
            except ValueError:
                print("Line {} does not have 2 valid numbers".format(i + 1))

            
except FileNotFoundError:
    print("File of the name {} was not found".format(file_name))


'''
Test 1:
['C:\\Users\\yosem\\Documents\\GitHub\\CP_CS_101\\Week_8\\lab8-tylerpike0\\.github\\file.py', 'file_test_data_1']
['1 2\n', '5 7\n', '4.3 2.e']
1.0 + 2.0 = 3.0
5.0 + 7.0 = 12.0
Line 3 does not have 2 valid numbers

Test 2:
['C:\\Users\\yosem\\Documents\\GitHub\\CP_CS_101\\Week_8\\lab8-tylerpike0\\.github\\file.py', 'file_test_data_2']
['\n', '5\n', '1 2 3\n', 'e 1']
Line 1 has 0 numbers when 2 are expected
Line 2 has 1 numbers when 2 are expected
Line 3 has 3 numbers when 2 are expected
Line 4 does not have 2 valid numbers

Test 3:
['C:\\Users\\yosem\\Documents\\GitHub\\CP_CS_101\\Week_8\\lab8-tylerpike0\\.github\\file.py', 'file_test_data_3']
File of the name file_test_data_3 was not found

Test 4:
['C:\\Users\\yosem\\Documents\\GitHub\\CP_CS_101\\Week_8\\lab8-tylerpike0\\.github\\file.py']
There where 0 arguments when 1 was expected
'''