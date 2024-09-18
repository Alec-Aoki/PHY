def generate_lines(num_lines):
    with open("output.txt", "w") as file:
        for _ in range(num_lines):
            file.write("1 1\n")

# Generate 1000 lines
generate_lines(1000)

print("1000 lines have been generated and saved to 'output.txt'.")
