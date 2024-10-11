"""Pytest fixture definitions.

To use pytest_plugins this conftest files needs to be in the root folder.
See here for more info:
https://docs.pytest.org/en/stable/deprecations.html#pytest-plugins-in-non-top-level-conftest-files
"""

pytest_plugins = [
    "tests.fixtures.clients",
]
