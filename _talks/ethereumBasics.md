---
title: "Ethereum Background"
collection: talks
type: "Tutorial"
permalink: /research/2013-03-01-tutorial-1
date: 2013-03-01
---

# Blockchain

Blockchain: is a public database that is updated and shared across multiple computers across one network.

Block: in this public database is the data and the state that's being stored. When transactions are done (for example, you send 1 ETH to someone), a new block has to be added to the blockchain recording that transaction and the state of the system.

Chain: refers to the immutability aspect of these blocks, each block references all of the blocks before it (parents), and thus you cannot change the data within a block without changing all of the preceding ones.

# Blocks

Blocks are batches of transactions with a hash of the previous block in the chain. These hashes link blocks together cryptographically. This prevents fraud, as one change to a block would invalidate the whole blockchain. ![[Untitled.avif]] Blocks are only created and committed into Ethereum once every 12 seconds.

To preserve the transaction history, blocks are ordered, and each block references it's parent block. Transactions within blocks are also strictly ordered.

Once a block is put together by a randomly selected validator on the network, it is propagated to the rest of the network; all nodes add this block to the end of their blockchain, and a new validator is selected to create the next block. The exact block-assembly process and commitment/consensus process is currently specified by Ethereum’s “proof-of-stake” protocol.

Proof-of-stake:

    Validating nodes have to stake 32 ETH into a deposit contract as collateral against bad behaviour.
    In every slot, a validator is randomly selected to be the new block proposer. They bundle transactions together, execute them and determine a new state.
    Other validators who hear about the new block re-execute the transactions to ensure they agree with the proposed change to the state. If the block is valid, they add it to their database.
    If a validator hears about two conflicting blocks for the same slot they use the fork-choice algorithm to pick the one supported by most ETH.

In a high-level, a block contains the following fields:

![[Pasted image 20240706174121.png]]

Block time: the amount of time separating blocks, in Ethereum this is divided into twelve second units. However, occasionally validators can be offline, meaning slots can go empty.

Block size: blocks themselves are bounded in size. Each block size has a target of 15 million gas but the size of blocks will increase or decrease in accordance with network demands, up until the block hits the limit of 30 million gas. This is important as it ensures blocks cannot be unnecessarily large.

# Accounts

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

# EVM

Blockchain is usually described with the analogy of "distributed ledger". This ledger maintains a record of the activity which adheres to a set of rules based on what someone can and cannot do to the ledger. For example, someone cannot receive more ETH than they send. 

While Ethereum has ETH, it's own currency, it has something much more powerful: smart contracts. Instead of a distributed ledger, as Bitcoin tends to be described, Ethereum is more like a state machine, which is a large data structure that not only holds all accounts and balances, but is also a machine state, which can change block to block according to a set of rules. 

**State:** the state is an enormous data structure, which keeps all accounts linked by hashes and reducible to a single root hash stored on the blockchain.

**EVM Instructions:** executes as a stack machine, with a depth of 1024 items. Each item is a 256-bit hash word. During execution, the EVM maintains a transient memory, which does not persist between transactions. 

Contracts, however, do contain a Merkle Patricia _storage_ trie (as a word-addressable word array), associated with the account in question and part of the global state.

"Compiled smart contract bytecode executes as a number of EVM [opcodes](https://ethereum.org/en/developers/docs/evm/opcodes/), which perform standard stack operations like `XOR`, `AND`, `ADD`, `SUB`, etc. The EVM also implements a number of blockchain-specific stack operations, such as `ADDRESS`, `BALANCE`, `BLOCKHASH`, etc."

![[Untitled 1.avif]]

# Ether

**Ether** (**ETH**): Cryptocurrency of Ethereum. The purpose of ETH is to allow for market computation. This market provides an economic incentive for participants to provide computational power to the network. 

Any participant who broadcasts a transaction request in the network must provide some ETH as payment. The network then awards the bounty to whoever does the work of verifying, executing and committing the transaction to the blockchain, followed by broadcasting it to the network. 

The amount of ETH that is paid by the participant corresponds to the computational resources required to complete the transaction, and is usually denoted as Gas. Gas prevents malicious actors from clogging the network, as there is a monetary cost to it.

Finally, ETH is used to provide crypto-economic security to the network in three ways:
1) It rewards validators who propose blocks or call out dishonest behaviour from other validators
2) It is staked by validators, who put it as collateral to not misbehave (lest it be destroyed)
3) It is used to weigh votes for newly proposed blocks

# Networks

**Public Networks:** accessible to anyone with an internet connection. 

An example is the Ethereum Mainnet, which is the primary public Ethereum production blockchain, where transactions occur on the distributed ledger. This is what people discuss when discussing Ether or Ethereum generally.

In addition to the Mainnet, there are testnets (public). These are networks used by protocol and smart contract developers to test implementation in a production-like environment before deployment to the Mainnet. 

The two types are: **Sepolia (recommended)**, **Goerli (long-term support)**

# Transactions

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

# Web2 vs. Web3

![[Pasted image 20240705170036.png]]
![[Pasted image 20240705170132.png]]

# Consensus Mechanisms

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

# dapps

**dapps**: a dapp is an application built on a decentralized network that uses back-end smart contracts and front-end interfaces. On Ethereum, smart contracts are transparent, like open APIs, so your smart contract can include someone else's smart contract.

**==Properties:==**

**Decentralized**: dapps operate on Ethereum, so no-one and no group has control over it. This also means that once you upload a dapp, you cannot take it back
**Deterministic**: dapps perform the same function each time given the parameters
**Turing complete**: dapps can perform any action given required resources
**Isolated**: dapps are executed on the EVM, which is a virtual environment preventing it from having consequential effects on the blockchain

**==Benefits==**:

**Zero downtime**: because they cannot be taken back and are constantly present on the blockchain, they do not have downtime
**Privacy**: you can access dapps anonymously
**Resistance to censorship**: no-one can block individuals from using dapps, submitting transactions or accessing data on the blockchain
**Complete data integrity**: data on the blockchain is immutable and indisputable, which means that malicious actors cannot forge transactions or alter data that has been made public
**Trustless computation and verifiable behavior**: smart contracts can be analyzed and guaranteed to execute in predictable ways, without needing to trust a central authority. 

**==Drawbacks==**:

**Maintenance**: dapps are hard to maintain and update, as code and data published to the blockchain is harder to modify. It's hard for developers to make updates if bugs and security risks are identified in an old version.
**Performance overhead:** scaling is really hard, to achieve the level of security, integrity, transparency and reliability that Ethereum aspires to have, every node runs and stores every transaction.
**Network congestion**: when one dapp uses too many resources, the whole network gets clogged up. Currently, the network can only process 10-15 transactions, so if they are being sent faster than this, the pool of unconfirmed transactions can quickly balloon.
**UX**: user friendly experiences can be tough to achieve
**Centralization**: user and developer friendly solutions build on-top of the Ethereum base layer may end up looking like centralized applications

# Nodes & Clients

A node is an instance of the Ethereum client software that is connected to other computers running the Ethereum software. These nodes form a network. 

A client is an implementation of Ethereum that verifies data against protocol rules keeping the network secure. 

**Execution Client**: a client that listens to new transactions broadcast into the network, executing them in the EVM, and holding the latest state of current Ethereum data.

**Consensus Client**: a client that implements the proof of stake algorithm, which enables the network to achieve consensus based on validated data from the execution client. A validator can be added to the consensus client, allowing a node to participate in securing the network.

These clients work together to keep track of the head of the chain, and allow for users to interact with the network. This approach makes it easier to develop and maintain software, and enables the reuse of individual clients.

![[Untitled 2.avif]]

**Client Diversity**: both execution and consensus clients exist in a variety of programming languages, developed by different teams.

Multiple implementations of clients can make the network stronger, as it reduces dependency on one singular codebase. The ideal state is to have diversity without one singular client dominating the network, eliminating a potential singular point of failure. The variety of languages also invites developers of all backgrounds to create integrations in their own preferred language.

Each of these implementations follow a specific set of specifications.

**Node Types**:

**Full Nodes:** full nodes do a block-by-block validation of the blockchain, downloading and verifying the block body and state data for each block. Some full nodes verify starting from the genesis block, going through the entire history, while others start at a more recent and valid block. 

Regardless of where this verification starts, full nodes only keep a local copy of the most recent 128 (typically) blocks, allowing older data to be deleted. This data can be regenerated when needed.

They:

* Store full blockchain data (although typically pruned so a full node does not store all data going back to genesis)
* Participate in block validation, verifying all blocks and states
* Can either be retrieved from local storage or regenerated from "snapshots" by a full node
* Serve the network and provide data on request

**Archive Nodes:** full nodes which do not delete any of the downloaded data from genesis, verifying every block. 

They:

* Store everything kept in the full node and build an archive of historical states. They are needed if you want to query something like an account balance at a certain block or simply reliably test your own transactions.
* The data stored represents units of terabytes, which makes archive nodes less attractive for average users but handy for analytics, vendors and block explorers.

**Light Nodes:** instead of downloading every block, light nodes download block headers. These headers summarize the content of the blocks. Any other information required gets requested from a full node. The light node can independently verify data against the state roots in the block headers. 

They enable users to fully participate in the network without the powerful hardware or the bandwidth to run full nodes. Eventually, light nodes may be able to run on phones and other devices. 

Light clients are currently in an area of development for Ethereum, and new light clients are expected for the consensus and execution layers.

**Synchronization Modes:** to follow and verify current data in the network, the Ethereum client has to synchronize with the current state of the network. This is done by downloading data from peers, and establishing a local blockchain database. 

Synchronization modes represent the different approaches to doing this, and the trade-offs with each approach.

**==Execution Layer Synchronization Modes:==** 

**Full Archive Sync**h**: download all blocks and generate the state of the blockchain incrementally by executing every block from genesis.
- Minimizes the dependence on trust, and maximizes the security by verifying each transaction.
- It can take days to weeks to process all transactions

**Full Snap Synch**: verifies the chain block-by-block, similar to the full archive sync, however, it starts at a trusted check-point. The node saves periodic checkpoints while deleting data older than a certain age.
* Fastest sync strategy, currently the default
* Saves a lot of disk usage and bandwidth without risking network security

**Light Synch**: download all the block headers, and verify some randomly. Only synchs the tip of the chain from a trusted checkpoint.
- Gets only the latest state while relying on trust in developers and consensus mechanism
- Client ready to use with current network state in a few minutes

**==Consensus Layer Synchronization Modes:==**

**Optimistic Synch:** post-merge synchronization allows execution nodes to synch via established methods. 

==**Nodes as a Service:**== as known, stakers can run nodes to support the proof-of-stake model for Ethereum, where solo stakers must run the consensus and execution client from their own system. 

Node service providers, which are for non-staking nodes, run distributed node clients behind the scenes, providing API keys to users to read and write to the blockchain. Almost all of these services are extremely easy to integrate with.

==**Node Architecture**==

An Ethereum node is comprised of a consensus and execution client, compared to the proof-of-work method of just an execution client. The diagram below shows the relationship between the execution and consensus client:
![[Untitled 3.avif]]

The **execution client** is responsible for transaction handling, transaction gossip, state management and supporting EVM. However, it is not responsible for block building, block gossiping or consensus logic. 

The execution client creates execution payloads, which include: the list of transactions, updated state trie and other data. 

Consensus clients include the execution payload in each block. The execution client is also responsible for re-executing transactions in new blocks to ensure they are valid. 

In summary, the execution client is a user gateway to Ethereum, and is the home to the EVM, Ethereum's state and transaction pool.

The **consensus client** deals with all the logic which enables a node to stay in sync with the Ethereum network. 

This includes receiving blocks from peers and running a fork-choice algorithm to ensure the node always follows the chain with the greatest accumulation of attestations (weighed by validator effective balances). 

Similar to the execution client, consensus clients have their own P2P network through which they share blocks and attestations.

The consensus client does not participate in attesting to or proposing blocks (a validators job). A consensus client without a validator only keeps up with the head of the chain, allowing the node to stay synced. This enables a user to transact with Ethereum using their execution client, confident that they are on the correct chain.

![[Pasted image 20240707102553.png]]**Note:** gossiping is an information dissemination technique similar to how epidemics spread, where each user spreads information from one to the next.

==**Light Clients:**== a light node is a node running a light client software. It is essentially keeping the necessary information for each block, rather than the full blocks that a full node or archive node does. 

*How do light clients work?* 

They essentially work through the use of a synch committee, where a subset of 512 validators are selected to sign the header of recent blocks. Each block header contains the aggregated signature, and which validators signed it, as well as the validators expected to sign the next block.

This means a light client can quickly see that the synch committee has signed off on the data they receive, and they can also check that the sync committee is the genuine one by comparing the one they receive from the one they were told to expect in the previous block. 

In this way, the light client can keep updating its knowledge of the latest Ethereum block without actually downloading the block itself, just the header which contains summary information.

On the execution layer, there is no specification for a light client.

Light clients allow for secure validation and verification of incoming data, while using up very little computational power compared to full or archive nodes.  This benefits users, especially those with negligible hardware, who are now able to access Ethereum with minimal reliance on third parties. 

Light clients could be embedded into browsers, used in mobile phones and even smaller devices such as smart watches.

An extension of this is enabling internet of things **IOT** devices. A light client can easily be used to prove ownership of some token balance or NFT, allowing for easy transactions or transmissions on the go. 

It is also good for rollups (see Level 2), which will be less prone to hacks targeting the bridges that allow for funds to transfer from Mainnet to the rollup. 

"One vulnerability is the oracles that rollups use to detect that a user has made a deposit into the bridge. If an oracle feeds bad data, they could trick the rollup into thinking there was a deposit to the bridge and to incorrectly release funds. A light client embedded in the rollup could be used to protect against corrupted oracles because the deposit into the bridge could come with a proof that can be verified by the rollup before releasing any tokens. The same concept could also be applied to other interchain bridges."

Finally, light clients can be used to upgrade wallets. Instead of depending on data provided from an RPC provider, your wallet could directly verify the data being presented.

==**Archive Nodes:**==

The global data with information about each account and contract is stored in a database called state. This is handled by the execution layer client and includes:
- Account balances and nonces
- Contract code and storage
- Consensus-related data, e.g. Staking Deposit Contract

To interact with the network, Ethereum clients have to keep up with the recent changes (the tip of the chain), aka the current state. 

An execution layer client configured as a full node verifies and follows the latest state of the network but only caches the past few states (last 128 blocks). This is done so that it can provide fast data and handle chain reorgs. 

The state can be seen as a momentary snapshot, while the archive is a history replay of the network.

Historical states can be pruned as they are not necessary for the network to operate and it would be redundant to keep out-of-date data. States that existed ~128 blocks away from the head of the chain are effectively thrown out. Thus, full nodes only keep historical blockchain data (blocks and transactions) and occasional snapshots so they can regenerate older states on request.

However, this means that accessing a historical state on a full node needs a lot of computational power, as all past transactions are needed to be recomputed to initialize a previous state. Archive nodes solve this by storing the most recent states but also every historical state created after each block. 

**Archive Node Use Cases:** sending transactions, deploying contracts and verifying consensus does not require access to historical states. The main benefit of state archives is a quick access to queries about historical states (which are saved on disk). 

# Smart Contracts

Participants don't write a snippet of code everytime they want to process a transaction in the EVM. Instead, developers upload smart contracts into the EVM state, and users make requests to execute these snippets with different parameters.

A good allegory for a smart contract is that it is a vending machine: a script that, when given certain parameters, performs computation if certain conditions are satisfied.

Any developer can make a smart contract, and any user can use a smart contract, but in both cases a fee has to be paid to the network to execute/upload the code.


