from django.db import models

class Teaches(models.Model):
    ProfID = models.CharField(max_length = 15)
    CourseID = models.CharField(max_length = 20)

    def __str__(self):
        return self.ProfID + ' - ' + self.CourseID

class Faculty(models.Model):
    ProfID = models.CharField(max_length = 15)
    CourseID = models.CharField(max_length = 20)

    def __str__(self):
        return self.ProfID + ' - ' + self.CourseID

class Announcement(models.Model):
    Time = models.CharField(max_length = 20)
    Date = models.CharField(max_length = 20, default='DEFAULT VALUE')
    Name = models.CharField(max_length = 25)
    Anno = models.CharField(max_length = 400)

    def __str__(self):
        return self.Date + ' - ' + self.Time + ' - ' + self.Name

class attendance(models.Model):
    title = models.CharField(max_length = 100)
    DOU = models.CharField(max_length = 100)
    File = models.FileField(upload_to='Attendance')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.File.delete()
        super().delete(*args, **kwargs)

class Assignments(models.Model):
    Atitle = models.CharField(max_length = 100)
    Asubject = models.CharField(max_length = 100)
    ADOU = models.CharField(max_length = 100)
    AFile = models.FileField(upload_to='Assignment')

    def __str__(self):
        return self.Atitle

    def delete(self, *args, **kwargs):
        self.AFile.delete()
        super().delete(*args, **kwargs)

class Timetable(models.Model):
    Ttitle = models.CharField(max_length = 100)
    TFile = models.FileField(upload_to='Timetable')

    def __str__(self):
        return self.Ttitle

    def delete(self, *args, **kwargs):
        self.TFile.delete()
        super().delete(*args, **kwargs)