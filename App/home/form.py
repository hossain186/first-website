from django.forms import ModelForm

from .models import Topic , Artical

class Tform(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

class Aform(ModelForm):
    class Meta:
        model = Artical
        fields = '__all__'
