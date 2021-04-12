from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=350)
    content = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['title','content'], name="BlogPostBasicIndex"),
            models.Index(fields=['add_date'], condition=Q(add_date__gte='2021-01-01'), name="BlogDateInNewYearIndex")
        ]
