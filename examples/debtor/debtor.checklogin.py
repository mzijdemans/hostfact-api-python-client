from hostfact_api import HostFactAPI

api = HostFactAPI()

debtorParams = {
				'Username': 'DB0001',
				'Password': '3e5cd56E'
}

response = api.sendRequest('debtor', 'checkLogin', debtorParams)

print(response)