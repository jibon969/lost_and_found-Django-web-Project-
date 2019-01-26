from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from person.models import Person
from item.models import Item
from lost.forms import LostPersonModelForm, LostItemModelForm
from comment.models import PersonComment, PersonReplayComment
from comment.models import ItemComment, ItemReplayComment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


# List of all lost item and person

def lost(request):
    lost_person = Person.objects.filter(person='L').all()
    lost_item = Item.objects.filter(category='L').all()
    search = request.GET.get('q')
    if search:
        lost_person = Person.objects.filter(
            Q(status__icontains=search) |
            Q(name__icontains=search) |
            Q(father_name__icontains=search) |
            Q(mother_name__icontains=search) |
            Q(age__icontains=search) |
            Q(location__icontains=search) |
            Q(phone_number__icontains=search) |
            Q(identification_mark__icontains=search) |
            Q(secret_information__icontains=search)
        )

        lost_item = Item.objects.filter(
            Q(status__icontains=search) |
            Q(name__icontains=search) |
            Q(category__icontains=search) |
            Q(location__icontains=search) |
            Q(phone_number__icontains=search) |
            Q(identification_mark__icontains=search) |
            Q(secret_information__icontains=search)
        )
    context = {
        'lost_person': lost_person,
        'lost_item': lost_item
    }
    return render(request, 'lost.html', context)


# Lost Person Details views

@login_required(login_url='/login/')
def lost_person_details(request, id):
    lp_detail = get_object_or_404(Person, id=id)
    context = {
        'lp_detail': lp_detail
    }
    # Person Comment Form
    if request.method == "POST":
        PersonComment.objects.create(
            message=request.POST.get('message'),
            created_by=request.user,
            person=lp_detail
        )
    # End Person comment Form
    return render(request, 'lost-person-details.html', context)


# Lost Person Replay comment form

@login_required(login_url='/login/')
def lost_person_reply_comment(request, id):
    comment = PersonComment.objects.get(id=id)
    if request.method == "POST":
        PersonReplayComment.objects.create(
            message=request.POST.get('message'),
            reply=comment,
            created_by=request.user
        )
    return render(request, 'lost-person-details.html')


# Lost Item Details Views

@login_required(login_url='/login/')
def lost_item_details(request, id):
    l_item = get_object_or_404(Item, id=id)
    context = {
        'l_item': l_item
    }
    # Item Comment Form
    if request.method == "POST":
        ItemComment.objects.create(
            message=request.POST.get('message'),
            created_by=request.user,
            item=l_item
        )
    # End Item Comment
    return render(request, 'lost-item-details.html', context)


# Lost item replay comment

@login_required(login_url='/login/')
def lost_item_reply_comment(request, id):
    comment = ItemComment.objects.get(id=id)
    if request.method == "POST":
        ItemReplayComment.objects.create(
            message=request.POST.get('message'),
            reply=comment,
            created_by=request.user
        )
    return render(request, 'lost-item-details.html')


# Lost Person Create Form

@login_required(login_url='/login/')
def create_lost_person(request):
    if request.method == 'POST':
        form = LostPersonModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Post successfully Created')
            return redirect('/lost/')
    else:
        form = LostPersonModelForm()
    context = {
        'form': form
    }
    return render(request, 'lost-form.html', context)


# Lost Item Create Form

@login_required(login_url='/login/')
def create_lost_item(request):
    if request.method == 'POST':
        form = LostItemModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Post successfully Created')
            return redirect('/lost/')
    else:
        form = LostItemModelForm()
    context = {
        'form': form
    }
    return render(request, 'lost-form.html', context)


# Lost Person Update

@login_required(login_url='/login/')
def lost_person_update(request, id):
    lp_update = get_object_or_404(Person, id=id)
    form = LostPersonModelForm(request.POST or None, instance=lp_update)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Update successfully complete')
        return redirect('/lost/')
    context = {
        'form': form
    }
    return render(request, 'lost-form.html', context)


# Lost Item Update

@login_required(login_url='/login/')
def lost_item_update(request, id):
    l_item_update = get_object_or_404(Item, id=id)
    form = LostItemModelForm(request.POST or None , instance=l_item_update)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Update successfully complete')
        return redirect('/lost/')
    context = {
        'form': form
    }
    return render(request, 'lost-form.html', context)


# Lost Person Delete

@login_required(login_url='/login/')
def lost_person_delete(request, id):
    lp_delete = get_object_or_404(Person, id=id)
    if request.method == "POST":
        lp_delete.delete()
        messages.add_message(request, messages.WARNING, 'Post successfully Deleted')
        return redirect('/lost/')
    context = {
        'lp_delete': lp_delete
    }
    return render(request, 'lost_person_delete.html', context)


# Lost Item Delete

@login_required(login_url='/login/')
def lost_item_delete(request, id):
    l_item_delete = get_object_or_404(Item, id=id)
    if request.method == "POST":
        l_item_delete.delete()
        messages.add_message(request, messages.WARNING, 'Post successfully Deleted')
        return redirect('/lost/')
    context = {
        'f_item_delete': l_item_delete
    }
    return render(request, 'lost_item_delete.html', context)