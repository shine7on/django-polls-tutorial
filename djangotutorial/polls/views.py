from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))
    # or return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse(f"You are looking at the question {question_id}")

def result(request, question_id):
    response = "You are looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)
