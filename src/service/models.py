from django.db import models

from account.models import User


class Site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sites")
    name = models.CharField(max_length=255)
    url = models.URLField()
    visit_count = models.IntegerField(default=0)
    data_sent = models.BigIntegerField(default=0)
    data_received = models.BigIntegerField(default=0)

    def increment_visit_count(self):
        self.visit_count += 1
        self.save(update_fields=["visit_count"])

    def update_data_usage(self, sent, received):
        self.data_sent += sent
        self.data_received += received
        self.save(update_fields=["data_sent", "data_received"])
