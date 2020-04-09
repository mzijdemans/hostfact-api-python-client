from hostfact_api import HostFactAPI

api = HostFactAPI()

debtorParams = {
    'Identifier': 1,
    'TemplateID': 3,
    'ServiceID': 1,
    'ServiceType': 'hosting'
}

response = api.sendRequest('debtor', 'generatepdf', debtorParams)

print(response)
