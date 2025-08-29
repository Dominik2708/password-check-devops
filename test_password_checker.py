import pytest
from password_checker import is_valid_password

def test_too_short():
	assert not is_valid_password("Abc1")

def test_no_digit():
	assert not is_valid_password("Abcdefgh")

def test_no_lowercase():
	assert not is_valid_password("ABCDEFG1")

def test_no_uppercase():
	assert not is_valid_password("abcdefgh1")

def test_valid_password():
	assert is_valid_password("Abcdefg1")

	assert is_valid_password("A1bcdefg")

