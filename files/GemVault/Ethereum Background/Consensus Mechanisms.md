==**Proof of Work:**==

Ethereum began with a proof-of-work consensus mechanism (well known to also be Bitcoin's mechanism). This allowed nodes to agree on the state of all information recorded on the blockchain and prevented economic attacks. 

*"The proof-of-work protocol, Ethash, required miners to go through an intense race of trial and error to find the nonce for a block. Only blocks with a valid nonce could be added to the chain.*

*When racing to create a block, a miner repeatedly put a dataset, that could only be obtained by downloading and running the full chain (as a miner does), through a mathematical function. The dataset was used to generate a mixHash below a target that is dictated by the block difficulty. The best way to do this is through trial and error.*

*The difficulty determined the target for the hash. The lower the target, the smaller the set of valid hashes. Once generated, this was incredibly easy for other miners and clients to verify. Even if one transaction were to change, the hash would be completely different, signalling fraud.*

*Hashing makes fraud easy to spot. But proof-of-work as a process was also a big deterrent to attacking the chain."*

The objective of PoW was to extend the chain. The longest chain was the most believable one, as it had the most computational work done to achieve it. Within Ethereum's PoW system, it was impossible to create new blocks that erased transactions or maintained a second chain. That's because a malicious miner would have to solve the block nonce faster than everyone else on the chain. This would require a malicious miner to own 51% of the chain's mining power, which would be extremely costly and difficult to maintain.

Proof of work also produced Ethereum, with miners gaining 2 ETH for mining a block.

**Finality:** a transaction has finality when it is part of a block that cannot change. Due to decentralized mining, it was possible for two valid blocks to be mined at the same time. This would create a temporary fork, solved by one chain becoming longer and thus accepted (when people added blocks to the chain).

Transactions rejected on the temporary fork may not have been included in the accepted chain. This means it could get reversed. So **finality** refers to the time you should wait before considering a transaction irreversible. The more blocks that were mined meant a higher confidence in a transaction being final, meaning a probabilistic association was created with it.

**==Proof of Stake:==**

Proof of stake works purely off of validators, who check for the validity of new blocks propagated into the blockchain, and occasionally create and propagate their own blocks. If they try to defraud, their ETH will be destroyed (32 ETH).

To participate as a validator, a user must deposit 32 ETH into the deposit contract and run the execution, consensus and validator clients. On depositing their ETH, the user joins an activation queue that limits the rate of validator joining the network. 

Once active, validators receive new blocks from peers on the Ethereum network. The transactions delivered in the block are re-executed to check if the proposed changes to the state is valid. The validator then sends an attestation in favor of the block across the network.

**How Transactions Work in PoS:**

The following provides an end-to-end explanation of how a transaction gets executed in Ethereum proof-of-stake.

1) A user creates and signs a transaction with their private key. 
2) The transaction is submitted to an Ethereum execution client, verifying it's validity. 
3) If the transaction is valid, the client adds it to the local mempool and broadcasts it to other nodes over the execution layer gossip network. When other nodes hear, they add it to their mempool.
4) One of the nodes in the network is the block proposer for the current slot. This node is responsible for building and broadcasting the next block to be added to the Ethereum blockchain.
	*"The execution client bundles transactions from the local mempool into an "execution payload" and executes them locally to generate a state change. This information is passed to the consensus client where the execution payload is wrapped as part of a "beacon block" that also contains information about rewards, penalties, slashings, attestations etc. that enable the network to agree on the sequence of blocks at the head of the chain."*
5) Other nodes receive the new beacon block on the consensus layer gossip network. They pass it to their execution client where the transactions are re-executed to ensure validity. 
6) The transaction can be considered finalized if it has become part of a chain with a supermajority link between two checkpoints. Checkpoints occur at the start of each epoch and they exist to account for the fact that only a subset of active validators attest in each slot, but all active validators attest across each epoch.

**Finality:**
A transaction has finality in distributed networks, when it is part of a block that can't change without a large amount of ETH being burned. On PoS, this is managed using "checkpoint" blocks. The first block in each epoch is a checkpoint. Validators vote for pairs of checkpoints that it considers to be valid. If a pair of checkpoints attracts votes representing at least two-thirds of the total staked ETH, the checkpoints are upgraded. The more recent of the two (target) becomes "justified". The earlier of the two is already justified because it was the "target" in the previous epoch. Now it is upgraded to "finalized".

**Fork Choice:**

When the network performs optimally and honestly, there is only ever one new block at the head of the chain, and all validators attest to it. However, it is possible for validators to have different views of the head of the chain due to network latency or because a block proposer has equivocated. Therefore, consensus clients require an algorithm to decide which one to favor.

**==Proof of Authority:==**

Proof of authority is a modified version of PoS, that is a reputation based algorithm. In the genesis block, a set of authorized signers are trusted. All authorized signers maintain equal power and privileges when determining consensus. They are selected based on their reputation, and are the only ones allowed to create new blocks. The reputation is human based, rather than algorithm based. 
