bid_dict = {}
bidder_flag = True
while bidder_flag:
  name= input("What is your name? ")
  bid= input("What is your bid? $")
  bid_dict[name] = bid

  maximum = max(bid_dict, key=bid_dict.get)

  
  restart = input("Are there any other bidders? [y/n] ")
  clear()
  if restart == "n":
    bidder_flag = False
    print(f"{maximum} won the auction with ${ bid_dict[maximum]}.")
   
