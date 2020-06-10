from django import forms

from .models import attendance
from .models import Assignments
from .models import Timetable

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = attendance
        fields = ('title', 'DOU', 'File')

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ('Atitle', 'Asubject', 'ADOU', 'AFile')

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ('Ttitle', 'TFile')