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

**==MEV Examples==**

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