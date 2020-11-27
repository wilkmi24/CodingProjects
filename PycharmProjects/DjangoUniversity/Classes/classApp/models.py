from django.db import models


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="",blank=True, null=False)
    Course = models.IntegerField(blank=True, null=True)
    Instructor = models.CharField(max_length=60, default="",blank=True, null=False)
    Duration = models.FloatField(default="",blank=False, null=False)


    objects = models.Manager()
    def __str__(self):
        return self.Title

