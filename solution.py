#!/usr/bin/python
import hashlib
import binascii
import base58
import os
from bit import Key
from bit.format import bytes_to_wif

TARGET_WALLET = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"
PRIME = 957496696762772407663

class UtilHash():
    def __init__(self):
        print("Lets go..")

    def to_hex(self, number):
        return hex(number).lstrip("0x").rstrip("L")

    def compressed_private_key_from_string(self, string):
        return Key.from_hex(hashlib.sha256(string.encode()).hexdigest())
    
    def uncompressed_private_key_from_string(self, string):
        return Key(bytes_to_wif(self.compressed_private_key_from_string(string).to_bytes(), compressed=False))

    def compressed_private_key_from_hex(self, hex_number):
        return Key.from_hex(hex_number)

    def uncompressed_private_key_from_hex(self, hex_number):
        return Key(bytes_to_wif(self.compressed_private_key_from_hex(hex_number).to_bytes(), compressed=False))

    def char_encoding_ascii(self, c):
        return ord(c)

    def ascii_word(self, word):
        sum = 0
        for c in word:
            sum += self.char_encoding_ascii(c)
        return sum
    
    def char_encoding_alpha(self, c):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        return alphabet.find(c.lower()) + 1

    def alpha_word(self, word):
        sum = 0
        for c in word:
            sum += self.char_encoding_alpha(c)
        return sum

    def is_hex_number(self, hex_number):
        return self.uncompressed_private_key_from_hex(hex_number).address == TARGET_WALLET or self.compressed_private_key_from_hex(hex_number).address == TARGET_WALLET


        
if __name__=='__main__':
    xrp_list = ["xrp, XRP", "ripple", "Ripple", "RIPPLE", None]
    eth_list = ["eth, ETH", "ethereum", "Ethereum", "ETHEREUM", "ETHER", None]
    btc_list = ["btc", "BTC", "bitcoin", "Bitcoin", "BITCOIN", None]
    dorian_list = ["dorian", "Dorian", "DORIAN", None]
    satoshi_list = ["satoshi", "Satoshi", "SATOSHI", None]
    nakamoto_list = ["nakamoto", "Nakamoto", "NAKAMOTO", None]
    phemex_list = ["phemex", "Phemex", "PHEMEX", None]
    hair_list = ["hair", "Hair", "HAIR", None]
    neck_list = ["neck", "Neck", "NECK", None]
    jaw_list = ["jaw", "Jaw", "JAW", None]
    prime_list = [PRIME, None]


    tool = UtilHash()

    for xrp in xrp_list:
        for eth in eth_list:
            for btc in btc_list:
                for dorian in dorian_list:
                    for satoshi in satoshi_list:
                        for nakamoto in nakamoto_list:
                            for phemex in phemex_list:
                                for prime in prime_list:
                                    for hair in hair_list:
                                        for jaw in jaw_list:
                                            for neck in neck_list:
                                                words = [xrp, eth, btc, dorian, satoshi, nakamoto, phemex, prime, hair, jaw, neck]
                                                ascii_word_number = 0
                                                alpha_word_number = 0
                                                for word in words:
                                                    if word == PRIME:
                                                        ascii_word_number += word
                                                        alpha_word_number += word
                                                    elif word != None:
                                                        ascii_word_number += tool.ascii_word(word)
                                                        alpha_word_number += tool.alpha_word(word)
                                                if ascii_word_number == 0:
                                                    next
                                                hex_ascii_word_number = tool.to_hex(ascii_word_number)
                                                hex_alpha_word_number = tool.to_hex(alpha_word_number)
                                                if tool.is_hex_number(hex_ascii_word_number) or tool.is_hex_number(hex_alpha_word_number):
                                                    print("EUREKA!")
                                                    print(words)
