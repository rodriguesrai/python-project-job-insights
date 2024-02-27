from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict[str, str]]:
        with open(path, "r") as file:
            csv_reader = csv.DictReader(file)
            self.jobs_list = list(csv_reader)

        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = []
        for job in self.jobs_list:
            if job["job_type"] not in unique_job_types:
                unique_job_types.append(job["job_type"])

        return unique_job_types

    def filter_by_multiple_criteria(self, jobs, filter_criteria) -> List[dict]:
        filtered_jobs = []
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria must be a dictionary")
        for job in jobs:
            if (
                job["job_type"] == filter_criteria["job_type"]
                and job["industry"] == filter_criteria["industry"]
            ):
                filtered_jobs.append(job)
        return filtered_jobs
