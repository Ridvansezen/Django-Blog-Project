from django.db import models

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length= 50, verbose_name="Başlık")
    description = models.TextField(max_length=500, verbose_name="Açıklama")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma tarihi")
    def __str__(self):
        return self.title
