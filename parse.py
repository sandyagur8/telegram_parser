import json
from datetime import datetime

# Read the JSON file
with open('result.json', 'r') as file:
    data = json.load(file)

# Open a text file for writing
with open('output.txt', 'w', encoding='utf-8') as output_file:
    # Iterate through each message in the messages array
    for message in data['messages']:
        # Extract the required fields
        actor = message.get('from', 'Unknown')
        text = message.get('text', '')
        date = message.get('date', '')
        reply_to = message.get('reply_to_message_id', 'None')

        # Convert the date string to a more readable format
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
            formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            formatted_date = date  # Use the original date string if parsing fails

        # Create the output string
        output_string =f"{actor} said {text} at {formatted_date} : replied to :{reply_to}"
        output_string = (output_string).replace("\\n","") +"\n"
        # Write the output string to the file
        output_file.write((output_string))

print("Messages have been written to output.txt")
