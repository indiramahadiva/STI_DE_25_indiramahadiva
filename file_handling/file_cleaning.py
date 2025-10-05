from pathlib import Path

data_directory = Path(__file__).parent / "data" 

with open(data_directory / "quotes.txt") as file:
    print(file.read())