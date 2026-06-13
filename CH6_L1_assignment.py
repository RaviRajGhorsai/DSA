"""

Implement the count_marketers function. It should accept a list of strings (job titles) and return the number of users who've set their title to "marketer". LockedIn users sometimes use different casing in their titles, so make sure to account for that.

"""

def count_marketers(job_titles: list[str]) -> int:
    count = 0

    for job_title in job_titles:
        if job_title.lower() == "marketer":
            count += 1

    return count
