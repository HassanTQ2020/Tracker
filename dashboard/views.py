from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from dashboard.models import Home
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import HomeForm
# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        issuetype = request.POST['issuetype']
        status = request.POST.get('status','Open')#setting default value
        desc = request.POST['desc']
        ins = Home(name=name,email=email,phone=phone,issuetype=issuetype,status=status,desc=desc)
        ins.save()
        
    return render(request,"index.html")
class dashboard(View):
   def get(self,request):
        allIssues = Home.objects.all()
        count     = Home.objects.count()
        context = {'issues':allIssues,'count':count}
        return render(request,"dashboard.html",context)
def get_data(request):
    data = {
        'sales':100,
        'customers':10,
    }
    return JsonResponse(data)
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        bs_count  = Home.objects.filter(issuetype='Blank/Frozen Screen').count()
        cd_count = Home.objects.filter(issuetype='Corrupted Drivers').count()
        pass_count = Home.objects.filter(issuetype='Password Reset/ Account Access').count()
        or_count= Home.objects.filter(issuetype='Overheating').count()
        newapp_count  = Home.objects.filter(issuetype='New Application Installation').count()
        cs_count  = Home.objects.filter(issuetype='Computer is Slow').count()
        sn_count  = Home.objects.filter(issuetype='Strange Noise').count()
        iis_count  = Home.objects.filter(issuetype='Internet is Down').count()
        labels =['Blank/Frozen Screen','Corrupted Drivers','Password Reset/ Account Access','Overheating','New Application Installation','Computer is Slow','Strange Noise','Internet is Down']
        default_items = [bs_count,cd_count,pass_count,or_count,newapp_count,cs_count,sn_count,iis_count]
        data = {
           'labels':labels,
           'default':default_items,
         }
        return Response(data)
# Adding pie chart model
class PieData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        o_count  = Home.objects.filter(status='Open').count()
        p_count = Home.objects.filter(status='Pending').count()
        wip_count = Home.objects.filter(status='Work in Progress').count()
        c_count= Home.objects.filter(status='Closed').count()
        label_pi=['Open','Pending','Work in Progress','Closed']
        default_item = [o_count,p_count,wip_count,c_count]

        data_pi = {
           'label_':label_pi,
           'default_':default_item,
         }
        return Response(data_pi)
# Adding Udate form module
class updateIssue(View):
   def get(self,request,pk):
        issue = Home.objects.get(id=pk)
        form = HomeForm(instance=issue)
        if request.method == "POST":
            form = HomeForm(request.POST, instance=issue)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        context = {'form':form}
        return render(request,'update_form.html',context)
