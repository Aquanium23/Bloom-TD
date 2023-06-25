from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, JsonResponse
from .models import Student, ClassRoom, StudentProfile


# Create your views here.

def test(request):
    # response = HttpResponse()
    html_content = """
    <html>
        <head>
            <title>Django Project</title>
        </head>
        <body>
            <h1>Django is a web framework.</h1>
        </body>
    </html>
    """
    # response.content = html_content
    # return response


# You can also use  return HttpResponse(html_content)

def view_name_bombastic(request):
    response = HttpResponse()
    html_content = """
        <html>
            <head>
                <title>Mr. Bombastic</title>
            </head>
            <body>
                <h1>She call me Mr. Bombastic,  tell me fantastic...</h1>
            </body>
        </html>
        """
    response.content = html_content
    return response


def view_name(request, name):
    last_name = request.GET.get('last_name')
    print(last_name)
    if name == 'harry':
        full_name = 'Harry Styles'
    elif name == 'john':
        full_name = 'John Pork'
    elif name == 'ram':
        full_name = 'Ram Bahadur'
    else:
        # return HttpResponse('<h1>Name not found</h1>', status=404)
        return HttpResponseNotFound('<h1>Name not found</h1>')
    context = {
        'name': full_name,
    }
    if last_name:
        context.update(last_name=last_name)
    return render(request, "myapp/name.html", context=context)


def view_name_ram(request, name):
    return render(request, "myapp/ram.html")


def json_view(request):
    response = {'id': 1, 'name': 'Tonzon', 'age': 19.4}
    students = [
        {'id': 1, 'name': 'Tonzon', 'age': 19.4},
        {'id': 2, 'name': 'Tonyzon', 'age': 14},
        {'id': 3, 'name': 'Tonzony', 'age': 12},
        {'id': 4, 'name': 'Toynyzony', 'age': 8},
    ]
    return JsonResponse(students, safe=False)


def index(request):
    # context={'id': 1, 'name': 'Tonzon', 'age': 28.3, 'title': 'Student' }
    context = {'students': [
        {'id': 1, 'name': 'Tonzon', 'age': 19.4, 'is_active': True},
        {'id': 2, 'name': 'Tonyzon', 'age': 14, 'is_active': False},
        {'id': 3, 'name': 'Tonzony', 'age': 12, 'is_active': True},
        {'id': 4, 'name': 'Toynyzony', 'age': 8, 'is_active': True},
    ], 'title': 'Student'}
    # context['students'] = ['students'][:3] Doesn't work ask abt this
    return render(request, template_name="myapp/index.html", context=context)


def student(request):
    context = {
        'title': 'Students',
        'classrooms': ClassRoom.objects.all(),
        'students': Student.objects.all(),
        'student_profiles': StudentProfile.objects.all()

    }
    return render(request, template_name='myapp/student.html', context=context)


for i in range(10):
    print(i)


def home(request):
    return render(request, 'myapp/portfolio.html')


def page1(request):
    return render(request, 'myapp/page1.html')


def page2(request):
    return render(request, 'myapp/page2.html')

def student_detail(request, id):
    context = {
        'student': Student.objects.get(id=id),
        'title': 'Student Detail'
    }
    return render(request, "myapp/student_detail.html", context=context)