from django.db import models



class Articles(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    actif = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True)
    slug = models.SlugField(max_length=10)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

        def __str__(self):
            return self.name



