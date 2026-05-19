from rest_framework import serializers
from .models import Trainee


class TraineeSerializer(serializers.ModelSerializer):
    # Read-only convenience field showing the related course title
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = Trainee
        fields = ['id', 'name', 'course', 'course_title', 'personal_image']
        read_only_fields = ['id']