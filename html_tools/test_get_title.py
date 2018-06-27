#!/usr/bin/env python3
import html_tools as test

def test_get_title():
    # Test Simple Case
    assert "Hello, world!" == test.get_title("<title>Hello, world!</title>")

    # Test Nested
    assert "Hello, world!!" == test.get_title("<html><title>Hello, world!!</title></html>")

    # Test Unicode
    assert "HellØ, world." == test.get_title("<html><title>HellØ, world.</title></html>")

    # Test None
    assert None == test.get_title("Hello, world!")
