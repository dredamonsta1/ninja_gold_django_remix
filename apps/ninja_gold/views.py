from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

# Create your views here.
def index(request):
    request.session['gold'] = request.session.get('gold', 0)
    request.session['log'] = request.session.get('log', [])
    return render(request, 'ninja_gold/index.html')
    

def money(request):
    if request.method == "POST":
        building = request.POST['building']

        now = datetime.now()
        timestamp = datetime.strftime(now, "%Y/%M/%d - %-I:%m %p")

        if building == "farm":
            gold = randint(10,20)

        elif building == "cave":
            gold = randint(5,10)

        elif building == "house":
            gold = randint(2,5)

        if building == "casino":
            gold = randint(-50,50)

        if gold > 0:
            message = "you entered a {} and earned {} golds - ({})".format(building, gold, timestamp)
        else:
            message ="you went to a casino and lost {} golds...Ouch! - ({})".format(gold*-1, timestamp)

            request.session['log'].insert(0, message)

        request.session['gold'] += gold







    return redirect('/')
