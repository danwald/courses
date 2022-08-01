import unittest

from cryptopals import hex2base64


class TestCypropals(unittest.TestCase):
    def test_hex2base64(self):
        ''' test case from https://cryptopals.com/sets/1/challenges/1'''
        INPUT = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        OUTPUT = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEquals(hex2base64(INPUT), OUTPUT)
