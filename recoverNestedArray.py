from Crypto.Hash import keccak
from Crypto.Util.number import long_to_bytes
from eth_abi import encode

import requests
import argparse


def recoverArray(args):
	
	"""
    recoverArray query the elements of 2D array in a smart contract.

    :param args: Args supplied to the script
    :return: Returns an array of the supplied dimensions (lines * columns)
    """

	# Hashing slot 
	slot = long_to_bytes(args.slot)
	slot = bytes(32-len(slot)) + slot
	k = keccak.new(digest_bits=256)
	k.update(slot)
	slot = "0x"+k.hexdigest()
	
	target = args.target
	rpc = args.rpc
	lines = args.lines
	columns = args.columns
	
	array = [[0]*columns for _ in range(lines)]

	for i in range(lines):

		initialHash = int(slot, 16) + i
		k = keccak.new(digest_bits=256)
		k.update(bytes.fromhex(hex(initialHash)[2:]))
		Keccak_initialHash = "0x"+k.hexdigest()

		for j in range(columns):

			finalSlot = int(Keccak_initialHash, 16) + j
		
			r = requests.post(rpc, 
							  headers={'Content-Type': 'application/json'}, 
							  json={"method":"eth_getStorageAt",
								  "params":[target, hex(finalSlot), "latest"],
							      "id":1,
								  "jsonrpc":"2.0"
							  })
			
			val = int(r.json()['result'], 16)
			array[i][j] = val

	return array


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('--rpc', type=str, required=True, help="RPC URL")
	parser.add_argument('--target', type=str, required=True, help="Target contract address")
	parser.add_argument('--slot', type=int, required=True, help="Array storage slot")
	parser.add_argument('--lines', type=int, required=True, help="Number of lines in the array")
	parser.add_argument('--columns', type=int, required=True, help="Number of columns in the array")
	args = parser.parse_args()

	arr = recoverArray(args)

	print()
	for line in arr:
		print(line)

if __name__ == "__main__":
	main()	
