import hashlib
from hashlib import sha256
from bip32utils import Base58, BIP32Key

def pk_to_p2wpkh_as_p2sh_addr(pk_bytes, testnet=False):
    assert len(pk_bytes) == 33 and (pk_bytes.startswith(b"\x02") or pk_bytes.startswith(b"\x03")), \
        "Only compressed public keys are compatible with p2sh-p2wpkh addresses. " \
        "See https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki."
    pk_hash = hash160_bytes(pk_bytes)
    push_20 = bytes.fromhex("0014")
    script_sig = push_20 + pk_hash
    address_bytes = hash160_bytes(script_sig)
    prefix = b"\xc4" if testnet else b"\x05"
    address = Base58.check_encode(prefix + address_bytes)
    return address


def hash160_bytes(byte_input):
    return hashlib.new('ripemd160', sha256(byte_input).digest()).digest()

def derive_address(mpk, path = []):
    pub = BIP32Key.fromExtendedKey(mpk)
    for child_index in path:
        pub = pub.ChildKey(child_index)
    return pk_to_p2wpkh_as_p2sh_addr(pub.PublicKey())


