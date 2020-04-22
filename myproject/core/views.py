from django.shortcuts import render
from subject.models import Faculty, Subject
from django.db import connection


# Create your views here.


def listsubject(request):
    c = connection.cursor()
    sql = "select s.id,s.name,s.tc,t.type_name, f.name as faculty_name " \
          "from subject_subject s" \
          " join subject_faculty f  on f.id = s.faculty_id" \
          " join subject_typesub t on t.type_id = s.type_id" \
          " order by s.id asc"

    c.execute(sql)
    rows = c.fetchall()
    print(rows)
    return render(request, 'homepage/index.html', {
        'listSubject': rows
    })