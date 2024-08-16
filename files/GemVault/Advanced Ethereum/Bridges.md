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
	
![[Pasted image 20240709120433.png]]

**Integrating Bridges to dapps:**

1) Building your own bridge is not easy, as it requires years of experience to build a secure and reliable bridge.
2) Many dapps require users to have their native token to interact with them. To enable users to access their tokens, they offer different bridge options on their website. However, this method is a quick fix to the problem as it takes the user away from the dapp interface and still requires them to interact with other dapps and bridges.
3) Integrating a bridge doesn’t require the dapp to send users to the external bridge and DEX interfaces.
4) Integrating multiple bridges solves many problems associated with integrating a single bridge.


