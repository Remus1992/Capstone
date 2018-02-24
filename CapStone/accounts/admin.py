from django.contrib import admin
from accounts.models import *

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(Equipment)
admin.site.register(Project)
admin.site.register(Cast)
admin.site.register(Crew)
admin.site.register(Message)