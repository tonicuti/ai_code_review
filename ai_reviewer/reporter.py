def format_report(raw_response: str) -> str:
    """
    Parses and formats the AI's output.
    Later, you can use the 'rich' library to add colors and syntax highlighting!
    """
    # For now, we just pass it through, but this is where you'd parse JSON or Markdown
    formatted = raw_response.replace("**", "") # Stripping bold for basic terminals
    return formatted