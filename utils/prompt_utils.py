def parse_prompt(raw_prompt):
    """
    Parses the raw user prompt to detect verbose flag and clean the prompt.

    Args:
        raw_prompt (str): The input string from the user.

    Returns:
        tuple: (prompt (str), verbose_flag (bool))
    """
    verbose_flag = False
    prompt = raw_prompt.strip()
    if prompt.endswith("--verbose"):
        verbose_flag = True
        prompt = prompt[:-9].strip()
    return prompt, verbose_flag
