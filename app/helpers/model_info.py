from app.services.ai_client import client
models = client.models.list()

for m in models:
    print(m.name)
