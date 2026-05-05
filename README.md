
## 🚀 Project Overview

## 🎨 User Interface (The Designer)

The app is structured into three primary views using `VerticalArrangements`:

1.  **ViewCategory:** The landing screen where players select their field of study (Geography, Math, or Trivia).
2.  **ViewDifficulty:** A secondary selection screen to set the challenge level.
3.  **ViewGame:** The main arena containing:
    -   A 3x3 Grid of Buttons (`Btn1` through `Btn9`).
    -   A Turn Indicator Label (`LblTurn`).
    -   A Reset Button (`BtnReset`) and a Back Button (`BtnBack`).
    -   **Notifier1:** Used for the "Knowledge Gate" popup dialogs.

---

## 🧩 Block Logic (The Brain)

The project follows a modular programming approach using App Inventor's block system.

### Global Variables
- `turn`: Keeps track of whether it is 'X' or 'O''s turn.
- `selected_category` & `selected_difficulty`: Store the player's game preferences.
- `current_answer`: Stores the correct answer for the active question for validation.
- `pending_move`: Temporarily holds the ID of the button the player is trying to claim.

### Key Procedures
- **AskQuestion:** Uses conditional logic to pull a random question-answer pair from the selected category/difficulty lists.
- **HandleMove:** Triggered when a grid button is clicked. It locks the move and invokes the `AskQuestion` logic.
- **CheckWin:** A comprehensive check that runs after every successful move to see if a player has aligned three symbols or if the board is full (Tie).
- **ResetGame:** Clears the board, resets the turn to 'X', and returns all button text to placeholders.

### Event Handlers
- **AfterTextInput:** The most critical block. It compares the user's input with `current_answer` (case-insensitive).
    - *If Correct:* The square is claimed for the current player.
    - *If Incorrect:* The turn is forfeited and passed to the opponent.

---

