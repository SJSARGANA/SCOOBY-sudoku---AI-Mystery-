from __future__ import annotations
import sys
from sudoku_io import board_to_string, read_board
from sudoku_solver import solve_board

def main() -> None:
    print("\n" + "*" * 60)
    print(" " * 15 + "🔍 SCOOBY SUDOKU - MYSTERY SOLVER 🔍")
    print("*" * 60)

    if len(sys.argv) < 2:
        file_paths = ["sudoku_boards/easy.txt"]
        print("Mystery Alert: No input file provided. Defaulting to: easy.txt")
    else:
        file_paths = sys.argv[1:]

    for file_path in file_paths:
        print("\n" + "-" * 40)
        print(f"🕵️ Searching in: {file_path}")
        
        try:
            board = read_board(file_path)
            solved, stats = solve_board(board)

            if solved is None:
                print("❌ Zoinks! The mystery couldn't be solved. No solution found.")
            else:
                print("✅ Mystery Solved! Here is the board:")
                print(board_to_string(solved))

            print("\n📊 Detective Stats:")
            print(f"   - Backtrack Calls: {stats.backtrack_calls}")
            print(f"   - Backtrack Failures: {stats.backtrack_failures}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

    print("\n" + "*" * 60)

if __name__ == "__main__":
    main()
