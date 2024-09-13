import json

def is_question(text):
    # Simple check for question mark, can be improved for more accuracy
    return '?' in text

def process_messages(data):
    messages = data['messages']
    questions = []
    
    for i, message in enumerate(messages):
        if is_question(message['text']):
            question = message['text']
            responses = []
            
            # Check the next 150 messages or until the end of the list
            for j in range(i+1, min(i+151, len(messages))):
                reply = messages[j]
                if reply.get('reply_to_message_id') == message['id'] :
                    responses.append(reply['text'])
            
            if responses:
                questions.append({
                    "question": question,
                    "responses": responses
                })
    
    return questions

# Read the JSON file
with open('result.json', 'r') as file:
    data = json.load(file)

# Process the messages
result = process_messages(data)

# Write the result to a new JSON file
with open('questions_and_responses.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=2)

print("Processing complete. Output saved to 'questions_and_responses.json'")
