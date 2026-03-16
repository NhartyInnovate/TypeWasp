# Disappearing Text Writing App

A Python desktop application that encourages continuous writing by deleting everything if the user stops typing.

This project was built as part of the **100 Days of Python Development challenge**.

## Project Idea

Writer's block is a common problem for many writers. One interesting solution is the concept of "dangerous writing", where the user must keep typing continuously. If they stop typing for too long, everything they've written disappears.

This application recreates that idea using **Python and Tkinter**.

If the user stops typing for more than **5 seconds**, all the text in the editor is automatically deleted.

## Features

- Desktop GUI built with Tkinter
- Live countdown timer
- Automatic text deletion if typing stops
- Word counter
- Character counter
- Reset timer option
- Clear text option
- Responsive writing editor

## How It Works

1. The user begins typing in the editor.
2. A countdown timer starts from **5 seconds**.
3. Each key press resets the timer.
4. If the user stops typing and the timer reaches **0**, all text is deleted.

This encourages the user to keep writing continuously without hesitation.

## Technologies Used

- Python
- Tkinter
- Python Standard Library

No external dependencies are required.

## Running the Application

Clone the repository:
