import datetime
from django.db import models
from django.utils import timezone

from polls.utils import get_redis


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    @property
    def stats_votes(self):
        redis_value = get_redis().get(self.redis_key) or 0
        return int(redis_value)

    @property
    def redis_key(self):
        return "Choice%s" % self.id
