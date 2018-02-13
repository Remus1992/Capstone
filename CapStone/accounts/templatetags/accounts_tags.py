from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def profile_or_default_image(user):
    if user.image:
        return mark_safe('<img src="{}" width="300px" class="avatar img-circle img-thumbnail" alt="avatar">'.format(user.image.url))
    return mark_safe('<img src="{}" width="300px" class="avatar img-circle img-thumbnail" alt="avatar">'.format('/static/accounts/img/human_being.jpg'))


@register.simple_tag
def project_poster_or_default_image(project):
    if project.project_cover_art:
        return mark_safe('<img src="{}" width="300px" class="avatar img-circle img-thumbnail" alt="movie_poster">'.format(project.project_cover_art.url))
    return mark_safe('<img src="{}" width="300px" class="avatar img-circle img-thumbnail" alt="avatar">'.format('/static/accounts/img/Default_poster.jpg'))


@register.simple_tag
def project_background_or_default_image(project):
    if project.project_images:
        return mark_safe('<img src="{}" alt="background">'.format(project.project_images.url))
    return mark_safe('<img src="{}"  alt="background">'.format('/static/accounts/img/green_background.jpg'))