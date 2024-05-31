################################
# Github Repo link
# Your Name: Tshering Dengkar
# Your Section : BBI B
# Your Student ID Number: 03230370
################################
# REFERENCES:
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://www.geeksforgeeks.org/window-sliding-technique/
# https://docs.python.org/3/tutorial/errors.html
################################
# SOLUTION: 
# Your Solution Score: 489773
################################

def extract_digits(line):
    """Extracts the first and last digit from the given line using a sliding window approach."""
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char

    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    return 0

def calculate_sum_from_file(file_path):
    """Calculates the sum of the two-digit numbers formed from each line in the input file."""
    total_sum = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    number = extract_digits(line)
                    total_sum += number
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return total_sum

# Example usage
if __name__ == "__main__":
    file_name = '370.txt'
    result = calculate_sum_from_file(file_name)
    print(f"The final result is: {result}")

