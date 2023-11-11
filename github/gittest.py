# import json
# import requests

# GITHUB_KEY = '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'

# PAYLOAD = {
#     'name': 'api_test1',
#     'public': 'true'
# }

# res = requests.get(
#     'https://api.github.com/user/repos',
#     headers={'Authorization': f'token {GITHUB_KEY}'},
#     data=json.dumps(PAYLOAD)
# )

# print(res.json()[0]['url'])
