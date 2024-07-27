# In-Memory Key-Value Store Server and Client

## Project Overview

This project implements a simple in-memory key-value store server and client application using Python's `gevent` library for handling concurrency and network communication. The server supports basic operations such as `GET`, `SET`, `DELETE`, `FLUSH`, `MGET`, and `MSET`. The client can connect to the server, send commands, and receive responses.

## Requirements

- Python 3.8+
- `gevent` library

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ankurac7/key-value-store.git
cd key-value-store
```
### 2. Install Dependencies
```
pip install gevent
```
## Usage
To start the server, run the following command:
```
python server.py
```

To interact with the server, use the client:
```
python client.py
```
#### Command Handling Logic:
Implement handlers for commands like GET, SET, DELETE, FLUSH, MGET, and MSET:
- GET: Retrieve the value for a given key.
- SET: Set the value for a given key.
- DELETE: Remove a key-value pair.
- FLUSH: Clear all data from the store.
- MGET: Retrieve values for multiple keys.
- MSET: Set multiple key-value pairs.

## Features

- **Concurrency**: The server leverages the `gevent` library to handle multiple client connections concurrently, ensuring efficient and non-blocking I/O operations.

- **Basic Commands**: The server supports a range of essential commands:
  - `GET`: Retrieve the value associated with a specific key.
  - `SET`: Store a key-value pair in the server's in-memory dictionary.
  - `DELETE`: Remove a specific key-value pair.
  - `FLUSH`: Clear all data from the key-value store.
  - `MGET`: Retrieve values for multiple keys in a single command.
  - `MSET`: Set multiple key-value pairs in a single operation.

- **In-Memory Storage**: The server uses an in-memory dictionary to store key-value pairs, providing fast data access and manipulation.

- **Protocol Handling**: Implements a simple communication protocol using JSON for data exchange between the client and server.

