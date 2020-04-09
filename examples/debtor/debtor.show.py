from hostfact_api import HostFactAPI

api = HostFactAPI()

debtorParams = {
    'Identifier': '1'
}

response = api.sendRequest('debtor', 'show', debtorParams)

print(response)
