#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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