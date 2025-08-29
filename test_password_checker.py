import pytest
from password_checker import is_valid_password

def test_short():
	assert not is_valid_password("Abc1")

def test_digit():
	assert not is_valid_password("Abcdefgh")

def test_lower():
	assert not is_valid_password("ABCDEFG1")

def test_upper():
	assert not is_valid_password("abcdefgh1")

def test_valid():
	assert is_valid_password("Abcdefg1")
	assert is_valid_password("A1bcdefg")

