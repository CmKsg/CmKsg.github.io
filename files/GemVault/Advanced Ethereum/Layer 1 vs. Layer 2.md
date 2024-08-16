Layer 1 is the base blockchain. Ethereum and Bitcoin are both layer 1, as they are the underlying foundation that layer 2 networks build on top of.

Examples of layer 2 projects include "rollups" on Ethereum and the Lightning Network on Bitcoin. All user transaction activity on the layer 2 projects ultimately settle back to layer 1 of the blockchain.

Ethereum also functions as a data availability layer for layer 2s. Layer 2 projects will post their data on Ethereum (transactions), relying on Ethereum for data availability. This data is used to dispute transactions or get the state of layer 2.

![[Pasted image 20240708134030.png]]

**==Layer 2==**

**Why Layer 2?**

Blockchain is:
1) Decentralized
2) Secure
3) Scalable
A simple blockchain architecture can only achieve two out of the three. The main goal of layer 2 is to achieve scalability without compromising decentralization and security. When the demand to use Ethereum is high (as it only supports 15 transactions per second), the network becomes congested, increasing transaction fees. Layer 2s are solutions which reduce the fees by processing transactions off the blockchain's layer 1.

**Benefits:**
![[Pasted image 20240708161708.png]]
![[Pasted image 20240708161726.png]]
![[Pasted image 20240708161734.png]]

**How does it work?**

Layer 2 is essentially a separate blockchain that extends Ethereum, handling transactions from layer 1 while taking advantage of the security and decentralization. There are a few types of layer 2 blockchains.

**Rollups**

![[Untitled 4.avif]]
Rollups bundle hundreds of separate transactions into a singular transaction in layer 1. This distributes the L1 transaction fees across everyone in the roll-up, making it cheaper for each user. 

The transaction data is submitted to layer 1, but the execution of the transaction is done by the rollup. By submitting the transaction to layer 1, rollups inherit the security of Ethereum. This is because once the data is uploaded to Ethereum, reverting a rollup requires reverting Ethereum. 

There are two approaches to rollups, which differ primarily on how the transaction data is submitted to layer 1.

1) **Optimistic Rollups:** optimistic in the sense that transactions are assumed to be valid, but can be challenged if necessary. If a transaction is suspected, a fault proof is run to see if it is invalid.
2) **Zero Knowledge Rollups:** zero knowledge rollups use validity proofs, where transactions are computed off-chain and then compressed data is supplied to Ethereum as a proof of validity.