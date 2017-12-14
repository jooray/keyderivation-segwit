# Introduction

I did not find a simple tool for generating Segwit P2WPKH
over P2SH addresses from a master public key that is similar to
[addrgen](https://github.com/prusnak/addrgen).

This is my implementation in Python, it is not lightweight as it
uses [my fork of bip32utils](https://github.com/jooray/bip32utils),
but it works. Pull requests to get rid of dependencies are welcome.

# Dependencies

Install my fork of bip32utils:

```bash
pip3 install git+https://github.com/jooray/bip32utils --upgrade
```

# Usage

For usage example see addrgen.py

