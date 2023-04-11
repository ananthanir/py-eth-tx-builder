# py-eth-tx-builder

A simple project that try to send transaction to the Ethereum blockchain. It interacts with Vyper contract using web3.py

* main-1.py = signs and send a transaction
* main-2.py = builds, signs then sends the transaction

### To run

Clone the repo

```bash
git clone https://github.com/ananthanir/py-eth-tx-builder
cd py-eth-tx-builder
```

Change into hardhat-vyper directory

```
cd hardhat-vyper
```

Now follow the read me to deploy the contract, and come back to root directory

```
cd ..
```

To run

```
python main-1.py
```
 or 
```
python main-2.py
```