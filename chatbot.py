import requests

messages = []

while True:
    user_input = input("Tu: ")

    messages.append({"role": "user", "content": user_input})

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3",
            "messages": messages,
            "stream": False,
        }
    )

    reply = response.json()["message"]["content"]

    messages.append({"role": "assistant", "content": reply})

    print("AI:", reply)