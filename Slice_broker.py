import hug
import requests
import json


class SliceBroker:

    def __init__():
        self.agents = {}

    @hug.get()
    def locate_slice_resources(pdt: hug.types.json):
        """called by the Slice Builder"""
        # Salvar a msg PDT no banco de dados mongodb, com as informações do builder que solicitou (Falta implementar).

        # Deveria decompor (Falta implementar decomposição) a msg pdt e enviar (função enviar já está implementada) para os respectivos agents que pode ser um DC ou WAN.

        return requests.get( "http://localhost:8001/push_resource_offer?ResourceDescriptor=" + json.dumps(pdt))


    @hug.get()
    def register_provider(providerId: hug.types.text, location: hug.types.text):
        """Provide an interface for the registration of Slice Agents to maintain an updated list of potential resource providers """


        # Salvar o registro dos agentes no banco de dados mongodb, identificando cada agente (Falta implementar).
        print(providerId)
        print(location)
        return {'message': "tudo blz"}
