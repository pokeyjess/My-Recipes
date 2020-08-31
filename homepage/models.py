from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField()
    instructions = models.TextField()
    recipe_image = models.ImageField(upload_to='images/', null=True, blank=True)
    class Meta:
        ordering = ('title',)
    
    # def upload_image(self, filename):
        # return 'recipe/{}/{}'.format(self.title, filename)

    def __str__(self):
        return f"{self.title} : {self.category.name}"

