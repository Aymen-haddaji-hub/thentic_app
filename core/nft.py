import requests
import json


def create_nft():
    """
    create new NFT contract using THENTIC API"""
    url = 'https://thentic.tech/api/nfts/contract'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'aBcmbYFXLtuTjuwxEOSCN7IjjT19VPwG',
            'chain_id': '3',
            'name': 'CarPasport', 
            'short_name': 'CarPsp'}

    #creates NFT contract on BNB testnet
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        return 'NFT contract created - please sign the transaction in the following url:{}'.format(r.json()['transaction_url'])
    else:
        return 'Error creating NFT contract'


def mint_nft(nft_id, owner_address, data):
    """
    mint new NFT using THENTIC API"""
    url = 'https://thentic.tech/api/nfts/mint'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'aBcmbYFXLtuTjuwxEOSCN7IjjT19VPwG',
            'chain_id': '3',
            'nft_id': nft_id,
            'tot': owner_address,
            'contract': str(get_contract_address()),
            'nft_data': data}

    #mint NFT on BNB testnet
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        return 'NFT minted - please sign the transaction in the following url:{}'.format(r.json()['transaction_url'])
    else:
        return 'Error minting NFT'


def transfer_nft(nft_id, owner_address, new_owner_address):
    """
    transfer NFT using THENTIC API"""
    url = 'https://thentic.tech/api/nfts/transfer'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'aBcmbYFXLtuTjuwxEOSCN7IjjT19VPwG',
            'chain_id': '3',
            'nft_id': nft_id,
            'contract': get_contract_address(),
            'from': owner_address,
            'to': new_owner_address}

    #transfer NFT on BNB testnet
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        return 'NFT transferred - please sign the transaction in the following url:{}'.format(r.json()['transaction_url'])
    else:
        return 'Error transferring NFT'


def get_contract_address():
    """
    get NFT contract address using THENTIC API"""
    url = 'https://thentic.tech/api/contracts'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'aBcmbYFXLtuTjuwxEOSCN7IjjT19VPwG',
            'chain_id': '3'}

    r = requests.get(url, json=data, headers=headers)
    if r.status_code == 200:
        return r.json()['contracts'][0]['contract']
    else:
        return 'Error getting NFT contract address'


def get_nfts():
    """
    get NFTs using THENTIC API"""
    url = 'https://thentic.tech/api/nfts'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'aBcmbYFXLtuTjuwxEOSCN7IjjT19VPwG',
            'chain_id': '3'}

    r = requests.get(url, json=data, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        return 'Error getting NFTs'

def create_invoice(owner_address):
    """
    create invoice for NFT using THENTIC API"""
    url = 'https://thentic.tech/api/invoices/new'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'aBcmbYFXLtuTjuwxEOSCN7IjjT19VPwG',
            'chain_id': '3',
            'amount': '0.01',
            'to': owner_address
    }

    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        id = r.json()['request_id']
        return 'Invoice created - please sign the transaction in the following url:{}'.format(r.json()['transaction_url'],
                                                                                               id)  # returns invoice id
    else:
        return 'Error creating invoice'


def cancel_invoice(request_id):
    """
    cancel invoice for NFT using THENTIC API"""
    url = 'https://thentic.tech/api/invoices/cancel'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'aBcmbYFXLtuTjuwxEOSCN7IjjT19VPwG',
            'chain_id': '3',
            'request_id': request_id
    }

    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        return 'Invoice canceled - please sign the transaction in the following url:{}'.format(r.json()['transaction_url'])
    else:
        return 'Error canceling invoice'


def get_invoices():
    """
    get invoice for NFT using THENTIC API"""
    url = 'https://thentic.tech/api/invoices/all'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'aBcmbYFXLtuTjuwxEOSCN7IjjT19VPwG',
            'chain_id': '3'
    }

    r = requests.get(url, json=data, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        return 'Error getting invoice'
