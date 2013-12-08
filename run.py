# run.py
from trello.scrum.burndown import BurndownBoard
import sys

def main():	
	pin = None
	if sys.argv and len(sys.argv) > 1:
		pin = sys.argv[1]

	bb = BurndownBoard('nZC92spt', pin=pin)
	print bb.get_burndown_totals()
	
if __name__ =='__main__':
	main()
