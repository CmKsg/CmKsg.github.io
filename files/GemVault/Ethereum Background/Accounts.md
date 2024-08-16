**EOA (Externally Owned Account)**: someone's account, which they access the blockchain with
- Costs nothing to create
- Can initiate transactions
- Made up of public and private keys
- Transactions can only be ETH/token transactions
**Contract account**: smart contracts deployed to the network
- Creating a contract requires payment as you're using up the network
- Can only send transaction when receiving a transaction
- Transactions from an external account to a contract account can trigger code which can execute different actions
- Do not have private keys, instead purely controlled by logic

**==Fields==**:
![[Pasted image 20240705180158.png]]
**nonce**: a counter indicating the number of transactions sent from an EOA or the number of contracts created by a contract. Only one transaction with a ] nonce can be executed, protecting against replay attacks where signed transactions are repeatedly broadcast and re-executed.

**balance**: number of wei owned by account.

**codeHash**: the code of the account in the EVM. Contract accounts have code fragments that are programmed in to perform different operations. The EVM code gets executed if a message comes to the account. Code Hash cannot be changed or manipulated. All code fragments are contained in the state database under their corresponding hashes. For EOAs, the codeHash is empty.

**storageRoot**: a 256-bit hash that denotes the storage contents of an account. Empty by default.

