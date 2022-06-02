import BalanceRequests
import Bipwallet
import SeedSlova

seed = SeedSlova.seed()
#print(seed)
wallet = Bipwallet.address(seed)
BalanceRequests.ball(wallet)