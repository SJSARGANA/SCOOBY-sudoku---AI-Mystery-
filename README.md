# SCOOBY sudoku - AI Mystery Solver

Welcome to **SCOOBY sudoku**! This is a fun, vibrant, Scooby-Doo themed Sudoku solver built using Python. Underneath the colorful UI, it packs a powerful AI brain that solves Sudoku puzzles treating them as a **Constraint Satisfaction Problem (CSP)**.

Whether you want to play around with the interactive GUI or run bulk tests in the terminal, this detective tool is ready to solve any numerical mystery.

## Features

* **Colorful Scooby-Themed GUI:** Built with Tkinter, featuring vibrant Scooby colors (Orange, Blue, Mint Green).
* **Advanced AI Solver:** Uses **AC-3 (Arc Consistency)**, **Forward Checking**, and **Backtracking** algorithms to solve puzzles efficiently.
* **Detective Stats:** Tracks and displays performance metrics like the number of backtrack calls and failures.
* **Dual Modes:** Run it via the interactive Graphical User Interface (GUI) or the Command Line Interface (CLI).
* **Multiple Difficulties:** Comes with pre-loaded boards ranging from easy to evil.

## Project Structure

```text
SCOOBY-sudoku/
 |-- sudoku_boards/        # Text files containing different Sudoku puzzles
 |    |-- easy.txt
 |    |-- medium.txt
 |    |-- hard.txt
 |    |-- veryhard.txt
 |    |-- evil.txt
 |-- sudoku_gui.py         # The main GUI application (Run this for the visual app)
 |-- sudoku_io.py          # Helper functions for reading and formatting the board
 |-- sudoku_solver.py      # The core AI logic (AC-3, Domains, Backtracking)
 |-- q3_sudoku_csp.py      # CLI script for running the solver in the terminal
