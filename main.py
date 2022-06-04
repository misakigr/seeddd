import SeedSlova
import Bipwallet
import BalanceRequests

seed = SeedSlova.seed()
#print(seed)
wallet = Bipwallet.address(seed)
BalanceRequests.ball(wallet)