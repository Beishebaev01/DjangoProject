from django import forms
from posts.models import Category, Tag


class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=100, required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if (title and content) and (title.lower() == content.lower()):
            raise forms.ValidationError("Title and content cannot be the same.")
        return cleaned_data
    
    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title and len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
    
