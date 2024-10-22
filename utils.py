import openai
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI()

# Generate product description using the latest OpenAI API (>=1.0.0)
def generate_description(input):

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[

        {"role": "system", "content": "You are a product description generator. Generate a rich text product description with emojis."},
        {"role": "user", "content": input}
    ]
    )
    return completion.choices[0].message

#print(generate_description("shoes"))





    


   