import datetime as dt

from hypothesis import given
import hypothesis.strategies as st

from festa_major import next_festa_major


dates = st.dates(max_value=dt.date(3000, 1, 1))


@given(dates)
def test_next_festa_major_is_after_given_date(date):
    assert date <= next_festa_major(date)


@given(dates)
def test_next_festa_major_is_earlier_than_370_days_away(date):
    assert (next_festa_major(date) - date).days <= 370


@given(dates)
def test_next_festa_major_is_in_august(date):
    assert next_festa_major(date).month == 8


@given(dates)
def test_next_festa_major_is_a_sunday(date):
    assert next_festa_major(date).isocalendar()[2] == 7


@given(dates)
def test_next_festa_major_in_first_seven_days_of_august(date):
    assert 1 <= next_festa_major(date).day <= 7


def test_next_festa_major_during_2021():
    assert next_festa_major(dt.date(2021, 3, 7)) == dt.date(2021, 8, 1)
    assert next_festa_major(dt.date(2021, 8, 15)) == dt.date(2022, 8, 7)


def test_next_festa_major_of_a_festa_major():
    next_date = dt.date(2022, 8, 7)
    assert next_festa_major(next_date) == next_date
