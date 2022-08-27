#!/usr/bin/python3
""" command line tool to run the app"""

from cmd import Cmd
import shlex
from core.nft import *
import time
import json


class App(Cmd):
    """Simple command processor for thentic app."""

    prompt: str = "[THENTIC-Console]$ "

    def do_help(self, arg):
        """ shows help """
        return super().do_help(arg)

    def do_EOF(self, line):
        """exit on Ctrl+D"""
        return True

    def do_exit(self, line):
        """exit the console"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create_nft_contract(self, args):
        """creates a new NFT smart contract"""
        args = self._key_value_parser(args.split())
        print(create_nft())

    def do_get_contract_address(self, args):
        """gets the NFT contract address"""
        args = self._key_value_parser(args.split())
        print("NFT contract address: {}".format(get_contract_address()))

    def do_mint_nft(self, args):
        """mints a new NFT"""
        args = self._key_value_parser(args.split())
        print("enter your wallet address")
        owner_address = str(input())
        id = int(time.time())
        data = {
            "car": "BMW",
            "model": "M3",
            "year": 2019,
            "color": "red",
            "price": 10000,
            "first_circulation": "2021-01-01",
            "owner": owner_address,
            "status": "new"
        }
        json_data = json.dumps(data)
        print(mint_nft(id, owner_address, json_data))

    def do_transfer_nft(self, args):
        """transfers an NFT"""
        args = self._key_value_parser(args.split())
        print("enter your wallet address")
        owner_address = input()
        print("enter the new owner's wallet address")
        new_owner_address = input()
        print("enter the NFT id")
        id = int(input())
        print(transfer_nft(id, owner_address, new_owner_address))

    def do_get_nfts(self, args):
        """gets all NFTs"""
        args = self._key_value_parser(args.split())
        print(get_nfts())

    
    def do_create_invoice(self, args):
        """creates an invoice"""
        args = self._key_value_parser(args.split())
        print("enter the admin address")
        owner_address = input()
        print(create_invoice(owner_address))


    def do_get_invoices(self, args):
        """gets all invoices"""
        args = self._key_value_parser(args.split())
        print(get_invoices())


    def do_delete_invoice(self, args):
        """deletes an invoice"""
        args = self._key_value_parser(args.split())
        print("please enter the invoice id")
        id = int(input())
        print(cancel_invoice(id))


if __name__ == '__main__':
    App().cmdloop()
