from collections import deque


def is_palindrome(word: str) -> bool:
    if len(word) < 2:
        return True

    container = deque(word.replace(" ", "").lower())
    left = container.popleft()
    right = container.pop()

    while left and right:
        if left != right:
            return False

        if len(container) < 2:
            return True

        left = container.popleft()
        right = container.pop()

    return True

if __name__ == "__main__":
    assert is_palindrome("")
    assert is_palindrome("a")
    assert is_palindrome("Aa")
    assert is_palindrome("aba")
    assert is_palindrome("abb  a")
    assert is_palindrome("abcba ")
    assert not is_palindrome("ab")
    assert not is_palindrome("abb")
    assert not is_palindrome("abca")
    assert not is_palindrome("abbca")
    print("Success!")
