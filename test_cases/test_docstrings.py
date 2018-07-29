import pytest


@pytest.mark.fast
class TestWithDocstring:
    """SUITE: Testing with docstring"""

    def test_method_with_docstring(self):
        """CASE-001: Test method with docstring"""
        pass

    def test_no_docstring(self):
        pass
