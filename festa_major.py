import datetime as dt


def first_sunday_of_august(year: int) -> dt.date:
    weekday_of_august_first = dt.date(year, 8, 1).isocalendar()[2]
    missing_days = 7 - weekday_of_august_first
    return dt.date(year, 8, 1 + missing_days)


def next_festa_major(date: dt.date) -> dt.date:
    this_years_festa_major = first_sunday_of_august(date.year)
    next_years_festa_major = first_sunday_of_august(date.year + 1)

    if date <= this_years_festa_major:
        return this_years_festa_major
    else:
        return next_years_festa_major


if __name__ == "__main__":
    today = dt.date.today()
    next_fm: dt.date = next_festa_major(today)
    print(f"Today is {today}. The next festa major will be on {next_fm}")
