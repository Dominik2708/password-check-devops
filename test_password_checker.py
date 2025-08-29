from password_checker import is_valid_password

def test_short():
	assert not is_valid_password("Mn2")

def test_digit():
	assert not is_valid_password("Kmdhfh")

def test_lower():
	assert not is_valid_password("HALLO3")

def test_upper():
	assert not is_valid_password("testing323")

def test_valid():
	assert is_valid_password("ValidesPasswort123")
	assert is_valid_password("2TESvalidesPasswort")

