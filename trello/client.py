from rauth import OAuth1Service
import settings
import sys


class TrelloClient(object):
	
	def __init__(self, pin=None):

		self.trello_service = OAuth1Service(
			consumer_key	 = settings.KEY,
			consumer_secret = settings.SECRET,
			name = 'trello',
			authorize_url = settings.OAUTH_AUTHORIZE_URL,
			access_token_url = settings.OAUTH_ACCESS_TOKEN_URL,
			request_token_url = settings.OAUTH_REQUEST_TOKEN_URL,
			base_url = settings.OAUTH_BASE_URL)

		print 'Initializing Trello Client...'

		request_token, request_token_secret = self.trello_service.get_request_token()
		authorize_url = self.trello_service.get_authorize_url(request_token)

		if not pin:
			print 'Visit this URL in your browser: ' + authorize_url
			pin = raw_input('Enter PIN from browser: ')
		else:
			print 'Using pin:', pin

		self.session = self.trello_service.get_auth_session(request_token, 
										request_token_secret, 
										method='POST',
		                                data={'oauth_verifier': pin})

		self.access_token = self.session.access_token
		self.access_token_secret = self.session.access_token_secret

		print self.session.access_token, self.session.access_token_secret # Save this to database

def main():
	pin = None
	if sys.argv and len(sys.argv) > 1:
		pin = sys.argv[1]
	tc = TrelloClient(pin=pin)

if  __name__ =='__main__':
	main()

