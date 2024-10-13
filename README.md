# The Flask Filler

## Description

**The Flask Filler** is a game where text files serve as inputs to play. The game is built using Python, with custom stack and queue implementations to manage gameplay mechanics. Players provide input through text files to simulate filling and managing flasks.

## Features

- **Custom Queue and Stack Implementations:** Implements a queue (`bqueue.py`) and a stack (`bstack.py`) to handle game mechanics.
- **Text File Inputs:** Players can provide game configurations and commands via text files.
- **Modular Codebase:** The main game logic is handled in `Assignment3FINAL.py`, utilizing the custom data structures for gameplay.

## How It Works

1. **Input:** Players submit text files containing commands or configurations that guide the flask-filling process.
2. **Initialization:** The game reads and processes the input files, setting up necessary data structures.
3. **Process:** The game processes the input commands using a combination of stacks and queues to simulate the filling and organizing of flasks.
4. **Output:** The game outputs the results of the flask-filling process based on the input commands.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Clone the repository or download the files `Assignment3FINAL.py`, `bqueue.py`, and `bstack.py`.
2. Prepare your input text files with the required game configurations.
3. Run the game using the command:

    ```bash
    python Assignment3FINAL.py
    ```

4. Provide the text file as input when prompted or specify it in the code.

### Example

```bash
$ python Assignment3FINAL.py
```
The script will read the text file and simulate the game based on the provided input.

## Program Structure

- **`bqueue.py`**: Contains the implementation of the queue data structure.
- **`bstack.py`**: Contains the implementation of the stack data structure.
- **`Assignment3FINAL.py`**: The main script that manages game logic and interaction with input files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

