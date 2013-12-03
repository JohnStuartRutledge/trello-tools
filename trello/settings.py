KEY = '04e60231a12bd917801238f0edc14aab'
SECRET = 'd3a0c48c7270b30e0063ca3d01c634758a9084594c13e86d0077083615382317'
APP_NAME = 'Pills+Trello+Tools'
TOKEN_REQUEST_URL = 'https://trello.com/1/authorize?key={}&name={}&expiration=30days&response_type=token'.format(KEY, APP_NAME)
OAUTH_AUTHORIZE_URL = 'https://trello.com/1/OAuthAuthorizeToken'
OAUTH_ACCESS_TOKEN_URL = 'https://trello.com/1/OAuthGetAccessToken'
OAUTH_REQUEST_TOKEN_URL = 'https://trello.com/1/OAuthGetRequestToken'
OAUTH_BASE_URL = 'https://trello.com/1/'