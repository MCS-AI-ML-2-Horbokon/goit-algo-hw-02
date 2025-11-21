from collections import deque


def is_palindrome(word: str) -> bool:
    if len(word) < 2:
        return True

    container = deque(word)
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
    assert is_palindrome("aa")
    assert is_palindrome("aba")
    assert is_palindrome("abba")
    assert is_palindrome("abcba")
    assert not is_palindrome("ab")
    assert not is_palindrome("abb")
    assert not is_palindrome("abca")
    assert not is_palindrome("abbca")
    print("Success!")
