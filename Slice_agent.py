import requests, hug


class SliceAgent:
    def __init__(self):
        # register in the broker
        requests.get("http://localhost:8000/register_provider?providerId='1'&location='Belem'")

        # Salvar a msg PDT no banco de dados slqlite, com as informações que o broker solicitou (Falta implementar).

    @hug.get()
    def push_resource_offer(ResourceDescriptor: hug.types.json):
        print( ResourceDescriptor )
        # return {Resource Element ID[], Cost}

# sa = SliceAgent()
