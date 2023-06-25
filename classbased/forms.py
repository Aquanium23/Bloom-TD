from django import forms

class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=20)

class StudentForm(forms.Form):
    name = forms.CharField(max_length=20)