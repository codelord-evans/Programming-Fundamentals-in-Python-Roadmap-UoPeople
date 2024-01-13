import ast

def invert_dictionary(input_file, output_file):
    # Read the dictionary from the input file
    with open(input_file, 'r') as f:
        original_dict_str = f.read()
    
    # Convert the string representation of the dictionary to a Python dictionary
    original_dict = ast.literal_eval(original_dict_str)
    
    # Invert the dictionary
    inverted_dict = {}
    for key, value in original_dict.items():
        if isinstance(value, list):
            for v in value:
                inverted_dict.setdefault(v, []).append(key)
        else:
            inverted_dict.setdefault(value, []).append(key)
    
    # Write the inverted dictionary to the output file
    with open(output_file, 'w') as f:
        f.write(str(inverted_dict))

# Input and output file paths
input_file_path = 'input_dict.txt'
output_file_path = 'output_inverted_dict.txt'

# Call the function with the file paths
invert_dictionary(input_file_path, output_file_path)
