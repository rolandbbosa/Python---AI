import openai

openai.api_key = ""

print('What is on your mind?')


def ai():
    prompt = input('INPUT...  ')

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt= prompt,
        temperature=0.4,
        max_tokens=1000,
    )

    ans = response.choices[0].text

    print(ans)

while True:
    ai()
