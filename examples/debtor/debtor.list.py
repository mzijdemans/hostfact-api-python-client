from hostfact_api import HostFactAPI

api = HostFactAPI()

debtorParams = {
    # 'searchat': 'EmailAddress|Website',
    # 'searchfor': 'gmail.com'
}

response = api.sendRequest('debtor', 'list', debtorParams)

print(response)
