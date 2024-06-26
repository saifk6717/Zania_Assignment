import openai
from config import OPENAI_API_KEY

#Load the OpenAI API key
openai.api_key = OPENAI_API_KEY

#Function to get answers from OpenAI API
def get_answer_from_text(question, text_chunk):
    #Defining the messages for chat
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Text: {text_chunk}"},
        {"role": "user", "content": f"Question: {question}"}
    ]
    #Calling the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        max_tokens=100
    )
    #Extracting and returning the answers
    answer = response.choices[0].message['content'].strip()
    return answer if answer else "Data Not Available"

