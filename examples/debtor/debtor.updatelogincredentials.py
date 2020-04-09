from hostfact_api import HostFactAPI

api = HostFactAPI()

debtorParams = {
    'Username': 'DB0001',
    'EmailAddress': 'info@company.com',
    'Password': 'newpassword',
    'SendPasswordForgotEmail': 'yes',
}

response = api.sendRequest('debtor', 'updatelogincredentials', debtorParams)

print(response)
