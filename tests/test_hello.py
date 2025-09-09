# test_hello.py
from hello import greet

def test_greet():
    assert greet("GitHub") == "Hello, GitHub!"
    assert greet("World") == "Hello, World!"
