from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Home.html')
def about(request):
    return render(request,'About.html')
def contact(request):
    return render(request,'Contact.html')
def student(request):
    student_list = [
        {"name":"Rohit1","class":"10th"},
        {"name":"Rohit2","class":"10th"},
        {"name":"Rohit3","class":"10th"},
        {"name":"Mohit","class":"9th"},
        {"name":"Yash","class":"9th"},
        {"name":"Vaibhav","class":"9th"},
        {"name":"Sohit","class":"8th"},
        {"name":"Sakshi","class":"8th"}
    ]
    return render(request,'Student.html',{'students':student_list})
def mark(request):
    total = None
    if request.method == "POST":
        s1 = int(request.POST.get("subject1") or 0)
        s2 = int(request.POST.get("subject2") or 0)
        s3 = int(request.POST.get("subject3") or 0)
        s4 = int(request.POST.get("subject4") or 0)
        s5 = int(request.POST.get("subject5") or 0)
        total = s1+s2+s3+s5+s4
    
    return render(request,'Mark.html',{'total':total})
def gallery(request):
    return render(request,'Gallery.html')
