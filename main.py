import requests, json
import subprocess
import sys

authorize_url = " https://gymkhana.iitb.ac.in/profiles/oauth/authorize/?client_id=SpB6ZZODGwfgYXnccf06EAICmFjMkwi51mLKqdmz&response_type=code&scope=basic profile picture sex ldap phone insti_address program secondary_emails&redirect_uri=https://insti.app&state=some_state"		#gymkhana url 
token_url = "https://gymkhana.iitb.ac.in/profiles/oauth/token/"			#gymkhana token url

#callback url specified when the application was defined
callback_uri = "http://localhost:8000"		#app url


# fields ---- first_name,last_name,type,profile_picture,sex,username,email,program,contacts,insti_address,secondary_emails,mobile,roll_number
test_api_url = "https://gymkhana.iitb.ac.in/profiles/user/api/user/?fields=first_name,last_name,type,profile_picture,sex,username,email,program,contacts,insti_address,secondary_emails,mobile,roll_number"		#gymkhana api url


client_id = 'SpB6ZZODGwfgYXnccf06EAICmFjMkwi51mLKqdmz'
client_secret = 'Nzj4Qk3nXolzeOEViTWRv4YobNvgqnB4rUiulLXBKI6WPih99PJE3qDpWhKxbvMHato4yLEfmatGE03QHResYTpUeF1txlW9ncpc4c0POoOiJEPzsyBHyQIWCOmA3fgO'

#step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
# prompted for credentials.

# authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=openid'


authorization_code = input('code: ')			#auth_code client recieved from sso site

#turn the authorization code into a access token 
#authorization_code is short lived
#access_token for about 10 hours		(enough for us)
#refresh_token for long time and can be refreshed
data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}

access_token_response = requests.post(token_url, data=data, allow_redirects=False, auth=(client_id, client_secret))	#to get access_token
print(access_token_response.text)

# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
access_token = tokens['access_token']			#extract access token from json

#To make calls for api backend
api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(test_api_url, headers=api_call_headers)

print(api_call_response.text)