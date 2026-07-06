import os

def read_file(filepath: str) -> str:
    """Reads the source code from the given file path."""
    if not os.path.exists(filepath):
        return ""
    
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()