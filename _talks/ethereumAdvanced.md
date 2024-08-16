---
title: "Advanced Ethereum"
collection: talks
type: "Conference proceedings talk"
permalink: /research/ethereumAdvanced
date: 2014-03-01
---

# Bridges

Bridges connect blockchain networks. They enable connectivity and interoperability between blockchains. Blockchains operate in siloed environments, so they cannot trade or communicate with other blockchains naturally.

**Benefits of Bridges:**

Bridges unlock use cases by allowing blockchains to exchange data and move assets between them. Each blockchain has their own advantages and disadvantages, bridges help the development of the overall crypto ecosystem by connecting them together.

For developers, bridges enable:

1) Transfer of data, information and assets across chains.
2) Unlocking new features and use cases for protocols.
3) Opportunity to leverage the strength of different blockchains. For example, developers can benefit from the lower fees offered by different L2 solutions.
4) Collaboration among developers from various blockchain ecosystems.
5) Attracting users and communities from various ecosystems.

**How do they work?**

There are three ways to do cross-chain transfer which stand out:

1) Lock and mint: lock assets on the source chain and mint assets on the destination chain
2) Burn and mint: burn assets on the source chain and mint assets on the destination chain
3) Atomic swaps: swap assets on the source chain for assets on the destination chain with another party

**Bridge Types:**

Bridges can be classified into the following categories:
1) Native bridges: typically built to bootstrap difficulty on a blockchain, making it easier for users to move funds to the ecosystem. 
2) Validator or oracle based bridges: bridges which rely on external validators or oracles to validate cross-chain transfers.
3) Generalized message passing bridges: transfer assets, along with messages and arbitrary data across chains.
4) Liquidity networks: primarily focus on transferring assets from one chain to another with atomic swaps. Generally, they don't support cross-chain message passing.

**Trade-offs to Consider:**

1) Security: who verifies the system? Bridges secured by external validators are less secure than bridges that are locally or natively secured by the blockchain's validators
2) Convenience: how long it takes to complete a transaction, how many transactions did a user need to sign
3) Connectivity: what are the different destinations a bridge can connect to and how difficult is it to integrate a new blockchain
4) Ability to pass more complex data: can a bridge enable the transfer of messages and more complex arbitrary data
5) Cost effectiveness: how much does it cost to transfer assets via a bridge. 

**Trusted Bridges**: bridges which are externally verified. They use an external set of verifiers to send data across chains. As a result, they offer great connectivity. 

**Trustless Bridges**: bridges that rely on the blockchains they are connecting to and their validators to transfer messages and tokens. They are trustless because they do not add new trust assumptions, and as a result are considered more secure.
	**Generalized Message Passing Bridges:** excel with security and transfer more complex data across chains. They are also typically good with cost effectiveness. However, the strengths come at the cost of connectivity for light client bridges and speed drawbacks for optimistic bridges that use fraud proofs.
	**Liquidity Networks:** these bridges use atomic swaps and are logically verified systems. As a result, they excel with security and speed. Moreover, they are cost-effective and offer good connectivity. However, they cannot pass complex data like generalized message passing bridges can.

<img src="/researchFiles/20240709120433.png">

**Integrating Bridges to dapps:**

1) Building your own bridge is not easy, as it requires years of experience to build a secure and reliable bridge.
2) Many dapps require users to have their native token to interact with them. To enable users to access their tokens, they offer different bridge options on their website. However, this method is a quick fix to the problem as it takes the user away from the dapp interface and still requires them to interact with other dapps and bridges.
3) Integrating a bridge doesn’t require the dapp to send users to the external bridge and DEX interfaces.
4) Integrating multiple bridges solves many problems associated with integrating a single bridge.

# Layer 2

Layer 1 is the base blockchain. Ethereum and Bitcoin are both layer 1, as they are the underlying foundation that layer 2 networks build on top of.

Examples of layer 2 projects include "rollups" on Ethereum and the Lightning Network on Bitcoin. All user transaction activity on the layer 2 projects ultimately settle back to layer 1 of the blockchain.

Ethereum also functions as a data availability layer for layer 2s. Layer 2 projects will post their data on Ethereum (transactions), relying on Ethereum for data availability. This data is used to dispute transactions or get the state of layer 2.

<img src="/researchFiles/20240708134030.png">

## Layer 2

**Why Layer 2?**

Blockchain is:
1) Decentralized
2) Secure
3) Scalable
A simple blockchain architecture can only achieve two out of the three. The main goal of layer 2 is to achieve scalability without compromising decentralization and security. When the demand to use Ethereum is high (as it only supports 15 transactions per second), the network becomes congested, increasing transaction fees. Layer 2s are solutions which reduce the fees by processing transactions off the blockchain's layer 1.

**Benefits:**
<img src="/researchFiles/20240708161708.png">
<img src="/researchFiles/20240708161726.png">
<img src="/researchFiles/20240708161734.png">

**How does it work?**

Layer 2 is essentially a separate blockchain that extends Ethereum, handling transactions from layer 1 while taking advantage of the security and decentralization. There are a few types of layer 2 blockchains.

**Rollups**

<img src="/researchFiles/Untitled 4.avif">

Rollups bundle hundreds of separate transactions into a singular transaction in layer 1. This distributes the L1 transaction fees across everyone in the roll-up, making it cheaper for each user. 

The transaction data is submitted to layer 1, but the execution of the transaction is done by the rollup. By submitting the transaction to layer 1, rollups inherit the security of Ethereum. This is because once the data is uploaded to Ethereum, reverting a rollup requires reverting Ethereum. 

There are two approaches to rollups, which differ primarily on how the transaction data is submitted to layer 1.

1) **Optimistic Rollups:** optimistic in the sense that transactions are assumed to be valid, but can be challenged if necessary. If a transaction is suspected, a fault proof is run to see if it is invalid.
2) **Zero Knowledge Rollups:** zero knowledge rollups use validity proofs, where transactions are computed off-chain and then compressed data is supplied to Ethereum as a proof of validity.

# MEV

MEV refers to the maximum value that can be extracted from block production in excess of the standard block reward and gas fees by including, excluding and changing the order of transactions in the block.

**MEV Extraction**

In theory, MEV accrues entirely to validators as they are the only party that can guarantee the execution of a profitable MEV opportunity. In practice, MEV is primarily extracted by independent network participants referred to as searchers. 
	Searchers run complex algorithms on blockchain data to detect profitable MEV opportunities and have bots to automatically submit those profitable transactions to the network.
Validators do get a portion of the full MEV amount as searchers pay a high gas fee to get higher likelihood of their profitable transactions in the block. Assuming searchers are rational, they are willing to pay up to 100% (usually 90%) of their MEV in gas fees.

**Gas Golfing**

This dynamic has made being good at gas golfing profitable. Gas golfing is essentially using tricks to minimize gas usage, such as using accounts with high number of 0's in their hash, or leaving a small amount of tokens in an account as it costs less gas to update a storage slot than to initialize one.

**Generalized Frontrunners**

Rather than programming efficient algorithms to detect MEV opportunities, some searchers run generalized frontrunners. These are bots that watch the mempool to detect profitable transactions. The frontrunner will copy the profitable transaction's code, replace addresses with the frontrunner's address and run the transaction locally to double-check that the modified transaction results in a profit. If it is profitable, the frontrunner will submit the modified transaction with the replaced address and get the original searcher's MEV.

**Flashbots**

It is an independent project which extends execution clients with a service that allows searchers to submit MEV transactions to validators without revealing to the public mempool. This prevents transactions from being frontrun.

## MEV Examples

**Decentralized Exchange (DEX) Arbitrage**:

If two DEXes are offering a token at two different prices, someone can buy it on the lower-priced DEX and sell it on the higher priced DEX in a single atomic transaction. This is true, riskless arbitrage.

**Liquidations:**

Lending protocols like Maker and Aave require users to deposit some collateral. This collateral is then used to lend out to other users.

Users can borrow assets and tokens from others depending on what they need up to a certain percentage of their deposited collateral. 

As the value of the collateral fluctuates, so too does it's borrowing power. If, due to fluctuations, the borrowed amount exceeds the collateral percentage, the protocol allows anyone to liquidate the collateral, paying off lenders. If liquidated the borrower has to pay a liquidation fee, some of which goes to the liquidator.

Searchers compete to parse blockchain data as fast as possible to determine which borrowers can be liquidated and be the first to submit a liquidation transaction and collect the liquidation fee for themselves.

**Sandwich Trading:**

To sandwich, a searcher will watch the mempool for large DEX trades (UNI to DAI trade will increase the price of UNI and decrease the price of DAI). A searcher can calculate the approximate price effects of this large trade, buying the token before the price increases and selling immediately after the large trade.

Sandwiching is however riskier.

**MEV In Ethereum PoS**

There are several issues that MEVs can cause, with an important one being the capability of accelerating blockchain validator centralization. 

A way to fix this that has been proposed is Proposer Builder Separation (PBS). In both PoW and PoS, a node that builds a block proposes it for addition to the chain to other nodes in the consensus. A new block becomes canonical after another miner builds on top of it or it receives enough attestations. 

The combination of block producer and block proposer roles is what causes a majority of the problems that are related to MEV. PBS is designed to mitigate the impact of MEV, especially at the consensus level. With PBS, validators are still responsible for proposing and voting on blocks, but a new class of specialized entities, called block builders, are tasked with ordering transactions and building blocks.

In-protocol proposer-builder separation reduces MEV’s effect on consensus by removing MEV extraction from the purview of validators. Instead, block builders running specialized hardware will capture MEV opportunities going forward.

