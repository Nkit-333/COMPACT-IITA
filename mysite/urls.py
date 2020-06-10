from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('accounts/', include('accounts.urls')),

    path('StudentDash',views.StudentDash,name='StudentDash'),
    path('StudentDash/student_profile', views.student_profile, name='student_profile'),
    path('StudentDash/view_Assignment', views.view_Assignment, name='view_Assignment'),
    path('StudentDash/view_timetable', views.view_timetable, name='view_timetable'),
    path('StudentDash/view_Attendance', views.view_Attendance, name='view_Attendance'),
    path('StudentDash/view_Announcement', views.view_Announcement, name='view_Announcement'),
    
    path('facultyDash',views.facultyDash,name='facultyDash'),
    path('facultyDash/faculty_profile', views.faculty_profile, name='faculty_profile'),
    path('facultyDash/update_Assignment', views.update_Assignment, name='update_Assignment'),
    path('facultyDash/update_timetable', views.update_timetable, name='update_timetable'),
    path('facultyDash/update_exam_schedule', views.update_exam_schedule, name='update_exam_schedule'),
    path('facultyDash/Attendance', views.Attendance, name='Attendance'),
    path('facultyDash/Announcement', views.Announcement, name='Announcement'),

    path('facultyDash/Attendance/upload/', views.upload_Attendance, name = 'upload'),
    path('facultyDash/Attendance/<int:pk>', views.delete_list, name = 'delete_list'),

    path('facultyDash/update_Assignment/upload/', views.upload_Assignment, name = 'upload_Assignment'),
    path('facultyDash/update_Assignment/<int:pk>', views.delete_Assignment, name = 'delete_Assignment'),

    path('facultyDash/update_timetable/upload/', views.upload_timetable, name = 'upload_timetable'),
    path('facultyDash/update_timetable/<int:pk>', views.delete_timetable, name = 'delete_timetable'),

    path('FAQ', views.FAQ, name='FAQ')
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)