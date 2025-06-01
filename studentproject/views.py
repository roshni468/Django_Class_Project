from django.shortcuts import render ,redirect

from myapp.models import*
def homepage(req):
    return render(req,"home.html")
def addstudent(req):
    if req.method=='POST':
        s_name=req.POST.get("studentName")
        d_name=req.POST.get("departmentName")
        c_name=req.POST.get("city")
        age=req.POST.get('age')
    
        student=student_from(
            name=s_name,
            department_name=d_name,
            city_name=c_name,
            age= age,

        )
        student.save()
        return redirect("list")

    
    return render(req,"addstudent.html")

def editstudent(req,myid):
    student=student_from.objects.get(id=myid)
    context={
        'data':student
    }
    if req.method=='POST':
        s_name=req.POST.get("studentName")
        d_name=req.POST.get("departmentName")
        c_name=req.POST.get("city")
        age=req.POST.get('age')
    
        student=student_from(
            id=myid,
            name=s_name,
            department_name=d_name,
            city_name=c_name,
            age= age,

        )
        student.save()
        return redirect("list")
    return render(req,"editstuent.html",context)

def list(req):
    s_list=student_from.objects.all()
    context={
        'data': s_list
    }
    
    return render(req,"studentlist.html",context)



def addtecher(req):
    if req.method=='POST':
        name=req.POST.get("id_number")
        d_name=req.POST.get("tacher_name")
        c_name=req.POST.get("city")
        age=req.POST.get("age")
    
        student=tacher_model(
            id_number=name,
            tacher_name=d_name,
            city_name=c_name,
            age= age,

      )
        student.save()
        return redirect("techerlist")

    return render(req,"addtecher.html")


def techerlist(req):
    s_list=tacher_model.objects.all()
    context={
        'data': s_list
    }
    
    return render(req,"techerlist.html",context)



def  addcourse(req):
    if req.method=='POST':
        s_name=req.POST.get("CSE")
        d_name=req.POST.get("math")
        c_name=req.POST.get("details")
        age=req.POST.get("fee")
    
        student=course_model(
            CSE=s_name,
            BBA=d_name,
            MATH=c_name,
            english= age,

        )
        student.save()
        return redirect("course_list")

    return render(req,"addcour.html")


def course_list(req):
    s_list=course_model.objects.all()
    context={
        'data': s_list
    }
    
    return render(req,"courselist.html",context)

def deletstudent(req,myid):
    student=student_from.objects.get(id=myid)

    student.delete()
    return redirect("list")


def deletteacher(req,myid):
    Teacher=tacher_model.objects.get(id=myid)

    Teacher.delete()
    return redirect("techerlist")


def deletcourse(req,myid):
    Teacher=course_model.objects.get(id=myid)

    Teacher.delete()
    return redirect("course_list")


def editcourse(req,myid):
    Teacher=course_model.objects.get(id=myid)

    context={
        'data':Teacher
    }
    if req.method=='POST':
        s_name=req.POST.get("CSE")
        d_name=req.POST.get("math")
        c_name=req.POST.get("details")
        age=req.POST.get("fee")
    
        student=course_model(
            id=myid,
            CSE=s_name,
            BBA=d_name,
            MATH=c_name,
            english= age,

        )
        student.save()
        return redirect("course_list")

   
    return render(req,"edit.html",context)