import string


def are_strs_equal_ignoring_whitespace(str1: str | bytes, str2: str | bytes) -> bool:
    if isinstance(str1, bytes):
        str1 = str1.decode()
    if isinstance(str2, bytes):
        str2 = str2.decode()
    remove_whitespace = {ord(c): None for c in string.whitespace}
    return str1.translate(remove_whitespace) == str2.translate(remove_whitespace)
