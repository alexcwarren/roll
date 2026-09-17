from roll import validate_format


def test_validate_format_accepts_valid_dice():
    assert validate_format("2d20") == (True, 2, 20)


def test_validate_format_rejects_invalid_text():
    is_valid, num_dice, die_type = validate_format("nonsense")

    assert is_valid is False
    assert num_dice is None
    assert die_type is None


def test_validate_format_rejects_missing_count():
    assert validate_format("d20") == (False, None, None)


def test_validate_format_rejects_missing_die_type():
    assert validate_format("2d") == (False, None, None)


def test_validate_format_rejects_unsupported_die():
    assert validate_format("2d100") == (False, None, None)


def test_validate_format_rejects_trailing_characters():
    assert validate_format("2d20abc") == (False, None, None)
