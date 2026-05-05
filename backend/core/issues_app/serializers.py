from rest_framework import serializers
from .models import Internship_placement, Weekly_log, Evaluation_criteria, Evaluation, Student, Supervisor, Daily_log

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

class Internship_placementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship_placement
        fields = '__all__'

class Weekly_logSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekly_log
        fields = '__all__'

class Evaluation_criteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation_criteria
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = '__all__'

class Daily_logSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily_log
        fields = '__all__'