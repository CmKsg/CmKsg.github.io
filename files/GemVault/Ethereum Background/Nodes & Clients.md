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

