# Programming 3 Project

Welcome to the repository for my Programming 3 project. This project encompasses several critical aspects of advanced programming, specifically focusing on Design Patterns, Socket Programming, and Threading. This README provides an overview of the project structure, the key concepts covered, and how to navigate and use the provided code.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Design Patterns](#design-patterns)
    - [Singleton](#singleton)
    - [Factory](#factory)
    - [Observer](#observer)
3. [Socket Programming](#socket-programming)
    - [Client-Server Model](#client-server-model)
    - [Example Implementations](#example-implementations)
4. [Threading](#threading)
    - [Multithreading Basics](#multithreading-basics)
    - [Synchronization](#synchronization)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

## Project Overview

This project demonstrates the application of various programming paradigms and concepts learned in the Programming 3 subject. The main areas of focus are:

- **Design Patterns**: Implementing and utilizing common design patterns to solve software design problems.
- **Socket Programming**: Building networked applications using sockets for communication between client and server.
- **Threading**: Managing concurrency in applications to perform multiple tasks simultaneously.

## Design Patterns

### Singleton

The Singleton pattern ensures a class has only one instance and provides a global point of access to it. This pattern is particularly useful for managing shared resources, such as configuration settings or a connection pool.

**Key Features:**
- Lazy Initialization
- Thread Safety

**Example Implementation:**
```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
