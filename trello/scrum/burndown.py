# aggregator.py
from trello.client import TrelloClient
import re

class BurndownBoard(TrelloClient):

	def __init__(self, board_id, pin=None):
		self.board_id = board_id
		self.pin = pin

	def get_burndown_totals(self):
		tc = TrelloClient(pin=self.pin)
		visitor = CardVisitor()
		tc.visit_cards(visitor, self.board_id)
		return visitor.get_totals()


class CardVisitor(object):

	def __init__(self):
		self.estimated = 0 
		self.actual = 0

	def visit(self, card):
		est, act = self.parse_counts(card['name'])
		self.estimated += est
		self.actual += act

	def parse_counts(self, name):
		# pattern finds (#/#) in the beginning of card titles
		pattern = r'^\((.*)/(.*)\) '
		matched = re.search(pattern, name, re.I)
		if matched and len(matched.groups()) > 0:
			try:
				est, act = matched.group(1).strip(), matched.group(2).strip()
				# if no estimate, probably unplanned spike, use actual value as estimate
				if est == '':
					est = act
				return float(est), float(act)
			except:
				print 'could not parse: {}'.format(name)
		return (0, 0)

	def get_totals(self):
		return dict(estimated=self.estimated, actual=self.actual)
