Oracles are applications that produce data feeds that make off-chain sources available for smart contracts. This is necessary to access information outside of the blockchain. This makes dapps and smart contracts have a ton more use cases and applications.

Besides pulling off-chain data into smart contracts, oracles can also push data off-chain to external systems. They differ based on source data, system architecture and trust models.

Blockchains are deterministic, as they have to be. Smart contracts execute the same result given information every single time. This means that incorporating non-blockchain data is tough, as this can cause the deterministic aspect to falter. So, oracles are used by smart contracts to gather external information through the use of APIs, and that information is then used for needed transactions.

Because the real-world is not as absolute as the blockchain, there are some issues that arise. For example, how do we verify that the injected information was extracted from the correct source or how do we ensure the data is consistently available and updated regularly?

This results in the **Oracle Problem**:

Oracles are typically validated on the following 3:

1) Correctness: An oracle must guarantee _authenticity_ and _integrity_ of data. Authenticity means the data was gotten from the correct source, while integrity means the data remained intact (i.e. wasn’t altered) before being sent on-chain.
2) Availability: An oracle should not delay or prevent smart contracts from executing actions and triggering state changes. This means that data from an oracle must be _available on request_ without interruption.
3) Incentive Compatibility: An oracle should incentivize off-chain data providers to submit correct information to smart contracts. Incentive compatibility involves _attributability_ and _accountability_. Attributability allows for linking a piece of external information to its provider, while accountability bonds data providers to the information they give, so they can be rewarded or penalized based on the quality of information provided.

**How does an oracle work?**

**Users**: entities that need information external to the blockchain to complete actions. 

Data requests will usually answer some or all of the following questions:

1. What sources can off-chain nodes consult for the requested information?
2. How do reporters process information from data sources and extract useful data points?
3. How many oracle nodes can participate in retrieving the data?
4. How should discrepancies in oracle reports be managed?
5. What method should be implemented in filtering submissions and aggregating reports into a single value?

**Oracle Contract:** the on-chain component for the oracle service. It listens to data requests from other contracts, relays data queries to oracle nodes and broadcasts returned data to client contracts. This contract may also perform some minor computations.

**Oracle Nodes:** the off-chain component for the oracle service. It extracts information from external resources, such as APIs and put's it on-chain for consumption by smart contracts. It essentially acts as a GET request for smart contracts.

==**Design Patterns:**== 

**Publish Subscribe**

This type of oracle exposes a data feed which other contracts can regularly read for information. The data is expected to change frequently, so contracts must listen for updates.

**Request Response**

This type allows the client contract to request arbitrary data other than that provided by a publish-subscribe oracle. Ideal when the dataset is too large to be stored in a smart contract's storage.

==**Centralized vs. Decentralized:**== 

**Centralized Oracles:**

Controlled by a single entity responsible for aggregating off-chain information and updating the oracle contract's data as requested. Efficient since they rely on a singular source of truth.

**Low Correctness Guarantees**

There is no way to ensure that the data provided is correct or not.

**Poor Availability**

Not guaranteed to always make off-chain data available to other smart contracts.

**Poor Incentive Compatibility**

Often have poorly designed or non-existent incentives for the data provider to send accurate/unaltered information.

**Decentralized Oracles:**

Comprised of multiple participants in a peer-to-peer network that form consensus on off-chain data before sending it to a smart contract.

**High Correctness Guarantee**

- Authenticity proofs: cryptographic mechanisms that validate the source of the information and detect possible alterations to the data after retrieval.
- Consensus based validation of information: rely on multiple oracles to query off-chain information. By comparing multiple oracles, decentralized oracles reduce the risk of passing invalid information to on-chain contracts.
	- Some decentralized oracle networks require participants to vote or stake on the accuracy of answers to data queries using the network's native token. Nodes whose answers deviate are punished by having their tokens taken.
	- Schelling-point mechanisms use game-theory to create single aggregate values, the mean of all entries in the peer-to-peer network in order to minimize on-chain footprint.

**Availability**

Decentralized oracle services ensure high-availability of off-chain data to smart contracts. This is achieved by both decentralizing the off-chain source of information and nodes responsible for transferring information on-chain.

This ensures fault-tolerance. Decentralization at the source and node-operator level is crucial. It is also possible for stake-based oracles to slash node operators who fail to respond quickly to data requests.

**Incentive Compatibility**

Decentralized oracle nodes are often required to sign the data they provide in response to data requests. Decentralized oracles may require nodes to place a stake on their confidence in the truth of data they submit. If the claim checks out, this stake can be returned along with rewards for honest service.

**Applications:**

Retrieving Financial Data: exchange rate data, capital markets data etc. to keep a live feed on prices

Generating Verifiable Randomness: for block-chain based games and lotteries, the deterministic nature of the blockchain is harmful. Therefore, randomness is implemented from external sources.

Getting Outcomes for Events: retrieving real-world event outcomes to enable other novel use cases.

Automating Smart Contracts: smart contracts do not run automatically, thus developers need to trigger some parts of the applications at intervals to ensure it is running smoothly.
