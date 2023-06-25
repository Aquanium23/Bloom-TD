from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from myapp.models import ClassRoom, Student
from .forms import ClassRoomForm, StudentForm


class FirstView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'classbased/first.html')

    def post(self, request, *args, **kwargs):
        pass


class ClassRoomView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Classroom',
            'classrooms': ClassRoom.objects.all()
        }
        return render(request, "classbased/classroom.html", context=context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("class_name")
        ClassRoom.objects.create(name=name)
        return redirect('crud_classroom')


class ClassRoomTemplateView(TemplateView):
    template_name = "classbased/classroom.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Classroom',
            'classrooms': ClassRoom.objects.all()
        })
        return context


class StudentListView(ListView):
    # model = Student
    template_name = 'classbased/student.html'
    context_object_name = 'students'
    queryset = Student.objects.filter(name__istartswith='z')


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'classbased/student_deatil.html'


class ClassRoomFormView(CreateView):
    pass


def classroom_form(request):
    if request.method == 'POST':
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            ClassRoom.objects.create(name=name)

        return redirect('classroom_form')

    context = {
        "title": "Classroom Form",
        'form': ClassRoomForm(),
        "classrooms": ClassRoom.objects.all()
    }
    return render(request, 'classbased/classroom_form.html', context=context)

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            Student.objects.create(name=name)

        return redirect('student_form')

    context = {
        "title": "Student Form",
        'form': StudentForm(),
        "students": Student.objects.all()
    }
    return render(request, 'classbased/student_form.html', context=context)