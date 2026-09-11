# Tic-Tac-Toe using Minimax

A command-line implementation of **Tic-Tac-Toe in Python** where the computer uses the **Minimax algorithm** to play optimally.

The project demonstrates how game-tree search can be used to build an AI agent that makes the best possible move in a deterministic, zero-sum game.

## Features

* Human vs Computer gameplay
* Computer plays using the **Minimax algorithm**
* Computer cannot be beaten when Minimax is implemented correctly
* Detects:

  * Row victories
  * Column victories
  * Diagonal victories
  * Draws
* Validates human moves
* Simple command-line interface
* No external dependencies

## How Minimax Works

Tic-Tac-Toe has a maximum game depth of **9**, since there are only 9 cells on the board.

The algorithm explores possible future game states and assigns scores to terminal states:

| Result        | Score |
| ------------- | ----: |
| Human wins    | `+10` |
| Computer wins | `-10` |
| Draw          |   `0` |

The AI assumes that:

* The **maximizing player** tries to maximize the score.
* The **minimizing player** tries to minimize the score.

The algorithm recursively explores all possible moves:

```text
                    Current Board
                         |
          +--------------+--------------+
          |              |              |
        Move 1         Move 2         Move 3
          |              |              |
       Future         Future         Future
       states         states         states
          |              |              |
        ...            ...            ...
```

At every level:

```text
MAX → choose the highest score
MIN → choose the lowest score
```

This allows the computer to select the move that gives it the best possible outcome, assuming the opponent also plays optimally.

## Board Representation

The board is represented as a 2D Python list:

```python
board = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]
```

The symbols are:

* `.` → Empty cell
* `O` → Human player
* `X` → Computer

Coordinates are zero-indexed:

```text
      j
      0   1   2
    +---+---+---+
 i 0| . | . | . |
    +---+---+---+
 i 1| . | . | . |
    +---+---+---+
 i 2| . | . | . |
    +---+---+---+
```

For example:

```text
0 2
```

places the player's symbol at the top-right cell.

## Algorithm

### 1. Evaluate the Board

The `eval()` function checks whether either player has won.

It examines:

* 3 rows
* 3 columns
* 2 diagonals

The evaluation is:

```text
Human wins    → +10
Computer wins → -10
No winner     → 0
```

### 2. Check Available Moves

`is_moves_left()` checks whether any empty cells remain.

If there are no moves left and nobody has won, the game is a draw.

### 3. Minimax Search

The `minimax()` function recursively explores the game tree.

For the maximizing player:

```python
score = max(score, minimax(...))
```

For the minimizing player:

```python
score = min(score, minimax(...))
```

Each move is temporarily applied to the board and then undone after the recursive call:

```python
board[i][j] = player
score = minimax(board, False)
board[i][j] = '.'
```

This allows the same board to be reused while exploring different branches.

### 4. Find the Best Move

`find_best_move()` evaluates every available move and selects the one with the optimal Minimax score.

For the maximizing player:

```text
Choose move with maximum score
```

For the minimizing player:

```text
Choose move with minimum score
```

## Complexity

For a general game-tree search, Minimax has approximately:

```text
Time Complexity: O(b^d)
Space Complexity: O(d)
```

where:

* `b` = branching factor
* `d` = maximum depth of the game tree

For Tic-Tac-Toe:

```text
d ≤ 9
```

and the branching factor decreases as the game progresses.

Since Tic-Tac-Toe has a very small state space, exploring the complete game tree is practical.

## Running the Program

Make sure Python 3 is installed.

Run:

```bash
python tic_tac_toe.py
```

You will see:

```text
Move played by Human
Enter coordinates of move :
```

Enter the row and column of your desired move.

For example:

```text
0
1
```

places `O` at row `0`, column `1`.

The computer will then calculate its best move using Minimax.

## Example

A possible game state:

```text
O X .
. O .
X . .
```

The computer examines the available moves and recursively evaluates the resulting game states before selecting its move.

Eventually the game ends with either:

```text
HUMAN WON!
```

```text
COMPUTER WON!
```

or:

```text
GAME IS DRAWED
```

## Possible Improvements

The current implementation is intentionally simple and focuses on understanding Minimax. It can be extended with:

* **Alpha-Beta Pruning** to reduce unnecessary game-tree exploration
* Depth-based scoring so that the AI prefers winning sooner and losing later
* Randomization between equally optimal moves
* A better command-line interface
* Player selection (`X` or `O`)
* Human vs Human mode
* Difficulty levels
* GUI using Tkinter/Pygame
* Board-state caching using memoization
* Unit tests for the game logic

### Alpha-Beta Pruning

A major improvement would be adding **Alpha-Beta Pruning** to Minimax.

Instead of exploring every possible branch, Alpha-Beta Pruning eliminates branches that cannot influence the final decision.

This can significantly reduce the number of positions that need to be evaluated while producing the **same optimal move** as standard Minimax.

