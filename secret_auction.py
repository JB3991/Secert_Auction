from replit import clear
from auction_art import logo

print(logo)
print("Welcome to the secert auction program")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  bid_amount = int(input("What's your bid?: $"))
  bids[name] = bid_amount
  other_bidders = input("Are there any other bidders? type 'yes' or 'no'.")
  if other_bidders == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif other_bidders == "yes":
    clear()