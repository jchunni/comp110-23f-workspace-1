"""Quiz 2 practice."""

def value_exists(dict: dict[str, int], x: int) -> bool:
    """Determines if the variable x is in the dictionary."""
    exists: bool = False
    for key in dict:
        if dict[key] == x:
            exists = True
    return exists