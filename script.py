import openai

openai.api_key = "***"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Give me 3 ideas for apps I could build with OpenAI APIs."}
    ]
)

print(response['choices'][0]['message']['content'])
