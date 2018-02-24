from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from accounts.models import User, Skill, Interest, Equipment, Cast, Crew, Project, Message
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse


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


@login_required(login_url='/projects/login/')
def profile_view(request, slug):
    profile = User.objects.get(username=slug)
    return render(request, "accounts/profile.html", {"profile": profile})


@login_required(login_url='/projects/login/')
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

        return HttpResponseRedirect(reverse("profile", args=[request.user.username]))
    return render(request, "accounts/profile_edit.html")


@login_required(login_url='/projects/login/')
def project_create(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        project = Project()
        project.owner = request.user
        project.title = request.POST.get('title_project')
        project.tag_line = request.POST.get('tag_line')
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


@login_required(login_url='/projects/login/')
def project_edit(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        project.tag_line = request.POST.get('tag_line')
        project.description = request.POST.get('description_project')
        project.genre = request.POST.get('genre')
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
    # print('string')
    if request.method == 'POST':
        msg = Message()
        msg.sender = request.user
        msg.recipient = User.objects.get(username=request.POST.get('recipient'))
        msg.project = Project.objects.get(title=request.POST.get('project_name'))
        cast = request.POST.get('cast_id')
        if cast:
            msg.cast = Cast.objects.get(pk=cast)

        crew = request.POST.get('crew_id')
        if crew:
            msg.crew = Crew.objects.get(pk=crew)

        msg.body = request.POST.get('message_body')
        msg.save()

    return render(request, "accounts/project_view.html", {"project": project})


# def send_message(request, slug):
#     project = get_object_or_404(Project, slug=slug)
#     if request.method == 'POST':
#         msg = Message()
#         msg.sender = request.user
#         msg.recipient = User.objects.get(username=request.POST.get('recipient'))
#         msg.project = Project.objects.get(title=request.POST.get('project_name'))
#         cast = request.POST.get('cast_id')
#         if cast:
#             msg.cast = Cast.objects.get(pk=cast)
#
#         crew = request.POST.get('crew_id')
#         if crew:
#             msg.crew = Crew.objects.get(pk=crew)
#
#         msg.body = request.POST.get('message_body')
#         msg.save()
#         return HttpResponseRedirect(reverse("project_view", kwargs={"slug": project.slug}))
#         # return JsonResponse({'message': 'Success'})
#     return JsonResponse({'message': 'Request must be post.'})

@login_required(login_url='/projects/login/')
def view_received_message(request):
    messages = request.user.received_messages.all().order_by('sender__username')
    messages_sent = request.user.sent_messages.all().order_by('recipient__username')
    # message_sender_list = []
    # for message in User.objects.get(username=request.POST.get('recipient')):
    #     print("printMe")
    #     print(message)
    #     message_sender = message.sender
    #     if message_sender not in message_sender_list:
    #         message_sender_list.append('message_sender')
    #     else:
    #         continue
    return render(request, 'accounts/view_received_message.html',
                  {'messages': messages, 'messages_sent': messages_sent})


@login_required(login_url='/projects/login/')
def view_single_message(request, slug):
    message = Message.objects.get(pk=slug)
    children_messages = message.children.all()
    message.read = True
    for child in children_messages:
        child.read = True
        child.save()
    message.save()
    messages = request.user.received_messages.all().order_by('sender__username')
    messages_sent = request.user.sent_messages.all().order_by('recipient__username')
    # messages = Message.objects.filter(sender=message.sender)
    # print(messages)

    return render(request, 'accounts/view_single_message.html',
                  {'message': message, 'messages': messages.exclude(pk=message.pk),
                   'messages_sent': messages_sent.exclude(pk=message.pk)})


def view_add_chat_message(request):
    if request.method == "POST":
        child_message = Message()
        parent_message = Message.objects.get(pk=request.POST.get('parent_id'))
        users_list = []
        users_list.append(parent_message.sender)
        users_list.append(parent_message.recipient)
        users_list.remove(request.user)
        child_message.message = parent_message
        child_message.sender = request.user
        child_message.recipient = users_list[0]
        # child_message.recipient = parent_message.sender if parent_message.sender is not request.user else parent_message.recipient
        child_message.project = parent_message.project
        child_message.cast = parent_message.cast
        child_message.crew = parent_message.crew
        child_message.body = request.POST.get('child_message')
        child_message.save()
        # print(child_message.is_parent())
        # print(parent_message.is_parent())

        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'MUST BE A POST'})


# @login_required(login_url='/projects/login/')
# def project_user_created_list(request):
#     return render(request, "accounts/project_user_created_list.html")
#
#
# @login_required(login_url='/projects/login/')
# def project_user_committed_list(request):
#     return render(request, "accounts/project_user_committed_list.html")


def about(request):
    return render(request, "accounts/about.html")
