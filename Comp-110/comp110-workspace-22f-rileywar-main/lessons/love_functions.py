"""Some tender, loving functions."""

def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string"""
    return f"I love you {subject}!"

#print(love("Riley"))

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    hate: int = 0
    while hate < n:
        love_note += love(to) + "\n"
        hate += 1
    return love_note