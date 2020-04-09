from hostfact_api import HostFactAPI

api = HostFactAPI()

productParams = {
	# 'searchfor': ''
}

response = api.sendRequest('product', 'list', productParams)

print(response)
