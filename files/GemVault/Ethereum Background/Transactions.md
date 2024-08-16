A transaction is a cryptographically signed instruction from an account. An Ethereum transaction refers to an action that is initiated by an EOA. Ex: sending 1 ETH from A to B. This transaction changes the world state, and need to be broadcast to the entire network.

These transactions include the following information:

**from:** the address of the sender
**to:** the receiving address
**signature:** the identifier of the sender
**nonce:** the transaction number from the account
**value:** the value of transaction
**input data:** include arbitrary data
**gasLimit:** the maximum amount of gas that can be consumed by the transaction
**maxPriorityFeePerGas:** the maximum price of the consumed gas supplied to the validator as tip
**maxFeePerGas**: the maximum fee per unit of gas to be paid for the transaction

Gas refers to the computational power needed to process a transaction. The gasLimit and priority fee signify the amount of transaction fee paid to the validator.

A transaction will look like:

```
{ 
from: "0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8", 
to: "0xac03bb73b6a9e108530aff4df5077c2b3d481e5a", 
gasLimit: "21000", maxFeePerGas: "300", 
maxPriorityFeePerGas: "10", 
nonce: "0", 
value: "10000000000" 
}
```