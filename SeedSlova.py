from bipwallet import wallet

def seed():
    # generate 12 word mnemonic seed
    seed = wallet.generate_mnemonic()
    return seed
print(seed())
if __name__ == '__main__':
    print(seed())