import requests, json
import subprocess
import sys

authorize_url = ""		#gymkhana url 
token_url = ""			#gymkhana token url

#callback url specified when the application was defined
callback_uri = ""		#app url

test_api_url = ""		#gymkhana api url


client_id = '<<your client_id goes here>>'
client_secret = '<<your client_secret goes here>>'

#step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
# prompted for credentials.

authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=openid'


authorization_code = ""			#auth_code client recieved from sso site

#turn the authorization code into a access token 
#authorization_code is short lived
#access_token for about 10 hours		(enough for us)
#refresh_token for long time and can be refreshed
data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}

access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))	#to get access_token


# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
access_token = tokens['access_token']			#extract access token from json

#To make calls for api backend
api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)
