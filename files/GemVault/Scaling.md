As the number of people who use Ethereum has grown, so has the number of transactions that occur on the chain. The problem with this is that Ethereum can only process 15 transactions per second, meaning that the gas fee for these transactions would be exorbitant due to the high traffic. To combat this, there have been several on-chain and off-chain solutions, increasing the scaling of the blockchain without harming the security and decentralization.

**On-Chain:**

**Sharding**

For a long time, sharding was meant to be the savior in terms of scaling. It is the process of splitting the database, by having subsets of validators responsible for individual shards rather than the entirety of Ethereum. However, the rapid development of rollups and danksharding has led the community to favor roll-up centric scaling.

**Off-Chain:**

**Layer 2 Scaling**

Layer 2 is a collective term for solutions designed to help scale applications by handling transactions off of the mainnet, while also having the full advantage of the security and decentralization of the mainnet.

Most layer 2 solutions are centered around a server or cluster of servers. Generally speaking, transactions are submitted to these layer 2 nodes instead of being submitted directly to layer 1. The layer 2 then batches these transactions up and anchors them to layer 1. 

**Rollups**

*Optimistic Rollups*: scaling Ethereum through moving computation and state storage off-chain. OR's execute transactions outside of Ethereum. Operators bundle multiple off-chain transactions together in large batches to submit to the Ethereum maainnet. This enables spreading fixed costs, and enables aspects like compression to reduce fees for all users.

Optimistic rollups are optimistic because they assume off-chain transactions are valid and don't publish proofs of validity for transactions hosted off-chain. Compared to zero-knowledge rollups, which publish proofs of validity for transactions, optimistic rollups instead rely on a fraud proving scheme to detect cases where transactions are not calculated correctly. After a rollup batch is submitted to Ethereum, there is a timeframe when anyone can challenge the results of the rollup by computing a fraud proof.

If the fraud proof succeeds, the rollup re-executes the transactions and updates the state accordingly. If it does not succeed, or is not challenged, the batch is deemed valid and accepted on Ethereum.

