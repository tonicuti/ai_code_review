def analyze_code(code: str) -> dict:
    """Extracts basic metadata to help the AI understand the code."""
    lines = code.split('\n')
    return {
        "line_count": len(lines),
        "language": "python", # You can make this dynamic later based on file extension
        "has_classes": "class " in code,
        "has_functions": "def " in code
    }