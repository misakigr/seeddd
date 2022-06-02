from bipwallet.utils import *

def address(seed):

    # Наша seed фраза
    #seed = 'vivid area able second bicycle advance demand alpha flip stable drift route'

    # Мастер ключ из seed фразы
    master_key = HDPrivateKey.master_key_from_mnemonic(seed)

    # Public key из мастер ключа по пути 'm/44/0/0/0'
    root_keys = HDKey.from_path(master_key, "m/44'/0'/0'/0")[-1].public_key.to_b58check()

    # Extended public key
    xpublic_key = str(root_keys, encoding="utf-8")

    # Адрес дочернего кошелька в зависимости от значения index
    address = Wallet.deserialize(xpublic_key, network='BTC').get_child(0, is_prime=False).to_address()

    rootkeys_wif = HDKey.from_path(master_key, f"m/44'/0'/0'/0/{0}")[-1]

    # Extended private key
    xprivatekey = str(rootkeys_wif.to_b58check(), encoding="utf-8")

    # Wallet import format
    wif = Wallet.deserialize(xprivatekey, network='BTC').export_to_wif()
    print(str(wif, 'utf-8'))
    print(address)

    return address
if __name__ == '__main__':
    address('vivid area able second bicycle advance demand alpha flip stable drift route')