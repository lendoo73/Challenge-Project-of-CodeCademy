# [What is Blockchain?](https://www.codecademy.com/courses/introduction-to-blockchain/lessons/blockchain-introduction/exercises/what-is-blockchain)

The blockchain is similar to a permanent book of records that keeps a log of all transactions that have taken place in chronological order.

The blockchain logs transactions between senders and receivers, except there is no bank or central authority.
The blockchain relies on a public network of computers to verify the transaction. 
The blockchain is a record of all the transactions that have happened amongst the members in that blockchain’s network.
Each block in the blockchain represents a transaction, and each transaction is connected to the prior transaction to form the entire connected blockchain.

## Block:
A block is an individual transaction or piece of data that is being stored within the blockchain.

## Blockchain:
A blockchain is a continuously growing list (“chain”) of records (“block”), called blocks, which are linked chronologically and secured using cryptography.
A blockchain is an accurate and permanent record of transactions that have been verified and stored in a chronological sequence.

# [The Blockchain Network](https://www.codecademy.com/courses/introduction-to-blockchain/lessons/blockchain-introduction/exercises/blockchain-network)
In the blockchain, there are many participants in the network that are constantly checking to ensure that each transaction is valid.
Each participant is a computer that owns a copy of the blockchain.
These participants cross-reference their copy of the blockchain each time a new block is being introduced.
Because this validation depends on multiple participants, the digital record is “decentralized”.

In order for a new block to be added, 51% of all of the participants in the blockchain network must verify that the new block is not fraudulent. Once a block has been verified as a valid transaction, it is added to each participant’s copy of the blockchain.

By having the majority of participants validate a new transaction, the blockchain removes the need for a central authority and automates the completion of transactions, reducing transaction fees while ensuring a high level of security.

## Blockchain Network:
The blockchain network and blockchain are terms used interchangeably. They represent the entire blockchain from the structure itself to the network that it is a part of.

## Decentralization:
The concept in which participants work together to validate transactions without relying on a central authority.

## Participant:
A client that owns a copy of the blockchain and verifies transactions across the network.

# [Blocks in the Blockchain](https://www.codecademy.com/courses/introduction-to-blockchain/lessons/blockchain-introduction/exercises/blockchain-blocks)
A block contains transaction data and other important details related to the creation of that block, such as the time when it was created and other unique information.
To create a block, we must have a record that we wish to store.

A block will always contain 
* a timestamp or the data regarding the time when the block was created;
* a unique hash or a unique code produced by combining all the contents within the block itself — also known as a digital fingerprint;
* a previous hash or a reference to the prior block’s hash. This reference to the prior block is how blocks chain to one another.

## Properties in a Block:
* **Timestamp:** The time the block is created determines the location of it on the blockchain.
* **Transaction Data:** The information to be securely stored in the block.
* **Hash:** A unique code produced by combining all the contents within the block itself — also known as a digital fingerprint.
* **Previous Hash:** Each block has a reference to the block prior to its hash. This is what makes the blockchain unique because this link will be broken if a block is tampered with.

# [Hashing](https://www.codecademy.com/courses/introduction-to-blockchain/lessons/blockchain-introduction/exercises/hashing)
Hashing is an application of cryptography that is fundamental to the design of the blockchain. It is a way to generate a seemingly random, but calculated string of letters and numbers from any input.

Think of a hash function as a machine that takes an object and turns it into a varying combination of letters and numbers. 
The output is known as the hash of the input.

There are many types of hash functions available. 
Blockchain uses a *cryptographic hash function*, meaning that the output is *random but deterministic*.
This means the same input will always produce the same hash.
That process is one-way, so the output (hash) cannot be used to produce the original input.

## Deterministic:
The same input will always produce the same output, but that output cannot produce the original input.

## Hash:
A calculated string of letters and numbers produced from a specific input.

## Hash Function:
A function that takes in an input of a random size, performs hashing on the input, and generates a seemingly random output of a fixed size, also known as the hash.

# [The Genesis Block](https://www.codecademy.com/courses/introduction-to-blockchain/lessons/blockchain-introduction/exercises/genesis-block)
A blockchain is similar to a permanent book of records,  it keeps an accurate unchanging record of all data, or transactions, stored in chronological order.
Each block has a reference to the block’s previous hash.
If a block’s contents are tampered with, the block’s hash changes and the chain breaks, making it difficult to successfully tamper with any one piece of the chain.

Since all blocks in the blockchain have a reference to the previous block, the first block is a little different than the rest.
It is known as the *Genesis Block*. The Genesis Block does not have a block before it. 
So it wouldn’t make sense to have a previous hash stored inside it. 
The value of the previous hash is typically hard-coded into the Genesis Block with the default value of zero.

## Genesis Block:
The first block on the blockchain and it is typically hard-coded into the blockchain structure.
Being the first block on the blockchain, it does not have a link to a previous hash.
