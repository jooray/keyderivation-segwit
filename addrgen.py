from bip32utils import Base58, BIP32Key

def derive_address(mpk, path = []):
    pub = BIP32Key.fromExtendedKey(mpk)
    for child_index in path:
        pub = pub.ChildKey(child_index)
    return pub.P2WPKHoP2SHAddress()

master_public_key='ypub6X3jfYGmBWr9oXXNfiJP13ydsSKjVWS1929vx6RAJdsFYMCZJeNrNf2tfEmNKkQ81xwD1E1xQZxrUWvgLousBuc3aec5YgDRrFfzBAP1VtN' # this can be xpub or ypub mpk
address = derive_address(master_public_key, [0, 2]) # go for ./0/2 key derivation path
print(address) # 38o7aArrsNZoZT4iXGrFrhxAKjfiRp8QX3

