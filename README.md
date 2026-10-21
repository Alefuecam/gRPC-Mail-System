# gRPC Mail System

A simplified email system developed in **Python**, using **gRPC**, **Protocol Buffers**, and **Tkinter** to implement client-server communication through remote procedure calls (RPCs).

The project demonstrates distributed systems concepts, remote method invocation, data serialization, multithreading, and persistent server-side storage.

## Features

- **User Registration:** Create accounts with unique usernames.
- **User Login:** Access an existing account.
- **Send Emails:** Exchange messages between registered users.
- **Inbox Management:** View received messages.
- **Outbox Management:** View previously sent messages.
- **Delete Emails:** Remove messages from the mailbox.
- **Read Status:** Track whether an email has been opened.
- **Data Persistence:** Preserve accounts and messages across client sessions and server restarts.
- **Graphical Interface:** Interact with the application through a Tkinter GUI.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Client and server implementation |
| gRPC | Remote procedure calls between client and server |
| Protocol Buffers | Definition of RPC services and message structures |
| Tkinter | Graphical user interface |
| Pickle | Serialization and persistence of application data |
| Python Dictionaries | In-memory data management |
| Python Threads | Concurrent execution |

## System Architecture

The application follows a client-server architecture.

### Client

The client provides a graphical interface built with Tkinter. Through this interface, users can register, log in, send messages, and manage their mailboxes.

User actions trigger remote procedure calls to the server using gRPC.

### Protocol Buffers

The `mail.proto` file defines the RPC services and message structures used for communication between the client and server.

The Protocol Buffers definitions are used to generate the Python code required for gRPC communication.

### Server

The server implements the remote procedures and manages application data, including user accounts, inboxes, outboxes, and message states.

Data is organized using Python dictionaries containing lists and tuples.

Each email is represented by information such as:

- Sender
- Numerical message identifier
- Subject
- Message content
- Read/unread status

Usernames serve as unique identifiers for registered accounts.

## Data Management

The server uses five principal dictionaries:

| Dictionary | Purpose |
|---|---|
| `usuarios` | Stores registered users and their credentials |
| `bandeja` | Stores received emails |
| `bandejaSalida` | Stores sent emails |
| `saturacion` | Helps manage mailbox capacity |
| `cantidadMail` | Tracks message quantities |

These dictionaries are grouped within a larger dictionary that represents the application's in-memory database.

## Data Persistence

To preserve application data across server restarts, the project uses Python's `pickle` library.

The persistence mechanism follows three main steps:

1. The server loads previously saved data when it starts.
2. User operations modify the in-memory data structures.
3. The updated data is serialized to an external file whenever the stored information changes.

This allows users to disconnect and reconnect without losing their accounts or messages. It also allows the server to recover previously saved information after restarting.

The implementation prioritizes simplicity and frequent data saving rather than database performance or transactional guarantees.

## Remote Procedure Calls

The RPC services defined in `mail.proto` support the main application operations:

- Registering users
- Logging in
- Sending emails
- Retrieving inbox messages
- Retrieving outbox messages
- Deleting emails
- Updating message read status

These operations are executed on the server and accessed remotely through the Python gRPC client.

## Running the Project

The application requires Python and the relevant gRPC dependencies.

General execution process:

1. Install the required Python dependencies, including `grpcio` and `protobuf`, with `grpcio-tools` if code generation is needed.
2. Generate the Python gRPC bindings from `mail.proto` if they are not already included.
3. Start the server application.
4. Launch the Tkinter client.
5. Register or log in to begin using the mail system.

The exact startup commands depend on the filenames and configuration used in the repository.

## Limitations and Possible Improvements

This project was developed as an educational implementation of a distributed email system.

Potential improvements include:

- Replacing Pickle storage with a transactional database such as SQLite or PostgreSQL.
- Implementing secure password hashing and stronger authentication.
- Improving concurrent access to shared data structures.
- Adding more robust error handling and connection recovery.
- Improving persistence efficiency and reliability.

**Security note:** The simplified authentication and Pickle-based storage are intended for a controlled educational environment. Pickle files should only be loaded from trusted sources, and the application should not be treated as a production-ready email service.

## Learning Outcomes

This project provided practical experience with:

- Designing and implementing remote procedure calls using gRPC.
- Defining services and messages with Protocol Buffers.
- Developing client-server applications in Python.
- Managing structured application data using dictionaries, lists, and tuples.
- Implementing file-based data persistence.
- Working with multithreading in Python.
- Integrating a graphical user interface with distributed application logic.

The project demonstrates the implementation of a functional distributed application, combining network communication, server-side state management, and persistent storage.
