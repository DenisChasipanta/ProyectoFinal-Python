from django.db import models
#from ckeditor.fields import RichTextField

# Create your models here.
class Articulo(models.Model):
    title=models.CharField(max_length=100, verbose_name='Título')
    subtitle=models.TextField(max_length=100,verbose_name='Subtítulo')
    content=models.TextField(verbose_name='Contenido')
    image=models.ImageField(upload_to='articulos', verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de publicación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')


    class Meta:
        verbose_name='article'
        verbose_name_plural='articles'
        ordering=['-created']
    
    def __str__(self):
        return self.title