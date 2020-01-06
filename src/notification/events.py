# add classes for product events here

class KukupaNotificationType:
    def __init__(self):
        # Pipeline events
        self.count_pipeline_executing = 0
        self.count_pipeline_canceled = 0
        self.count_pipeline_restarting = 0
        self.count_pipeline_killed = 0
        self.count_pipeline_success = 0
        self.count_pipeline_error = 0
        # Job events
        self.count_job_executing = 0
        self.count_job_canceled = 0
        self.count_job_restarting = 0
        self.count_job_killed = 0
        self.count_job_success = 0
        self.count_job_error = 0
