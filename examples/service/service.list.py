from hostfact_api import HostFactAPI

api = HostFactAPI()

serviceParams = {
	'searchfor': ''
}

response = api.sendRequest('service', 'list', serviceParams)

print(response)
