from rauth import OAuth1Service
import settings
"""
https://trello.com/1/OAuthGetRequestToken
https://trello.com/1/OAuthAuthorizeToken
https://trello.com/1/OAuthGetAccessToken
"""

ts = OAuth1Service(
	consumer_key	 = settings.KEY,
	consumer_secret = settings.SECRET,
	name = 'trello',
	authorize_url = settings.OAUTH_AUTHORIZE_URL,
	access_token_url = settings.OAUTH_ACCESS_TOKEN_URL,
	request_token_url = settings.OAUTH_REQUEST_TOKEN_URL,
	base_url = settings.OAUTH_BASE_URL)

print ts
request_token, request_token_secret = ts.get_request_token()
authorize_url = ts.get_authorize_url(request_token)

print request_token, request_token_secret, authorize_url


print 'Visit this URL in your browser: ' + authorize_url
pin = raw_input('Enter PIN from browser: ')

session = ts.get_auth_session(request_token, 
								request_token_secret, 
								method='POST',
                                data={'oauth_verifier': pin})

print session.access_token, session.access_token_secret # Save this to database

