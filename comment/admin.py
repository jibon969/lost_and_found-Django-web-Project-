from django.contrib import admin
from .models import ItemComment, ItemReplayComment
from .models import PersonComment, PersonReplayComment

# Register your models here.

admin.site.register(ItemComment)
admin.site.register(ItemReplayComment)
admin.site.register(PersonComment)
admin.site.register(PersonReplayComment)
