from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Member


# Create your views here.
def index(request):
    #return HttpResponse('Welcome to the world of Django.')
    member_list = Member.objects.order_by('-create_date')
    context = {'member_list' : member_list }
    return render(request, 'kingchobo/member_list.html', context)

def detail(request, member_id):
    #member = Member.objects.get(id=member_id)
    member = get_object_or_404(Member, pk=member_id)

    context = { 'member' : member }
    return render(request, 'kingchobo/member_detail.html', context)

def input(request):
    return render(request, 'kingchobo/member_input.html')

def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    profile = request.POST.get('profile')

    new_member = Member(name=name, email=email, profile=profile, create_date=timezone.now())
    new_member.save()

    return redirect('kingchobo:detail', member_id=new_member.id)