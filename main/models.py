from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='articles/')
    reading_time = models.DurationField(blank=True, null=True)
    author = models.CharField(max_length=255, default='jasur usmonov')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    views = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while Article.objects.filter(slug=slug).exists():
                slug = base_slug + str(count)
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Content(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:50]


class Comment(models.Model):
    author = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]


class NewsLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    subject = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.full_name} ({self.email})'


class Gallary(models.Model):
    image = models.ImageField(upload_to='gallaries/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Image uploaded on {self.created_at}'