from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    all_jobs = read(path)
    select_jobs = [job['job_type'] for job in all_jobs]
    no_repeat = set(select_jobs)

    return no_repeat


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    select_jobs = [job for job in jobs if job['job_type'] == job_type]

    return select_jobs


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    all_industry = read(path)
    select_industry = [industry['industry'] for industry in all_industry]
    no_repeat = set(filter(None, select_industry))
    return no_repeat


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    select_industry = [job for job in jobs if job['industry'] == industry]

    return select_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    all_salary = read(path)
    select_salary = [
        int(salary['max_salary'])
        for salary in all_salary if salary["max_salary"].isnumeric()
    ]
    no_repeat = set(filter(None, select_salary))
    return max(no_repeat)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    all_salary = read(path)
    select_salary = [
        int(salary['min_salary'])
        for salary in all_salary if salary["min_salary"].isnumeric()
    ]
    no_repeat = set(filter(None, select_salary))
    return min(no_repeat)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("job[min_salary] or job[max_salary] doesn't exists")
    elif (type(job["min_salary"]) is not int or
            type(job["max_salary"]) is not int):
        raise ValueError(
            "job[min_salary] or job[max_salary] aren't valid integers"
            )
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("job[min_salary] is greather than job[max_salary]")
    elif type(salary) is not int:
        raise ValueError("salary` isn't a valid integer")
    else:
        return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    list_salary = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                list_salary.append(job)
        except ValueError:
            continue

    return list_salary
