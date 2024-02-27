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

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
