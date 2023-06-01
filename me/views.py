from django.shortcuts import render, redirect ,reverse, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . import forms
from .forms import CustomerForm
from . import models
from me.models import Customer
from .models import billmount
from django.contrib.auth.models import Group
from django.views.generic import DetailView
from .filters import orderfilter
from django.contrib.auth.decorators import login_required,user_passes_test
#from django.conf import settings
# Create your views here.

@login_required(login_url='afterlogin')
def index(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('login/')
	
	return render(request, "me/students.html")


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='Customer')
            my_customer_group[0].user_set.add(user)
            messages.info(request,"this person was succesfuly saved")
            return redirect('logiin')
        
    return render(request,'me/customersignup.html',context=mydict)

def is_customer(user):
    return user.groups.filter(name='Customer').exists()

def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('view-customer')
    else:
        return redirect('logiin')
		
@login_required(login_url='afterlogin')
@user_passes_test(is_customer)
def view_customer_view(request):
    customers=Customer.objects.all()
    bilm=billmount.objects.all()
    ccount=customers.count()
    cco=bilm.count()
    orderr=orderfilter(request.GET, queryset=customers)
    customers= orderr.qs
	
    return render(request,'me/view_customer.html',{'customers':customers,'orderr':orderr,'ccount':ccount,'cco':cco})


@login_required(login_url='afterlogin')
@user_passes_test(is_customer)	
def addbl(request):
	
	if request.method=='POST':
		try:
			daySpent=int(request.POST.get('daySpent'))
			roomCharge=int(request.POST.get('roomCharge'))
			cost=int(request.POST.get('cost'))
			bFee=int(request.POST.get('bFee'))
			otherCharge=int(request.POST.get('otherCharge'))
			total=daySpent*roomCharge+cost+bFee+otherCharge
			blo=billmount(daySpent=daySpent,roomCharge=roomCharge,cost=cost,bFee=bFee,otherCharge=otherCharge,total=total)
			blo.save()
			return render(request,'me/bill.html',{'total':total})
		except:
			messages.info(request,"meel banaan lama ogola!")
	else:
		return render(request,'me/bill.html')
		
	return render(request,'me/bill.html')
def addview(request):
	
		
	return render(request,'me/bill2.html')
		
#####################
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

def reportt(request):
    order=Customer.objects.all()
    templatep='me/download_invoic.html'
    mydict={
        'order':order
    }
    resp=HttpResponse(content_type='application/pdf')
    resp['Content-Disposition']='filename="allreport.pdf"'
    tempp=get_template(templatep)
    html=tempp.render(mydict)
    pisa_st=pisa.CreatePDF(html,dest=resp)
    if pisa_st.err:
	    return HttpResponse('some error')
    return resp
	
    #return render_to_pdf('me/download_invoice.html',mydict)
	
def download_invoice_view(request,id):
    order=Customer.objects.get(pk=id)
	
    
    mydict={
        'username':order.user,
        'image':order.profile_pic,
        'mobile':order.mobile,
        'address':order.address,

    }
    return render_to_pdf('me/download_invoice.html',mydict)


def deletedata(request, id):
	todor=Customer.objects.get(pk=id)

	context={'todor':todor}
	if request.method == "POST":
		todor.delete()
		return HttpResponseRedirect(reverse("index"))
	
	return render(request, "me/delpage.html",context)
	
def edit_profile_view(request, id):
    todor=Customer.objects.get(pk=id)
    form=CustomerForm(instance=todor)
    context={'todor':todor,'form':form}
    if request.method=='POST':
       
        customerForm=forms.CustomerForm(request.POST,request.FILES,instance=todor)
        
        if customerForm.is_valid():
           		
            customerForm.save()
              
        return HttpResponseRedirect(reverse("view-customer"))
    return render(request,'me/edit.html',context=context)
