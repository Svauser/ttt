from rest_framework import serializers
from .models import Task
from rest_framework.exceptions import ValidationError
class TaskSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if len(value) < 3:
            raise ValidationError("Заголовок должен быть не короче 3 символов.")
        return value
    class Meta:
      model=Task
      fields = '__all__'