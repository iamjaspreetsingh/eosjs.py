# /home/jaspreet/.local/lib/python3.6/site-packages
# Reference:https://github.com/EvaCoop/eosjs_python

import requests
import json

#payload = "{\"block_num_or_id\":\"500000\"}"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

def get_table(contractName,tableName,scope):
	url = "https://jungle2.cryptolions.io:443/v1/chain/get_table_rows"
	payload = "{\"code\":\""+contractName+"\",\"table\":\""+tableName+"\",\"scope\":\""+scope+"\",\"index_position\":\"primary\",\"json\":\"true\"}"
	response = requests.request("POST", url, data=payload, headers=headers)
	return response.text	

def get_accPublickey(_accname):
	url = "http://jungle.eoscafeblock.com:8888/v1/chain/get_account"
	payload = "{\"account_name\":\""+_accname+"\"}"
	response = requests.request("POST", url, data=payload, headers=headers)
	pub = json.loads(response.text)
	return pub['permissions'][1]['required_auth']['keys'][0]['key']

from eosjs_python import Eos

aliceeos = Eos({
	'http_address': 'https://jungle2.cryptolions.io:443',
	'key_provider': '5KE2yA2iuQWrzzpSFt3VPCwdYZPrqse9k1z97Bpb5gz9gw1bMxD',
    'chain_id': '1eaa0824707c8c16bd25145493bf062aecddfeb56c736f6ba6397f3195f33c9f'
})   


bobeos = Eos({
	'http_address': 'https://jungle2.cryptolions.io:443',
	'key_provider': '5KcMt7aEEy766dftpaQfTUTHskpQ4iPy2EaGBJuLEhwfQEhaGtV',
    'chain_id': '1eaa0824707c8c16bd25145493bf062aecddfeb56c736f6ba6397f3195f33c9f'
})   

signedin=False
signinacc = bobeos # let bobeos be liquid acc
signedinaccName = 'bobzeptagram'


def transferVID(_from,_to,_quantity,signer):
  signer.push_transaction('zeptagram123','transfer',_from,'active',{
	"from":_from,
	"to":_to,
	"quantity":_quantity,
	"memo":""})

# result = get_table("zeptagram123","stat","ZPT")
# print(result)

# transferVID("alicezepta12","bobzeptagram","0.0001 ZPT",aliceeos)


# key_pair = Eos.generate_key_pair()


def createacct(_name):
	key_pair = Eos.generate_key_pair()
	aliceeos.newaccount({
		'creator': 'alicezepta12',
		'name': _name,
		'owner_public_key': key_pair["public"],
		'active_public_key': key_pair["public"],
		'buyrambytes_bytes': 2000,
		'delegatebw_stake_net_quantity': '1.0000 EOS',
		'delegatebw_stake_cpu_quantity': '1.0000 EOS',
		'delegatebw_transfer': 0
	})
	return key_pair

def signin(_name,_pk):
	signineos = Eos({
		'http_address': 'https://jungle2.cryptolions.io:443',
		'key_provider': _pk,
		'chain_id': '1eaa0824707c8c16bd25145493bf062aecddfeb56c736f6ba6397f3195f33c9f'
	})
	global signedin,signedinaccName
	signedin=True
	signedinaccName=_name
	global signinacc 
	signinacc=signineos



# nk=createacct("alicetesting")	
# print(nk)

signin("alicetesting","5JCUiyyjjaGxWoNNyAnPYA6FTmAqEjSs9Jw5dkXpPMkTpaZzhvA")

info = get_accPublickey(signedinaccName)
print(info)