from django.shortcuts import render
from dictionary.models import Words
import random

# Create your views here.
def index(request):
    if 'word' not in request.session:
        word = random.choice(Words.objects.all())
        request.session['word'] = word.id

    word_id = request.session['word']
    word = Words.objects.get(id=word_id)

    result = ''

    if request.method == 'POST':
        if 'answerButton' in request.POST:
            answer = request.POST.get('answer')
            if word.translation == answer:
                result = 'Правильна'
            else:
                result = 'Хибна'
        if 'nextButton' in request.POST:
            word = random.choice(Words.objects.all())
            request.session['word'] = word.id
            result = ''

    data = {
        'word': word,
        'result': result,
    }
    return render(request, 'quiz/swapCardTest.html', data)