# Introduction

I did not find a simple tool for generating Segwit P2WPKH
over P2SH addresses from a master public key that is similar to
[addrgen](https://github.com/prusnak/addrgen).

This is my implementation in Python, it is not lightweight as it
uses several other libraries, but it works. Pull requests to get
rid of dependencies are welcome.

# Dependencies

If you want to be able to handle ypub keys, install my fork of
bip32utils, otherwise you can just install the official version.

```bash
pip3 install git+https://github.com/jooray/bip32utils --upgrade
```

# Usage

```python
master_public_key='ypub6X3jfYGmBWr9oXXNfiJP13ydsSKjVWS1929vx6RAJdsFYMCZJeNrNf2tfEmNKkQ81xwD1E1xQZxrUWvgLousBuc3aec5YgDRrFfzBAP1VtN' # this can be xpub or ypub mpk
address = derive_address(master_public_key, [0, 2]) # go for ./0/2 key derivation path
print(address) # 38o7aArrsNZoZT4iXGrFrhxAKjfiRp8QX3
```
