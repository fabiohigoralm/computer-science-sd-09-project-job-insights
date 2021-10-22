from src.sorting import sort_by


ITEM_1 = {
    "max_salary": 5000,
    "min_salary": 1000,
    "date_posted": "2016-01-05"
}

ITEM_2 = {
    "max_salary": 6000,
    "min_salary": 1200,
    "date_posted": "2013-02-12"
}

ITEM_3 = {
    "max_salary": 7000,
    "min_salary": 1400,
    "date_posted": "2021-06-04"
}


def test_sort_by_criteria():
    jobs_mock = [ITEM_3, ITEM_2, ITEM_1]

    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == [ITEM_1, ITEM_2, ITEM_3]

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == [ITEM_3, ITEM_2, ITEM_1]

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == [ITEM_3, ITEM_1, ITEM_2]
