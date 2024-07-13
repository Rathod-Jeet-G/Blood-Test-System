import datetime
from django.shortcuts import render,redirect
from django.utils.dateparse import parse_datetime
from .models import UserRegister,Userfeedback
from laboratoryapp.models import Test_category,Name_category,Appointment
from laboratoryapp.forms import appointmentform


def login(request):
    if request.POST:
        email = request.POST['email']
        passwrod = request.POST['password']
        try:
            validate = UserRegister.objects.get(uid=email,userpwd=passwrod)
            if validate:
                request.session['user'] = email
                request.session['userId'] = validate.pk
                return redirect('user:home')
            else:
                return render(request,'login.html',{'error':'Password incorrect'})
        except:
            return render(request,'login.html',{'error':'Password incorrect'})
    return render(request,'login.html')
# signup api
def signup(request):
    if request.method == "POST":
        email = request.POST.get('email') 
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        age = int(request.POST.get('user_age'))
        gender = request.POST.get('usergender')
        useraddress = request.POST.get('useraddress')
        usercity = request.POST.get('usercity')
        userarea = request.POST.get('userarea')
        userpincode = int(request.POST.get('userpincode'))
        usercontactno = request.POST.get('usercontactno')

        if len(password)<8:
            return render(request,'signup.html',{'password_error':'password must be grater than 8 character'})
        if not any(c.isnumeric() for c in password) and not any(not c.isalnum() for c in password):
            return render(request,'signup.html',{'password_error':'Password must contain at least one number and one special character'})
    
        if not any(c.isnumeric() for c in password):
            return render(request,'signup.html',{'password_error':'Password must contain at least one number'})
    
        if not any(not c.isalnum() for c in password):
            return render(request,'signup.html',{'password_error':'Password must contain at least one special character'})
        if len(usercontactno) != 10:
            return render(request,'signup.html',{'password_error':'phone number contain 10 digit'})
        new_user = UserRegister(
            uid=email,
            userpwd=password,
            userfname=fname,
            usermname=mname,
            userlname=lname,
            user_age=age,
            usergender=gender,
            useraddress=useraddress,
            usercity=usercity,
            userarea=userarea,
            userpincode=userpincode,
            usercontactno=usercontactno
        )
        data = UserRegister.objects.filter(uid=email)
        if len(data)<=0:
            new_user.save()
            return render(request,'signup.html',{'sucessmessage':'Registration sucessfully'})
        else:
            return render(request,'signup.html',{'messagekey':"User Already Exists"})
    return render(request,'signup.html')

def home(request):
    user = request.session.get('user')
    if user:
        userid = UserRegister.objects.get(id=request.session['userId'])
        test_details = Test_category.objects.filter(email = request.session['user'])
        return render(request,'home.html',{'userid':userid,'test_details':test_details})
    return redirect('user:login')
def user_profile(request):
    user = request.session.get('user')
    if user:
        obj = UserRegister.objects.get(id=request.session['userId'])
        if request.POST:
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['passowrd']
            obj.userfname=name
            obj.uid=email
            obj.userpwd=password
            obj.save()
            return redirect('user:home')
        return render(request,'user_profile.html',{'n':obj})
    else:
        return redirect('user:login')

def book_appointment(request):
    user = request.session.get('user')
    if user:
        obj_test_name_category = Name_category.objects.all()
        userid = UserRegister.objects.get(id=request.session['userId'])
        form = appointmentform(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                c = Appointment.objects.filter(email=request.POST['email']) and Appointment.objects.filter(status='pending')
                if len(c) <= 0:
                    cdate = datetime.datetime.today()
                    postDate = request.POST['schedule']
                    # print(postDate)
                    postDateArray = postDate.split("T")
                    cDateArray = str(cdate).split(" ")
                    if parse_datetime(postDateArray[0]) >= parse_datetime(cDateArray[0]):
                        form.save()
                        return render(request, 'book_appointment.html', {'form':form,'msg': 'Your Appointment booked successfully', 'form': form, 'ab': obj_test_name_category, 'b': userid})
                    else:
                        return render(request, 'book_appointment.html', {'form':form,'ab': obj_test_name_category, 'b': userid, 'm': 'Select future date only'})
                else:
                    return render(request, 'book_appointment.html', {'form':form,'ab': obj_test_name_category, 'b': userid, 'm': 'Appointment already exists'})
        return render(request, 'book_appointment.html', {'form':form,'ab': obj_test_name_category, 'b': userid})
    return redirect('user:login')    

def user_feedback(request):
    user = request.session.get('user')
    if user:
        userid = UserRegister.objects.get(id = request.session['userId'])
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            Feedback = request.POST.get('Feedback')
            obj = Userfeedback()
            obj.username = name
            obj.useremail = email
            obj.feedback = Feedback
            obj.save()
            return redirect('user:home')
        return render(request,'user_feedback.html',{'userid':userid})
    else:
        return redirect('user:login')
def delete_appointment(request,id):
    user = request.session.get('user')
  
    if user:
        obj = Appointment.objects.get(pk=id)
        obj.delete()
        return redirect('user:view appointment')
    return redirect('user:login')
def view_test(request,id):
    user = request.session.get('user')
    if user:
        b = Test_category.objects.get(pk=id)
        c = UserRegister.objects.get(uid=b.email)
        return render(request,'report_table.html',{'b':b,'c':c})
    return redirect('user:login')

def view_appointment(request):
    user = request.session.get('user')
    if user:
        appoi_info = Appointment.objects.filter(email=request.session['user'])
        return render(request,'view_appointment.html',{'userinfo':appoi_info})
    return redirect('user:login')

def logout(request):
    request.session['user'] = False
    return redirect('user:login')