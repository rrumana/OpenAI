import os
import openai

# Enter your OpenAI API key here
secretKey = ""

def askGPT(text):
    openai.api_key = secretKey

    response = openai.Completion.create(
        engine = "gpt-3.5-turbo",
        prompt = text,
    )

    return print(response.choices[0].text)

def main():
    while True:
        print('GPT: Ask me a question\n')
        myQn = input()
        askGPT(myQn)

main()
