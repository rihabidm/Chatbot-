import requests

url = "http://127.0.0.1:5000/chat"
data = {"message": "What is the future of artificial intelligence?"}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Chatbot response:", response.json().get("response"))
else:
    print("Error:", response.status_code, response.text)
