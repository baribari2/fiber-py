# `fiber-py`

## Installation
With Poetry:
```
poetry add git+https://github.com/chainbound/fiber-py
```

## Usage
### Connecting
```python
from fiber.client import Client 

client = Client('FIBER_ENDPOINT', 'YOUR_API_KEY')
try:
  client.connect()
except Exception as e:
  print('Error connecting', e)
```

### Subscribing to transactions
The transaction stream is supported but without any filtering for now. `subscribe_new_txs`
returns a stream of `fiber.client.Transaction`, shown below.
```python
try:
  sub = client.subscribe_new_txs()

  # Iterate over transaction stream
  for tx in sub:
    do_something(tx)
except Exception as e:
  print("error subscribing", e)
```

**Transaction type**:
We export our own transaction type. All the bytes fields are encoded as hexadecimal strings.
```python
class Transaction:
  to: str
  gas: int
  hash: str
  nonce: int
  value: int
  sender: str
  type: int
  gas_price: int
  input: str
  max_fee: int
  priority_fee: int
  v: int
  r: str
  s: str
  access_list: Any
  chain_id: int
```

### Subscribing to blocks
```python
try:
  sub = client.subscribe_new_blocks()

  for block in sub:
    do_something(block)
except Exception as e:
  print("error subscribing", e)
```

