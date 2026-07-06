def get_ai_review(prompt: str) -> str:
    """
    Sends the prompt to the LLM API. 
    (Mocked here for the starter template).
    """
    # TODO: Replace with actual API call (e.g., openai.ChatCompletion.create)
    # Example mock response:
    mock_response = """
    **Bugs:** None detected.
    **Performance:** Consider using a list comprehension on line 12 for better speed.
    **Style:** Variable names could be more descriptive.
    """
    return mock_response.strip()