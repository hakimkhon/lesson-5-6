from django.db import models


class Woman(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)
    published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name