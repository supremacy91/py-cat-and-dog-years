from app import main


def test_should_return_zero_when_age_less_than_fifteen() -> None:
    assert main.get_human_age(14, 14) == [0, 0]


def test_should_return_one_human_year_after_fifteen_pet_years() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_should_return_one_human_year_until_twenty_three_pet_years() -> None:
    assert main.get_human_age(23, 23) == [1, 1]


def test_should_return_two_human_years_after_twenty_four_pet_years() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_should_convert_cat_and_dog_years_correctly_after_twenty_four() \
        -> None:
    assert main.get_human_age(28, 28) == [3, 2]


def test_should_convert_large_ages_correctly() -> None:
    assert main.get_human_age(100, 100) == [21, 17]
