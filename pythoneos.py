# /home/jaspreet/.local/lib/python3.6/site-packages
# # from eosapi import Client
# # from eosapi import HttpClient

# # # c = Client(nodes=['http://127.0.0.1:8888'])

# # # c.get_info()
# # # c.get_account('alice')

# # h = HttpClient(["https://jungle2.cryptolions.io:443"])

# # print(h.exec('chain', 'get_block', '{"block_num_or_id": 53686345}'))

# import requests

# url = "https://jungle2.cryptolions.io:443/v1/chain/get_table_rows"

# #payload = "{\"block_num_or_id\":\"500000\"}"

# payload = "{\"code\":\"zeptagram123\",\"table\":\"stat\",\"scope\":\"ZPT\",\"index_position\":\"primary\",\"json\":\"true\"}"

# headers = {
#     'accept': "application/json",
#     'content-type': "application/json"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)


# # headers = {
# #     'accept': "application/json",
# #     'content-type': "application/json"
# #     }

# # response = requests.request("POST", url, data=payload, headers=headers)

# # print(response.text)


# from eosjs_python import Eos


# key_pair = Eos.generate_key_pair()
# print(key_pair)

from eosjs_python import Eos

eos = Eos({
	'http_address': 'https://jungle2.cryptolions.io:443',
	'key_provider': '5KE2yA2iuQWrzzpSFt3VPCwdYZPrqse9k1z97Bpb5gz9gw1bMxD',
    'chain_id': '1eaa0824707c8c16bd25145493bf062aecddfeb56c736f6ba6397f3195f33c9f'
})   

#cleos push action eosio.token transfer '["eva","rider1","1 EVA","initial balance"]' -p eva

eos.push_transaction('zeptagram123','transfer','alicezepta12','active',{
	"from":"alicezepta12",
	"to":"bobzeptagram",
	"quantity":"0.0001 ZPT",
	"memo":""
})
