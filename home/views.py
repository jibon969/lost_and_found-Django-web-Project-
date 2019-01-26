from django.shortcuts import render, redirect
from home.models import Reward
from person.models import Person
from item.models import Item
from .forms import RewardModeLForm
# Create your views here.


# Home Page View

def index(request):
    # First Div
    last_person_post = Person.objects.all()[:1]
    last_item_post = Item.objects.all()[:1]
    # End First Div

    # 2nd Div
    lost_person = Person.objects.filter(person="L").all()[:1]
    lost_item = Item.objects.filter(category="L").all()[:1]
    # End 2 div

    # table
    recent_found_person = Person.objects.filter(person="F").all()[:3]
    recent_item_item = Item.objects.filter(category="F").all()

    # Reword Post
    my_reward = Reward.objects.all()[:3]

    # Found Post Count Post
    a = Person.objects.filter(person="F").all()
    b = Item.objects.filter(category="F").all()

    # Lost Post Count
    c = Person.objects.filter(person="L").all()
    d = Item.objects.filter(category="L").all()

    context = {
        'lost_person': lost_person,
        'lost_item': lost_item,
        'recent_found_person': recent_found_person,
        'recent_found_item': recent_item_item,
        'my_reward': my_reward,

        # Total Post Count

        'a': a,
        'b': b,
        'c': c,
        'd': d,

    }

    if last_person_post[0].update > last_item_post[0].update:
        context['last_post'] = last_person_post
    else:
        context['last_post'] = last_item_post

    return render(request, 'index.html', context)


# Reward Function

def reward(request):
    if request.method == 'POST':
        form = RewardModeLForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('index')
    else:
        form = RewardModeLForm()
    context = {
        'form': form,
    }
    return render(request, 'reward.html', context)