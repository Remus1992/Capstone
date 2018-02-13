from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from accounts.models import User, Skill, Interest, Equipment, Cast, Crew, Project
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def home(request):
    return render(request, "accounts/home.html")


def register(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        user = User()
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.set_password(request.POST.get('password'))
        user.email = request.POST.get('email_address')
        user.phone_number = request.POST.get('phone_number')
        user.profile_bio = request.POST.get('profile_bio')
        # print(request.FILES)
        image = request.FILES.get('profile_image')
        if image:
            user.image = image
        user.save()

        # skill
        skills = 0
        for i in request.POST:
            if i.startswith('skill_profile_'):
                skills += 1

        for i in range(skills):
            # print(request.POST.get('skill_profile_{}'.format(i)))
            # print(request.POST.get('skill-level_{}'.format(i)))
            skill = Skill()
            skill.name = request.POST.get('skill_profile_{}'.format(i))
            skill.level = request.POST.get('skill-level_{}'.format(i))
            skill.user = user
            skill.save()

        # interest
        interests = 0
        for i in request.POST:
            if i.startswith('interest_profile_'):
                interests += 1

        for i in range(interests):
            interest = Interest()
            interest.name = request.POST.get('interest_profile_{}'.format(i))
            interest.user = user
            interest.save()

        # equipment
        equipment_set = 0
        for i in request.POST:
            if i.startswith('equipment_profile_'):
                equipment_set += 1

        for i in range(equipment_set):
            equipment = Equipment()
            equipment.name = request.POST.get('equipment_profile_{}'.format(i))
            equipment.condition = request.POST.get('equipment_condition_{}'.format(i))
            equipment.user = user
            equipment_image = request.FILES.get('equipment_image_{}'.format(i))
            # print(request.FILES)
            if equipment_image:
                equipment.image = equipment_image
            equipment.save()

    return render(request, "accounts/profile_reg_form.html")


@login_required(login_url='/accounts/login/')
def profile_view(request):
    return render(request, "accounts/profile.html", {})


@login_required(login_url='/accounts/login/')
def profile_edit(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        user = request.user
        password = request.POST.get('password')
        if len(password) > 0:
            user.set_password(password)
        image = request.FILES.get('profile_image')
        if image:
            user.image = image
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.phone_number = request.POST.get('phone_number')
        user.profile_bio = request.POST.get('profile_bio')
        user.save()

        # skill
        skills = 0
        for i in request.POST:
            if i.startswith('skill_profile_'):
                skills += 1

        for i in range(skills):
            # print(request.POST.get('skill_profile_{}'.format(i)))
            # print(request.POST.get('skill-level_{}'.format(i)))
            skill = Skill()
            skill.name = request.POST.get('skill_profile_{}'.format(i))
            skill.level = request.POST.get('skill-level_{}'.format(i))
            skill.user = user
            skill.save()

        # interest
        interests = 0
        for i in request.POST:
            if i.startswith('interest_profile_'):
                interests += 1

        for i in range(interests):
            interest = Interest()
            interest.name = request.POST.get('interest_profile_{}'.format(i))
            interest.user = user
            interest.save()

        # equipment
        equipment_set = 0
        for i in request.POST:
            if i.startswith('equipment_profile_'):
                equipment_set += 1

        for i in range(equipment_set):
            equipment = Equipment()
            equipment.name = request.POST.get('equipment_profile_{}'.format(i))
            equipment.condition = request.POST.get('equipment_condition_{}'.format(i))
            equipment.user = user
            equipment_image = request.FILES.get('equipment_image_{}'.format(i))
            # print(request.FILES)
            if equipment_image:
                equipment.image = equipment_image
            equipment.save()

        return HttpResponseRedirect(reverse("profile"))
    return render(request, "accounts/profile_edit.html")


@login_required(login_url='/accounts/login/')
def project_create(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        project = Project()
        project.owner = request.user
        project.title = request.POST.get('title_project')
        project.description = request.POST.get('description_project')
        project.budget = request.POST.get('budget_project')
        project.budget_details = request.POST.get('budget_details')
        project.city = request.POST.get('city_name')
        project.state = request.POST.get('state')
        project.zip = request.POST.get('zip_code')
        project.start_date = request.POST.get('start_date')
        project.end_date = request.POST.get('end_date')

        project_poster = request.FILES.get('project_poster')
        if project_poster:
            project.project_cover_art = project_poster

        additional_notes = request.FILES.get('additional_notes')
        if additional_notes:
            project.project_documents = additional_notes

        project_images = request.FILES.get('project_images')
        if project_images:
            project.project_images = project_images

        project.save()

        # cast
        cast_list = 0
        for i in request.POST:
            if i.startswith('role_name_'):
                cast_list += 1

        for i in range(cast_list):
            cast = Cast()
            cast.project = project
            cast.character = request.POST.get('role_name_{}'.format(i))
            cast.classification = request.POST.get('cast_classification_{}'.format(i))
            cast.save()

        # crew
        crew_list = 0
        for i in request.POST:
            if i.startswith('crew_role_'):
                crew_list += 1

        for i in range(crew_list):
            crew = Crew()
            crew.project = project
            crew.classification = request.POST.get('crew_role_{}'.format(i))
            crew.save()
        return HttpResponseRedirect(reverse("project_view", kwargs={"slug": project.slug}))
    return render(request, "accounts/project_create.html")


@login_required(login_url='/accounts/login/')
def project_edit(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        project.description = request.POST.get('description_project')
        project.budget = request.POST.get('budget_project')
        project.budget_details = request.POST.get('budget_details')
        project.city = request.POST.get('city_name')
        project.state = request.POST.get('state')
        project.zip = request.POST.get('zip_code')
        project.start_date = request.POST.get('start_date')
        project.end_date = request.POST.get('end_date')

        project_poster = request.FILES.get('project_poster')
        if project_poster:
            project.project_cover_art = project_poster

        project.save()

        # cast
        cast_list = 0
        for i in request.POST:
            if i.startswith('role_name_'):
                cast_list += 1

        for i in range(cast_list):
            cast = Cast()
            cast.project = project
            cast.character = request.POST.get('role_name_{}'.format(i))
            cast.classification = request.POST.get('cast_classification_{}'.format(i))
            cast.save()

        # crew
        crew_list = 0
        for i in request.POST:
            if i.startswith('crew_role_'):
                crew_list += 1

        for i in range(crew_list):
            crew = Crew()
            crew.project = project
            crew.classification = request.POST.get('crew_role_{}'.format(i))
            crew.save()
        return HttpResponseRedirect(reverse("project_view", kwargs={"slug": project.slug}))

    return render(request, "accounts/project_edit.html", {"project": project})


def project_total_list(request):
    total_project_list = Project.objects.all()
    return render(request, "accounts/project_total_list.html", {'total_list': total_project_list})


def project_view(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "accounts/project_view.html", {"project": project})


@login_required(login_url='/accounts/login/')
def project_user_created_list(request):
    return render(request, "accounts/project_user_created_list.html")


@login_required(login_url='/accounts/login/')
def project_user_committed_list(request):
    return render(request, "accounts/project_user_committed_list.html")


def about(request):
    return render(request, "accounts/about.html")
