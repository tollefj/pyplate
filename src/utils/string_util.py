def remove_whitespace(text):
    return "".join(text.split())


def replace_whitespace(text, replacement=" "):
    return replacement.join(text.split())


def truncate_string(text, max_length, ellipsis="..."):
    return text[:max_length] + (ellipsis if len(text) > max_length else "")
