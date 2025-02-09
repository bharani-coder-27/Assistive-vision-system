import openai
import os

openai.api_key = #openai api key

def get_ai_suggestions(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    response_str = response["choices"][0]["message"]["content"].strip()
    return response_str