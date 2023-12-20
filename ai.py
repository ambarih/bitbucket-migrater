
import openai
import json
from pymongo import MongoClient

openai.api_key = "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"

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Jfrog-Nexus"]
collection = db["Jfrog"]

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response

def extract_method_and_endpoint(response_content):
    method_endpoint_description_list = []
    
    # Split the response into sections for each API endpoint
    sections = response_content.split('\n\n')

    for section in sections:
        lines = section.split('\n')

        # Skip sections with fewer than 3 lines (not a complete API endpoint entry)
        if len(lines) < 3:
            continue

        # Extract information from the lines
        method_line = lines[1].strip()
        endpoint_line = lines[2].strip()
        description_line = lines[3].strip()

        # Extract method, endpoint, and description
        method = method_line.split(':')[-1].strip()
        endpoint = endpoint_line.split(':')[-1].strip()
        description = description_line.split(':')[-1].strip()

        method_endpoint_description_list.append({
            "method": method,
            "endpoint": endpoint,
            "description": description
        })

    return method_endpoint_description_list

if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        
        response = chat_with_gpt(user_input)
        response_content = response['choices'][0]['message']['content']
        
        print("Raw Chatgpt Response:\n", response_content)
        
        # Extract method, endpoint, and description
        extracted_data = extract_method_and_endpoint(response_content)

        # Insert into MongoDB
        if extracted_data:
            collection.insert_many(extracted_data)
            print("Data inserted into MongoDB.")

    print("\nExiting the program.")
