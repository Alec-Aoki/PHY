def format_number_pairs(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()

        if len(lines) != 2:
            raise ValueError("Input file must contain exactly two lines")

        # Strip whitespace and split the lines into numbers
        numbers1 = lines[0].strip().split()
        numbers2 = lines[1].strip().split()

        # Ensure both lines have the same number of elements
        if len(numbers1) != len(numbers2):
            raise ValueError("Both lines must have the same number of elements")

        # Combine the numbers into pairs and format the output
        formatted_lines = []
        for num1, num2 in zip(numbers1, numbers2):
            formatted_lines.append(f"{num1} {num2}")

        # Write the formatted lines to the output file
        with open(output_filename, 'w') as file:
            file.write("\n".join(formatted_lines))

        return f"Formatted pairs have been written to {output_filename}"

    except FileNotFoundError:
        return f"Error: File '{input_filename}' not found"
    except ValueError as e:
        return f"Error: {e}"
    except IOError:
        return f"Error: Unable to write to file '{output_filename}'"

# Example usage
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script_name.py input_file.txt output_file.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    result = format_number_pairs(input_file, output_file)
    print(result)