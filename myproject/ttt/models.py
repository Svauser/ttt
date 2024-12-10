from django.db import models


class Task (models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    comleted=models.BooleanField(Default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

