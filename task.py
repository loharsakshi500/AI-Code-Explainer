from agent import explain_code


def explain_code_task(code):
    """
    Processes the user's code and gets the AI explanation.
    """

    if not code.strip():
        return "Please enter some code to explain."

    try:
        explanation = explain_code(code)
        return explanation

    except Exception as e:
        return f"An error occurred: {str(e)}"