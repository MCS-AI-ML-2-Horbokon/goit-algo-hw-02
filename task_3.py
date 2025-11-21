from collections import deque


braces = {
    "(": ")",
    "[": "]",
    "{": "}"
}

braces_inv = { v: k for k, v in braces.items() }

def is_symmetrical(text: str):
    stack = deque()
    for c in text:
        if c in braces:
            stack.append(c)
            continue

        brace_closed = braces_inv.get(c)
        if brace_closed:
            if len(stack) == 0:
                return False

            brace_to_close = stack.pop()
            if brace_closed != brace_to_close:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    assert is_symmetrical("")
    assert is_symmetrical("()")
    assert is_symmetrical("( ){[ 1 ]( 1 + 3 )( ){ }}")
    assert not is_symmetrical("(")
    assert not is_symmetrical("())")
    assert not is_symmetrical(")")
    assert not is_symmetrical("(()")
    assert not is_symmetrical("( 23 ( 2 - 3);")
    assert not is_symmetrical("( 11 }")
    print("Success!")
