import uuid
import time
import datetime
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.FloatField(default=time.time)
    date_created = models.DateTimeField(default=datetime.datetime.utcnow)
    wallet_address = models.CharField(max_length=1024, null=False)


class BuyHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buy_history_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.FloatField(default=time.time)
    date_created = models.DateTimeField(default=datetime.datetime.utcnow)
    amount_bnb = models.IntegerField(null=False)
    is_complete = models.BooleanField(default=False)
    note = models.CharField(max_length=1024, null=True)

    def check_time_over(self):
        now = time.time()
        time_over = now - self.created_at
        return time_over

    def is_complete_task(self):
        time_over = self.check_time_over()
        day_over = time_over / (24 * 60 * 60)
        if self.is_complete:
            return True
        if day_over > 90:
            self.is_complete = True
            self.save()
            return True
        return False

    def get_date_started(self):
        return self.date_created

    def get_date_finished(self):
        return sefl.date_created + datetime.timedelta(days=90)

    def get_program_type(self):
        if 0.1 <= self.amount_bnb <= 1:
            return 1
        elif 1 < self.amount_bnb <= 3:
            return 2
        elif 3 < self.amount_bnb <= 10:
            return 3
        else:
            return 4
