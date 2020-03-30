from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Students, Teachers


def firstPageController(request):
    return HttpResponse('<h1>My first app django</h1>')


def indexPageController(request):
    return HttpResponse('<h1>This is index page</h1>')


def htmlPageController(request):
    return render(request, 'html_page.html')


def htmlPageWithDataController(request):
    context = {}

    context['data1'] = "This is data 1 passing to html page"
    context['data2'] = "This is data 2 passing to html page"

    return render(request, 'html_page_data.html', context)


def htmlWithDataPassController(request, url_data):
    return HttpResponse('<h1>This is index page : ' + url_data + '</h1>')


def addData(request):
    return render(request, 'add_data.html')


def add_student(request):
    if request.method != "POST":
        return HttpResponse('<h2>Method not Allowed</h2>')
    else:
        file = request.FILES['profile_image']
        fs = FileSystemStorage()
        profile_img = fs.save(file.name, file)
        try:
            student = Students(
                name=request.POST.get('name', ''),
                email=request.POST.get('email', ''),
                standard=request.POST.get('standard', ''),
                hobbies=request.POST.get('hobbies', ''),
                roll_no=request.POST.get('roll_no', ''),
                bio=request.POST.get('bio', ''),
                profile_image=profile_img,
            )
            student.save()
            messages.success(request, "Added Student Successfully!")
        except:
            messages.error(request, "Fail, An error occurred!")

        return HttpResponseRedirect("/addData")


def add_teacher(request):
    if request.method != "POST":
        return HttpResponse('<h2>Method not Allowed</h2>')
    else:
        try:
            teacher = Teachers(
                name=request.POST.get('name', ''),
                email=request.POST.get('email', ''),
                department=request.POST.get('department', ''),
            )
            teacher.save()
            messages.success(request, "Added Teacher Successfully!")
        except:
            messages.error(request, "Fail, An error occurred!")

        return HttpResponseRedirect("/addData")


def show_all_data(request):
    context = {}

    all_students = Students.objects.all()
    all_teachers = Teachers.objects.all()

    context['students'] = all_students
    context['teachers'] = all_teachers

    return render(request, 'show_data.html', context)


def update_student(request, student_id):
    student = Students.objects.get(id=student_id)
    if student == None:
        return HttpResponse('Student not found')
    else:
        return render(request, 'student_edit.html', {'student': student})


def delete_student(request, student_id):
    student = Students.objects.get(id=student_id)
    if student == None:
        return HttpResponse('Student not found')
    else:
        student.delete()
        messages.success(request, 'Deleted successfully')
        return HttpResponseRedirect('/show_all_data')

def edit_student(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method not Allowed</h2>')
    else:
        student = Students.objects.get(id=request.POST.get('id', ''))
        if student != None:
            if request.FILES.get('profile_image') != None:
                file = request.FILES['profile_image']
                fs = FileSystemStorage()
                profile_img = fs.save(file.name, file)
            else:
                profile_img = None

            if profile_img != None:
                student.profile_image = profile_img

            student.name = request.POST.get('name', '')
            student.email = request.POST.get('email', '')
            student.standard = request.POST.get('standard', '')
            student.hobbies = request.POST.get('hobbies', '')
            student.bio = request.POST.get('bio', '')
            student.save()

            messages.success(request, 'Updated successfully')
            return HttpResponseRedirect("update_student/"+str(student.id)+"")
        else:
            return HttpResponse('Student not found')


def update_teacher(request, teacher_id):
    teacher = Teachers.objects.get(id=teacher_id)
    if teacher == None:
        return HttpResponse('Student not found')
    else:
        return render(request, 'teacher_edit.html', {'teacher': teacher})


def delete_teacher(request, teacher_id):
    teacher = Teachers.objects.get(id=teacher_id)
    if teacher == None:
        return HttpResponse('Teacher not found')
    else:
        student.delete()
        messages.success(request, 'Deleted successfully')
        return HttpResponseRedirect('/show_all_data')

def edit_teacher(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method not Allowed</h2>')
    else:
        teacher = Teachers.objects.get(id=request.POST.get('id', ''))
        if teacher != None:
            teacher.name = request.POST.get('name', '')
            teacher.email = request.POST.get('email', '')
            teacher.deparment = request.POST.get('deparment', '')
            teacher.save()

            messages.success(request, 'Updated successfully')
            return HttpResponseRedirect("update_teacher/"+str(teacher.id)+"")
        else:
            return HttpResponse('Teacher not found')
