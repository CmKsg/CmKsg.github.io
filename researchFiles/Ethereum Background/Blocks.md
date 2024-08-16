Blocks are batches of transactions with a hash of the previous block in the chain. These hashes link blocks together cryptographically. This prevents fraud, as one change to a block would invalidate the whole blockchain.
![[Untitled.avif]]
Blocks are only created and committed into Ethereum once every 12 seconds.

To preserve the transaction history, blocks are ordered, and each block references it's parent block. Transactions within blocks are also strictly ordered. 

Once a block is put together by a randomly selected validator on the network, it is propagated to the rest of the network; all nodes add this block to the end of their blockchain, and a new validator is selected to create the next block. The exact block-assembly process and commitment/consensus process is currently specified by Ethereum’s “proof-of-stake” protocol.

Proof-of-stake:

* Validating nodes have to stake 32 ETH into a deposit contract as collateral against bad behaviour. 
* In every slot, a validator is randomly selected to be the new block proposer. They bundle transactions together, execute them and determine a new state.
* Other validators who hear about the new block re-execute the transactions to ensure they agree with the proposed change to the state. If the block is valid, they add it to their database.
* If a validator hears about two conflicting blocks for the same slot they use the fork-choice algorithm to pick the one supported by most ETH.

In a high-level, a block contains the following fields:

![[Pasted image 20240706174121.png]]

**Block time:** the amount of time separating blocks, in Ethereum this is divided into twelve second units. However, occasionally validators can be offline, meaning slots can go empty.

**Block size:** blocks themselves are bounded in size. Each block size has a target of 15 million gas but the size of blocks will increase or decrease in accordance with network demands, up until the block hits the limit of 30 million gas. This is important as it ensures blocks cannot be unnecessarily large. 