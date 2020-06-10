from django.contrib import admin

from .models import Teaches
from .models import attendance
from .models import Assignments
from .models import Timetable
from .models import Faculty
from .models import Announcement

admin.site.register(Teaches)
admin.site.register(Timetable)
admin.site.register(attendance)
admin.site.register(Assignments)
admin.site.register(Faculty)
admin.site.register(Announcement)