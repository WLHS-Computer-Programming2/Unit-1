# Tic-Tac-Toe Game Assignment

## Assignment Description
Your task is to create a **Tic-Tac-Toe** game using **2D lists** in Python. The game should allow two players to take turns marking **X** and **O** on a **3x3 board** until one player wins or the game results in a draw.

## Requirements
1. **Create and display the board**: Use a 3x3 **2D list** to represent the game board and display it after every turn. Using a fuction to print the state of the board.
2. **Player input**: Allow two players to take turns choosing their move.
3. **Input validation**: Ensure that the chosen cell is empty before marking it.
4. **Input validation**: Ensure that the using is entering only X and O.
5. **Check for a winner**: Implement a function to determine if a player has won.
6. **Check for a draw**: If all spaces are filled and no winner is found, the game ends in a draw.
7. **End game**: Display the winner or announce a draw, then ask if players want to play again.
8. **Partner**: You will work with 1 other person on this project and you should use GitHub to collaborate.
9. **Testing**: You will test your code with 1 other *group* to test your code and improve your game.

## Bonus Challenges (Optional, after all other requirements are met)
- Implement an **AI opponent** for single-player mode.
- Allow the user to **choose board size (NxN)**.
- Add a graphical interface using `turtle` or `tkinter`.

## Rubric (Total: 20 Points)

| Criteria               | 5 Points | 4 Points | 3 Points | 2 Points | 0-1 Points |
|------------------------|----------|----------|----------|----------|------------|
| **Board Representation** | Uses a 2D list and properly updates/display the board. | Minor display or update issues. | Board updates but formatting is unclear. | Board is not properly represented as a 2D list. | No board or incorrect structure. |
| **Player Input Handling** | Correctly allows players to take turns and choose valid positions. | Minor issues with input validation. | Some invalid inputs cause errors. | Significant input handling errors. | No player input handling. |
| **Win Condition Check** | Accurately determines the winner. | Mostly works but fails in some cases. | Checks for a win but is not reliable. | Major issues in determining the winner. | No win-checking logic. |
| **Draw Condition Check** | Correctly detects and announces a draw. | Works but does not handle some cases. | Attempts to check but is unreliable. | Fails to properly detect a draw. | No draw detection. |
| **Code Readability & Comments** | Well-structured, easy to read, and commented. | Mostly clear, minor missing comments. | Somewhat readable but needs improvements. | Hard to follow, minimal comments. | Poorly structured and unreadable. |