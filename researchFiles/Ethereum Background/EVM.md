Blockchain is usually described with the analogy of "distributed ledger". This ledger maintains a record of the activity which adheres to a set of rules based on what someone can and cannot do to the ledger. For example, someone cannot receive more ETH than they send. 

While Ethereum has ETH, it's own currency, it has something much more powerful: smart contracts. Instead of a distributed ledger, as Bitcoin tends to be described, Ethereum is more like a state machine, which is a large data structure that not only holds all accounts and balances, but is also a machine state, which can change block to block according to a set of rules. 

**State:** the state is an enormous data structure, which keeps all accounts linked by hashes and reducible to a single root hash stored on the blockchain.

**EVM Instructions:** executes as a stack machine, with a depth of 1024 items. Each item is a 256-bit hash word. During execution, the EVM maintains a transient memory, which does not persist between transactions. 

Contracts, however, do contain a Merkle Patricia _storage_ trie (as a word-addressable word array), associated with the account in question and part of the global state.

"Compiled smart contract bytecode executes as a number of EVM [opcodes](https://ethereum.org/en/developers/docs/evm/opcodes/), which perform standard stack operations like `XOR`, `AND`, `ADD`, `SUB`, etc. The EVM also implements a number of blockchain-specific stack operations, such as `ADDRESS`, `BALANCE`, `BLOCKHASH`, etc."

![[Untitled 1.avif]]
