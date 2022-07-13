from django.db import models

class Diary(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content