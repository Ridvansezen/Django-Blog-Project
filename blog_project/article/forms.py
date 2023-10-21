from django import forms

from .models import Article,Comment


# Here in this class we're import article model and show as a form.
class article_form(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description", "article_image"]


# Here in this class we're import comment model and show as a form.
class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_description"]
