from django.contrib import admin
from .models import user_mapping,Questions,Question_vote
# Register your models here.

admin.site.register(user_mapping)
admin.site.register(Questions)
admin.site.register(Question_vote)