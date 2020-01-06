from notification.events import KukupaNotificationType


class NotificationCounter:
    def __init__(self):
        self.notification_total = 0
        self.kukupa_event = KukupaNotificationType()

    def filterNotificationByEvent(self, data):
        # Cerebro Pipeline counter
        if data['event'] == 'cerebro.pipeline.executing':
            self.kukupa_event.count_pipeline_executing += 1
        if data['event'] == 'cerebro.pipeline.canceled':
            self.kukupa_event.count_pipeline_canceled += 1
        if data['event'] == 'cerebro.pipeline.restarting':
            self.kukupa_event.count_pipeline_restarting += 1
        if data['event'] == 'cerebro.pipeline.killed':
            self.kukupa_event.count_pipeline_killed += 1
        if data['event'] == 'cerebro.pipeline.success':
            self.kukupa_event.count_pipeline_success += 1
        if data['event'] == 'cerebro.pipeline.error':
            self.kukupa_event.count_pipeline_error += 1
        # Cerebro Jobs counter
        if data['event'] == 'cerebro.job.executing':
            self.kukupa_event.count_job_executing += 1
        if data['event'] == 'cerebro.job.canceled':
            self.kukupa_event.count_job_canceled += 1
        if data['event'] == 'cerebro.job.restarting':
            self.kukupa_event.count_job_restarting += 1
        if data['event'] == 'cerebro.job.killed':
            self.kukupa_event.count_job_killed += 1
        if data['event'] == 'cerebro.job.success':
            self.kukupa_event.count_job_success += 1
        if data['event'] == 'cerebro.job.error':
            self.kukupa_event.count_job_error += 1
        # Expand with Hydra notifications here

        self.notification_total = (self.kukupa_event.count_pipeline_executing +
                                   self.kukupa_event.count_pipeline_canceled +
                                   self.kukupa_event.count_pipeline_restarting +
                                   self.kukupa_event.count_pipeline_killed +
                                   self.kukupa_event.count_pipeline_success +
                                   self.kukupa_event.count_pipeline_error +
                                   self.kukupa_event.count_job_executing +
                                   self.kukupa_event.count_job_canceled +
                                   self.kukupa_event.count_job_restarting +
                                   self.kukupa_event.count_job_killed +
                                   self.kukupa_event.count_job_success +
                                   self.kukupa_event.count_job_error)
