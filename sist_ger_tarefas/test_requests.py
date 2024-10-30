import requests
token = "seueyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NDU0MzI0LCJpYXQiOjE3Mjk0NTA3MjQsImp0aSI6ImU5MmMzMWI3ZDM3NDRjNDE4ZGE3MmUxY2RiOWI3OTY4IiwidXNlcl9pZCI6MX0.n0Cv3BqHv4RTOXnA7PS7ejvc_UKQWGnlMq_5gj82v5A"
url = "http://localhost:8000/tasks/"
headers = {
    "Authorization": "Bearer <seu_token_jwt>",
    "Content-Type": "application/json"
}
data = {
    "nome": "Nova Tarefa",
    "descricao": "Descrição da tarefa",
    "status": False
}

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    try:
        response_data = response.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Erro ao decodificar JSON. Resposta não é um JSON válido.")
else:
    print("Erro:", response.status_code, response.text)