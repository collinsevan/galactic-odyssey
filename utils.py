import textwrap

def format_output(text, width=50):
    """
    Formats the provided text to wrap at a specified width.

    Args:
        text (str): The text to be formatted.
        width (int): The maximum width of each line.

    Returns:
        str: The formatted text with line breaks.
    """
    return textwrap.fill(text, width=width)