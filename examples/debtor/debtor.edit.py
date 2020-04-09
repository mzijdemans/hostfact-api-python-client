from hostfact_api import HostFactAPI

api = HostFactAPI()

debtorParams = {
    'Identifier': '1',
    'CompanyName': 'Company Y',
    'AccountName': 'Company Y'
}

response = api.sendRequest('debtor', 'edit', debtorParams)

print(response)
