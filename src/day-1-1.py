
# Input file located in src/ directory
input_file = open('day-1-input.txt', "r")
lines = input_file.readlines()

# Every element in vectors is a tuple containing the first and last
# digit respectively
vectors = []

calibration_values = []

def get_vector(line):

    # Array containing every digit in the line
    digits = []

    for index, char in enumerate(line):
        if char.isdigit():
            digits.append(char)

    # Return a tuple countaining the first and last digits
    return (digits[0], digits[-1])


def vector_to_int(vector):
    s = ""

    for i in vector:
        s += i
    
    return int(s)

        
def main():

    # Get first and last digit from each line
    for line in lines:
        vectors.append(get_vector(line))
    
    # Combine the vectors into ints, then append them to a new array
    for vector in vectors:
        calibration_values.append(vector_to_int(vector))

    input_file.close()

    answer = sum(calibration_values)
    print(answer)

main()