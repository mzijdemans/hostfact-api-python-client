from hostfact_api import HostFactAPI

api = HostFactAPI()

debtorParams = {
	'Identifier'	: 1, # Debtor ID
	'Message' : 'test',
	#'Recipient' : '', # By default debtor e-mailaddress
	'TemplateID'	: 5, # E-mailtemplate ID
	#'References' : {'invoice' : 1, 'domain' : 1}, # Dict with references, for filling variables
}

response = api.sendRequest('debtor', 'sendemail', debtorParams)

print(response)