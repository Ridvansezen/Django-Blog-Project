from ckeditor.fields import RichTextField
from django.db import models

# This class represents our article model.
class Article(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Yazar"
    )

    title = models.CharField(max_length=50, verbose_name="Başlık")

    description = RichTextField(max_length=10000, verbose_name="Açıklama")

    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulma tarihi"
    )

    article_image = models.FileField(
        blank=True, 
        null=True, 
        verbose_name="Dosya Ekle")

    def short_description(self):
        return self.description[:100]

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_date"]


# This class represents our comment model.
class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name="Makale",
        related_name="comments",
    )

    comment_author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Kullanıcı"
    )

    comment_description = models.CharField(
        max_length=500, 
        verbose_name="Yorum")

    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_description

    class Meta:
        ordering = ["comment_date"]
