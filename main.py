from algosdk import account, mnemonic

# Generate new Algorand account
private_key, address = account.generate_account()

print("Generated Algorand Account:")
print("Address:", address)
print("Private Key:", private_key)

# Convert private key to mnemonic
mnemo = mnemonic.from_private_key(private_key)
print("Mnemonic:", mnemo)
