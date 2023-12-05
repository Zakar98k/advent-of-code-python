
# Input file located in src/ directory
# Input file is the same as part 1
input_file = open('day-1-input.txt', "r")
lines = input_file.readlines()
for line in lines:
    line.strip()
input_file.close()

# Every element in vectors is a tuple containing the first and last
# digit respectively
vectors = []

calibration_values = []

digits_dict = {
    "one": 1,"two": 2,"three": 3,"four": 4,"five": 5,
    "six": 6,"seven": 7,"eight": 8,"nine": 9
}


def get_vector(line):

    # Array containing every valid digit in the line
    digits = []

    # For each char in the line
    for index, char in enumerate(line):
        if char.isdigit():
            digits.append(char)
        else:
            # Check if substring starting from index matches valid digits
            for i in range(len(line)):
                if line[index:i] in digits_dict.keys():
                    digits.append(digits_dict[line[index:i]])
            
    #print(digits)

    # Return a tuple countaining the first and last digits
    return (digits[0], digits[-1])


def vector_to_int(vector):
    s = ""

    for i in vector:
        s += str(i)
    
    return int(s)

        
def main():

    # Get first and last digit from each line
    for line in lines:
        vectors.append(get_vector(line))
    
    # Combine the vectors into ints, then append them to a new array
    for vector in vectors:
        calibration_values.append(vector_to_int(vector))

    answer = sum(calibration_values)
    print(answer)

main()