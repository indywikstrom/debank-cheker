headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'origin': 'https://portfolio.metamask.io',
    'referer': 'https://portfolio.metamask.io/',
    'user-agent': 'ТВОЙ UA',
}

result = []

url = f'https://account.metafi.codefi.network/accounts/{address}?chainId=1&includePrices=true'
response = requests.get(url=url, headers=headers)
result.append(response.json())

with open("test.json", "w") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
