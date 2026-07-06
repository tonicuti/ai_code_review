def build_prompt(code: str, analysis: dict) -> str:
    """Combines system instructions with the user's code."""
    system_instruction = (
        "You are an expert Senior Software Engineer. Review the following code "
        "for bugs, performance issues, and stylistic improvements. "
        "Keep your feedback concise and structured."
    )
    
    context = (
        f"File Context: {analysis['language']} file with {analysis['line_count']} lines.\n\n"
        f"Code to review:\n```\n{code}\n```"
    )
    
    return f"{system_instruction}\n\n{context}"