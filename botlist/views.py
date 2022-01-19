from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from botlist.models import Submission
from django.contrib import messages


# Create your views here.
def index(req):
    bots = Submission.objects.all().filter(approved=True)
    print(bots)
    return render(req, 'index.html', {"bots": bots})


def submitPage(req: HttpRequest):
    return render(req, 'submit.html')


def submitBot(req: HttpRequest):
    if(req.method != "POST"):
        return HttpResponse("Only Post Request is Allowed")
    body = req.POST
    bot_name = body.get('bot_name')
    owner_name = body.get("owner_name")
    bot_id = body.get("bot_id")
    invite_link = body.get("invite_link")
    language_used = body.get("language_used")
    description = body.get("description")
    Submission(bot_name=bot_name, owner_name=owner_name, bot_id=bot_id,
               invite_link=invite_link, language_used=language_used, description=description, approved=False).save()
    messages.success(req, "Your Bot is submitted Successfully!")
    return render(req, 'success.html')
