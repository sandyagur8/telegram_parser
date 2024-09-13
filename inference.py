import json
import requests
import csv

# Function to send a message to the API and get the response
def get_bot_response(message):
    url = 'https://api.devdock.ai/bot/756c52f6-a723-4b44-b5ad-559b121c6144/api'
    headers = {
        'content-type': 'application/json',
        'x-api-key': 'sk_db_3WcWg0ZDmUjR2O92c5lj1IPEbpVduUc7'
    }
    payload = {
        "message": message,
        "history": [],
        "stream": False
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()['bot']['text']
    except requests.RequestException as e:
        return f"Error: {str(e)}"

# Function to flatten the responses
def flatten_responses(responses):
    flattened = []
    for response in responses:
        if isinstance(response, list):
            flattened.extend(response)
        else:
            flattened.append(response)
    return flattened
# Load the JSON file
with open('questions_and_responses.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Prepare CSV file
with open('questions_answers_comparison.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Question', 'Telegram Answer', 'Bot Answer'])

    # Process each question
    for item in data:
        question = item['question']
        flattened_responses = flatten_responses(item['responses'])
        telegram_answer = ' | '.join(str(resp) for resp in flattened_responses)
        bot_answer = get_bot_response(question)

        # Write to CSV
        csvwriter.writerow([question, telegram_answer, bot_answer])

print("Processing complete. Output saved to 'questions_answers_comparison.csv'")
