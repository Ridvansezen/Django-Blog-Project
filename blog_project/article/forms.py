from django import forms

from .models import Article,Comment


class article_form(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description", "article_image"]


class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_description"]
