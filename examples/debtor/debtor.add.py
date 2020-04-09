from hostfact_api import HostFactAPI

api = HostFactAPI()

debtorParams = {
    # 'DebtorCode': 'DB0001', # Custom customer number
    'CompanyName': 'Company X',
    'CompanyNumber': '123456789',
    'TaxNumber': 'NL123456789B01',
    'Sex': 'm',
    'Initials': 'John',
    'SurName': 'Jackson',
    'Address': 'Keizersgracht 100',
    'ZipCode': '1015 AA',
    'City': 'Amsterdam',
    'Country': 'NL',
    'EmailAddress': 'info@company.com',
    'PhoneNumber': '010 - 22 33 44',
    'AccountNumber': 'NL59RABO0123123123',
    'AccountBIC': 'RABONL2U',
    'AccountName': 'Company X',
    'AccountBank': 'Rabobank',
    'AccountCity': 'Amsterdam',
    'Groups': ['4']
}

response = api.sendRequest('debtor', 'add', debtorParams)

print(response)
