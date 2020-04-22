from django.shortcuts import render, redirect
from .models import Faculty, Subject
from django.db import connection


# Create your views here.
def formaddsubject(request):
    list = Faculty.objects.all()
    return render(request, 'addsubject/index.html', {
        'listFaculty': list
    })


def postaddsubject(request):
    fname = request.POST["name"]
    ftype = request.POST["type"]
    ffaculty = request.POST["faculty"]
    ftc = request.POST["tc"]
    obj = Subject(name=fname, type_id=ftype, tc=ftc, faculty_id=ffaculty)
    obj.save()
    return redirect('/')


def delsubject(request, subid):
    c = connection.cursor()
    sql = "delete from subject_subject where id = %s"
    c.execute(sql, (subid,))
    connection.commit()
    return redirect('/')