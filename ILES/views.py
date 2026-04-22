
from django.shortcuts import render, redirect , get_object_or_404
from .models import Evaluation_criteria, Internship_placement, Evaluation, Student , Supervisor , Weekly_log , Daily_log 
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view , permission_classes  
from rest_framework.response import Response
from .serializers import EvaluationSerializer, Internship_placementSerializer ,Weekly_logSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny
#from rest_framework.viewsets import ModelViewSet
from datetime import date
User = get_user_model()

@login_required
def create_placement(request):
    if request.method=='POST':
        student_id=request.POST.get('student_id')
        position_title=request.POST.get('position_title')
        company_name=request.POST.get('company_name')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        workplace_supervisor=request.POST.get('workplace_supervisor')
        academic_supervisor=request.POST.get('academic_supervisor')

        Internship_placement.objects.create(
            student_id=student_id,
            position_title=position_title,
            company_name=company_name,
            start_date=start_date,
            end_date=end_date,
            workplace_supervisor=workplace_supervisor,
            academic_supervisor=academic_supervisor,
        )
        return redirect('placements_list')
    students=User.objects.all()
    return render(request,'create_placement.html',{'student':students})


def placements_list(request):
    placements = Internship_placement.objects.all()
    return render(request, 'placements.html', {'placements': placements})

def student_placements(request, student_id):
    placements=Internship_placement.objects.filter(student_id=student_id)
    return render(request,'student_placements.html',{'placements':placements})
 
def create_evaluation(request):
    if request.method=="POST":
        student_id=request.POST.get('student_id')
        supervisor_id=request.POST.get('supervisor_id')
        criteria_id=request.POST.get('criteria_id')
        performance_score=request.POST.get('performance_score')
        comments=request.POST.get('comments')

        students=get_object_or_404(Student,id=student_id)
        supervisors=get_object_or_404(Supervisor,id=supervisor_id)
        criteria=get_object_or_404(Evaluation_criteria,id=criteria_id)

        Evaluation.objects.create(
            student=students,
            supervisor=supervisors,
            criteria=criteria,
            performance_score=performance_score,
            comments=comments
        )
        return redirect('evaluations_list')
    students=Student.objects.all()#give me all the records so i can show them in a drop down
    supervisors=Supervisor.objects.all()
    criteria=Evaluation_criteria.objects.all()
    return render( request,'create_evaluation.html',{
        'students':students,
        'supervisors':supervisors,
        'criteria':criteria,
    })
def evaluations_list(request):
    evaluations=Evaluation.objects.all()
    return render(request,'evaluation_list.html',{'evaluations':evaluations})

def student_evaluations(request):

    if not request.user.is_authenticated:
        return redirect('login')
    #if request.user.role != 'student':
        #return HttpResponse("Access denied -students only")
    evaluations=Evaluation.objects.filter(student=request.user)
    return render(request,'student_evaluation.html',{
        'evaluations':evaluations,
        'title':"Student Evaluations"
        })

def supervisor_evaluation(request):
    #if request.user.role !='supervisor':
        #return redirect('/')
    
    supervisor= Supervisor.objects.filter(user =request.user).first()
    evaluations=Evaluation.objects.filter(supervisor=supervisor)
    return render(request,'supervisor_evaluation.html',{
        'evaluations':evaluations
,         'title':"Supervisor Evaluations"
        })

def all_evaluations(request):#admin view 
    #if not request .user .is_superuser:
        
        #return redirect('login')
    evaluations=Evaluation.objects.select_related('student','supervisor','criteria')
    return render(request,'all_evaluations.html',{
                  'evaluations':evaluations,
                  'title':"all evaluations"
                  })
def create_daily_log(request):
    weekly_logs=Weekly_log.objects.all()
    if request.method=="POST":
        weekly_log_id=request.POST.get('weekly_log')
        day=request.POST.get('day')
        Activity=request.POST.get('activity')
        skills_gained=request.POST.get('skills_gained')
        challenges=request.POST.get('challenges')
        Description=request.POST.get('description')
        weekly_log=get_object_or_404(Weekly_log,id=weekly_log_id)
        Daily_log.objects.create(
            student =request.user,
            weekly_log=weekly_log,
            day=day,
            activity=Activity,
            skills_gained=skills_gained,
            challenges=challenges,
            description=Description,

        )
        return redirect(daily_logs_list)
    return render(request,'daily_log_form.html',{
        'weekly_logs':weekly_logs
    })
def daily_logs_list(request):
    logs=Daily_log.objects.filter(student=request.user)
    return render(request,'daily_logs_list.html',{
        'logs':logs
    })
def login_view(request):
        if request.method =="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                if user.role == 'Student':
                    return redirect('student_dashboard')
                elif user.role=='supervisor':
                    return redirect('supervisor_dashboard')
                elif user.role=='admin':
                    return redirect('admin_dashboard')
                return redirect('dashboard')
            else:
                return render(request,'login.html', {'error':'invalid details'})
        return render(request,'login.html')
def logout_view(request):
    logout (request)
    return redirect('login')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role=='student':
         return redirect('student_dashboard')
    elif request.user.role=='supervisor':
        return redirect('supervisor_dashboard')
    elif request.user.role=='admin':
        return redirect('admin_dashboard')
@login_required
def student_dashboard(request):
    if request.user.role !='student':
        return redirect('login')
    return render(request, 'student_dashboard.html')

@login_required
def supervisor_dashboard(request):
    if request.user.role !='supervisor':
        return redirect('login')
    return render(request,'supervisor_dashboard.html')

@login_required
def admin_dashboard(request):
    if request.user.role !='admin':
        return redirect('login')
    return render(request,'admin_dashboard.html')


@api_view(['POST','GET'])
def create_evaluation_api(request):
    serializer =EvaluationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])# Only authenticated users can access
def get_evaluation(request):
    evaluations=Evaluation.objects.all()#-  fetches all records from your Evaluation table.
    serializer=EvaluationSerializer(evaluations,many=True)#converts the queryset into JSON-friendly
    return Response(serializer.data)#sends that JSON back to the client.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def logs(request):
    if request.method=='GET':
        logs=Weekly_log.objects.all()
        serializer=Weekly_logSerializer(logs, many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=Weekly_logSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def placements(request):
    if request.method == 'GET':
        data=Internship_placement.objects.all()
        serializer=Internship_placementSerializer(data , many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=Internship_placementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        return Response(serializer.errors, status=400)
@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def create_log(request):
    data=request.data.copy()
    data['student']=request.user.id #
    serializer =Weekly_logSerializer(data=data)
    if serializer.is_valid():
        if date.today() > serializer.validated_data['end_date']:
            return Response ({"error" : 'Deadline passed'} , status=400)

        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def edit_log(request,id):
    try:
        log=Weekly_log.objects.get(id=id)
    except Weekly_log.DoesNotExist:
        return Response({'error' : 'Log not found'})
    
    if log.student != request.user :
        return Response({"error": "Not allowed"})
    if log.state == 'Approved':
        return Response({"error" : "Cannot edit Approved log"} , status=400)
    serializer=Weekly_logSerializer(log, data=request.data , partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors , status=400)

@api_view(['PUT','PATCH'])
#@permission_classes([IsAuthenticated])
def update_log(request, pk):
    try:
        log=Weekly_log.objects.get(pk=pk , student=request.user)
    except Weekly_log.DoesNotExist:
        return Response({{"error":"Log not found"}})
    if log.is_approved:
        return Response({"error":"cant edit an approved log"})
    serializer=Weekly_logSerializer(log, data=request.data , partial=True)
    if serializer.is_valid:
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

#class LogViewSet(ModelViewSet):
    queryset=Log.objects.all()
    serializer_class=LogSerializer

    