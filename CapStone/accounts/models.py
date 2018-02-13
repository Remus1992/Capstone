from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


def user_image_uh(instance, filename):
    return "users/{}/profile_image/{}".format(instance.username, filename)


class User(AbstractUser):
    phone_number = models.CharField(max_length=50)
    profile_bio = models.TextField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to=user_image_uh, blank=True, null=True)


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name or 'No name given'


class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interests')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


def equip_image_uh(instance, filename):
    return "users/{}/equip_image/{}".format(instance.user, filename)


class Equipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='equipment')
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=50)
    image = models.ImageField(upload_to=equip_image_uh, blank=True, null=True)

    def __str__(self):
        return self.name


def project_cover_art_uh(instance, filename):
    return "projects/{}/project_cover_art/{}".format(instance.owner, filename)


def project_document_uh(instance, filename):
    return "projects/{}/project_document/{}".format(instance.owner, filename)


def project_image_uh(instance, filename):
    return "projects/{}/project_image/{}".format(instance.owner, filename)


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_projects")
    title = models.CharField(max_length=100)
    project_cover_art = models.ImageField(upload_to=project_cover_art_uh, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    project_documents = models.FileField(upload_to=project_document_uh, blank=True, null=True)
    project_images = models.ImageField(upload_to=project_image_uh, blank=True, null=True)
    budget = models.CharField(max_length=50)
    budget_details = models.TextField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            num = 0
            temp_slug = slugify(self.title)
            while Project.objects.filter(slug=temp_slug).exists():
                num += 1
                temp_slug = "{}_{}".format(slugify(self.title), num)
            self.slug = temp_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or 'No name given'


class Cast(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="cast_members")
    character = models.CharField(max_length=100, blank=True, null=True)
    classification = models.CharField(max_length=50, blank=True, null=True)
    # username for person committed
    committed_cast_member = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.character or 'No name given'


class Crew(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="crew_members")
    classification = models.CharField(max_length=50, blank=True, null=True)
    # username for person committed
    committed_crew_member = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.classification or 'No name given'







