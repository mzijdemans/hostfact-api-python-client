from hostfact_api import HostFactAPI

api = HostFactAPI()

vpsParams = {
				# Get all vps of customer DB0001
				'searchat' 			: 'DebtorCode',
				'searchfor' 		: 'DB0001'
}

response = api.sendRequest('vps', 'list', vpsParams)

print(response)
