input_file = 'path_to_your_live_chat_file.json'
output_file = 'formatted_live_chat_file.json'

with open(input_file, 'r', encoding='utf-8') as f:  # Specify the encoding here
    lines = f.readlines()

# Add a comma at the end of each line except the last one
lines = [line.strip() + ',' if i < len(lines) - 1 else line.strip() for i, line in enumerate(lines)]

# Enclose the lines with square brackets to form a JSON array
formatted_content = '[' + '\n'.join(lines) + ']'

with open(output_file, 'w', encoding='utf-8') as f:  # Also specify the encoding here
    f.write(formatted_content)
