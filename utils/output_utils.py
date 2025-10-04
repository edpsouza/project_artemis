def display_response(response, prompt, verbose):
    if verbose:
        print(f"\nUser prompt: {prompt}\n")
        print(response.text)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    else:
        print(response.text)
    print("-" * 40)
