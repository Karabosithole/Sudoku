
# Sudoku

## Setting Up the Project

To ensure the project runs correctly with all its dependencies, follow the steps below to set up a virtual environment and install the required packages.

### 1. Clone the Repository  
First, clone the repository to your local machine:
```
git clone https://github.com/your-username/sudoku-game.git  
cd sudoku-game
```

### 2. Create a Virtual Environment  
In the project directory, create a virtual environment to isolate project dependencies:

- On macOS/Linux:
```
python3.12 -m venv venv
```
- On Windows:
```
python -m venv venv
```

### 3. Activate the Virtual Environment  
Activate the virtual environment to install packages locally:

- On macOS/Linux:
```
source venv/bin/activate
```
- On Windows:
```
venv\Scripts\activate
```

### 4. Install Dependencies  
Once the virtual environment is activated, install the required dependencies (like `pygame`):
```
pip install -r requirements.txt
```

If `requirements.txt` doesn’t exist, you can install Pygame directly:
```
pip install pygame
```

### 5. Running the Game  
With the dependencies installed, you can now run the Sudoku game:
```
python sudoku.py
```

### 6. Deactivate the Virtual Environment  
When finished, deactivate the virtual environment with:
```
deactivate
```
