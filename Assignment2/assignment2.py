"""
Author: "Frank" Chude Qian 
Email: CXQ41@case.edu
Example usage: "python .\assignment2.py .\example-002\schema.txt .\example-002\data.txt"
"""
import sys
#! Global Variables
SCHEMA_FILE_NAME = "schema_file.txt"
DATA_FILE_NAME = "data_file.txt"
LINE_WIDTH = 0
WIDTH_INTEGER = 0
VALID_LINE = 0
INVALID_LINE = 0

line_count = 0

#! Terminal Control tag
DEBUG = False
MINIMAL = True


"""
-----Requirenment-----Requirenment
1. Read in a schema file line by line.
    a. Discard commented lines (lines starting with the ‘#’ character).
    b. Parse all other lines to identify the WIDTH_INTEGER (see format rules below).
        i. Sum all of the WIDTH_INTEGER values contained in the schema file to calculate a total width value LINE_WIDTH.
2. After parsing the schema file and calculating LINE_WIDTH:
    a. Read through the provided data file line by line.
        i. Calculate the number of lines that have total with equal to LINE_WIDTH (do not count the trailing newline character). These are the valid lines in the data file.
        ii. Calculate the number of lines that have a width not equal to LINE_WIDTH. These are the invalid lines in the data file.
3. Print the number of valid lines followed by the number of invalid lines to stdout. The values should be separated by a single space and there should be no trailing whitespace.
"""


def customPrint(input_str, level=0):
    """
    Parameters
    ----------
    input_str : str
        The text string you want to print it out. It must be a string.

    level : int
        The information level of the string.
    """
    message = str(input_str)
    if level == 0:
        if DEBUG:
            print("[DEBUG]"+message)
    elif level == 1:
        if not MINIMAL:
            print("[INFO]"+message)
    elif level == 2:
        print("[WARNING]"+message)
    elif level == 3:
        print("[ERROR]"+message)
    elif level == 4:
        print("[CRITICAL]"+message)
    elif level == 5:
        print("[FATAL]"+message)
    else:
        print(message)


#! Input parameter parser
try:
    SCHEMA_FILE_NAME = sys.argv[1]
    DATA_FILE_NAME = sys.argv[2]
except IndexError:
    sys.stdout.write("0 0")
    customPrint(
        "No input arguments specified. Please use 'python3 assignment2.py SCHEMA_FILE_ADDRESS DATA_FILE_ADDRESS'", 5)
    sys.exit(99)
except:
    sys.stdout.write("0 0")
    customPrint("Some other issue observed. Please check...", 5)
    sys.exit(99)
else:
    customPrint("schema file name: "+SCHEMA_FILE_NAME)
    customPrint("data file name: "+DATA_FILE_NAME)
finally:
    customPrint("File name intake completed successfully", 1)

#! File validity checker:
try:
    #! Schema Processing
    with open(SCHEMA_FILE_NAME, 'r') as schema:
        for line in schema:
            # ? Judge if the line is comment or not
            if line.startswith("#"):
                line_count = line_count+1
                customPrint("Line"+str(line_count)+"Comment Line/r/n")
                continue
            else:
                # ? Line not comment, search for width
                options = line.split()

                line_count = line_count+1
                customPrint("Line"+str(line_count))
                customPrint(str(options))

                # ? Search for the keyword in the line
                try:
                    index = options.index("width")
                except ValueError:
                    customPrint("Line does not contain keywords!", 3)
                    continue
                else:
                    customPrint("Width keyword found! AT:"+str(index))

                # ? Read the index value and summarize them
                try:
                    WIDTH_INTEGER = int(options[index+1])
                except ValueError:
                    customPrint("Things after Width is not a value!!!", 4)
                    continue
                else:
                    LINE_WIDTH = WIDTH_INTEGER + LINE_WIDTH
    customPrint("Schema File Shows LINE_WIDTH = "+str(LINE_WIDTH), 1)

    #! Data Processing
    with open(DATA_FILE_NAME, 'r') as dataFile:
        for line in dataFile:
            customPrint("Line Length is: "+str(len(line)), 1)
            if(len(line) == (LINE_WIDTH+1)):
                VALID_LINE = VALID_LINE+1
            else:
                INVALID_LINE = INVALID_LINE+1

#! File not found protection
except FileNotFoundError:
    customPrint("File is not found!", 5)
except:
    customPrint("Other issue causing file open failed.", 5)
    sys.exit(99)
else:
    sys.stdout.write(""+str(VALID_LINE)+" "+str(INVALID_LINE))
finally:
    customPrint("Program Complete", 1)
