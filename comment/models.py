from django.db import models
from person.models import Person
from item.models import Item
from home.models import MyUser
# Create your models here.


class PersonComment(models.Model):
    message = models.TextField(max_length=4000)
    image = models.FileField(blank=True, null=True)
    person = models.ForeignKey(Person, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(MyUser, related_name='person_comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by.username


class PersonReplayComment(models.Model):
    message = models.TextField(max_length=4000)
    image = models.FileField(blank=True, null=True)
    reply = models.ForeignKey(PersonComment, related_name='reply', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(MyUser, related_name='person_replies', on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by.username


class ItemComment(models.Model):
    message = models.TextField(max_length=4000)
    image = models.FileField(blank=True, null=True)
    item = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(MyUser, related_name='item_comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by.username


class ItemReplayComment(models.Model):
    message = models.TextField(max_length=4000)
    image = models.FileField(blank=True, null=True)
    reply = models.ForeignKey(ItemComment, related_name='reply', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(MyUser, related_name='item_replies', on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by.username