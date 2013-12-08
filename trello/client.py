from rauth import OAuth1Service
import settings
import json
import sys


class TrelloClient(object):
	
	def __init__(self, pin=None):
		# do OAuth stuff
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

		print 'Connected to Trello!'

	@classmethod
	def get_api_url(cls, api_url):
		return '{}{}'.format(settings.OAUTH_BASE_URL, api_url)

	def get_lists(self, board_id):
		api_url = TrelloClient.get_api_url('boards/{}/lists'.format(board_id))
		return self.session.get(api_url, params={}).json()

	def get_cards(self, board_id):
		api_url = TrelloClient.get_api_url('boards/{}/cards'.format(board_id))
		return self.session.get(api_url, params={}).json()

	def visit_cards(self, visitor, board_id):
		cards = self.get_cards(board_id)
		for c in cards:
			visitor.visit(c)




