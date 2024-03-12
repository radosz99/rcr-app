import random
import string
from itertools import product

import pytest

from app.utils import get_path, create_tree_from_commands


def generate_random_string(length: int = 4):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


commands_number = [1, 5, 10, 100, 1000]
logs_number = [1, 1000, 10000]


def test_from_pdf():
    commands = ["LEFT", "GRAB", "LEFT", "BACK", "LEFT", "BACK", "LEFT"]
    root = create_tree_from_commands(commands)
    assert get_path(root, "LEFT") == "1"
    assert get_path(root, "GRAB") == "00"
    assert get_path(root, "BACK") == "01"


@pytest.mark.parametrize("commands,logs", product(commands_number, logs_number))
def test_random_commands(commands, logs):
    commands_list = [generate_random_string() for _ in range(commands)]
    random_list = [random.choice(commands_list) for _ in range(logs)]
    root = create_tree_from_commands(random_list)
    for command in commands_list:
        assert get_path(root, command) is not None