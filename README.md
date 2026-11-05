# Percentage Calculator

A simple, lightweight Python command-line utility to calculate percentages with custom ASCII art output.

## Installation

Ensure you have Python installed, then clone or download the script. No external dependencies are required.
```bash
git clone https://github.com/S4LMUN/Percentage.git
```

## Usage

Run the script from your terminal by passing two integer arguments: the **part** and the **base**.

```bash
python main.py <part> <base>
```

## Example

To calculate what percentage 25 is of 200:

```bash
python main.py 25 200
```

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/103faa6c-4864-408e-b695-f1218e049a0d" />

## Quick Access (Optional Alias)

To run the script from anywhere without typing `python` and the full file path every time, you can set up a shell alias.

## Setup

Add the following line to your shell configuration file (`~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`):

```bash
alias percent="python {path where you put it}/percentage/main.py"
```
