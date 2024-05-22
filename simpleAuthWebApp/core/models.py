from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40)
    timestamp = models.DateTimeField()
    body = models.TextField("Text")

    def __str__(self):
        return f"{self.title} - created on {self.timestamp}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=70)
    text = models.TextField("Text")

    def __str__(self):
        return f"{self.post} - commented by {self.author}"
