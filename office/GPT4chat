#  pip install g4f

from g4f.client import Client

client = Client()


def answer(question: str) -> str:

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content

def main():
    while True:
        question = input('\nВведите ваш вопрос > ')
        print(answer(question))


if __name__ == '__main__':
    main()
