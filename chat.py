import openai

openai.api_key = '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'


def chat_with_gpt3_5_turbo(messages):
    # We need to ensure that the messages are in the correct format
    for message in messages:
        if not isinstance(message, dict) or 'role' not in message or 'content' not in message:
            raise ValueError("Each message should be a dictionary with 'role' and 'content' keys")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages
    )

    return response.choices[0].message['content']


# Example usage
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Translate the following English text to French: 'Hello, world'"
    }
]
# response = chat_with_gpt3_5_turbo(messages)
# print(response)
