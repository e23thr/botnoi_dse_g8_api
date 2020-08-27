
# Sheet URL: https://docs.google.com/spreadsheets/d/1lZRtEqS_prvqsikCz5KSEsgT0e5tgVkd65wfB-R0QrA/edit?usp=sharing

import requests
response = requests.get(
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vSc5iYPbZvFAgwpLPhpRmbmJ75H-LQPbO831B_Z4dUf4V1tA3WBZUB-o4O8l655O0mOFWNKYa8qC-IM/pub?gid=0&single=true&output=csv')
assert response.status_code == 200, 'Wrong status code'
print(str(response.content))
f = open("templates/team-data.csv", "wb")
f.write(response.content)
f.close()
