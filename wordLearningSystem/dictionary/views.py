from django.shortcuts import render, redirect
from authorization.models import Users
from .models import Words, Personaldict, Wordsindict
import random
from PyDictionary import PyDictionary

# Create your views here.
def index(request, word=None):
    message = ''
    try:
        word_obj = Words.objects.get(word=word)
        meaning = meaningOfWord(word)

    except Words.DoesNotExist:
        word_obj = None
        meaning = None

    if request.method == "POST":
        if 'buttonSearch' in request.POST:
            searched = request.POST.get('searched')
            words = Words.objects.filter(word__contains=searched)
            data = {
                'words' : words,
            }
            return render(request, 'dictionary/dictionary.html', data)

        if 'buttonRandom' in request.POST:
            word = random.choice(Words.objects.all())
            # meaning = meaningOfWord(word.word)
            request.session['current_word'] = word.word
            return redirect('/dictionary/'+word.word+'/', word=word.word)

        if 'buttonAddToList' in request.POST:
            username = request.user.username
            user = Users.objects.get(name=username)
            # personalDict = Personaldict.objects.get(user=user)
            personalDict = get_personaldict(username=username)
            is_word_in_dict = Wordsindict.objects.filter(dict__user=user, word=word_obj).exists()

            # Використання результату перевірки
            if is_word_in_dict:
                # Слово є в особистому словнику
                message = 'Слово вже є у словнику'
            else:
                # Слово відсутнє в особистому словнику
                words_in_dict = Wordsindict(dict=personalDict, word=word_obj)
                words_in_dict.save()
                message = 'Слово додане у словник'

    context = {
        'word': word_obj,
        'meaning' : meaning,
        'message': message,
    }
    return render(request, 'dictionary/dictionary.html', context)


def meaningOfWord(word):
    dictionary = PyDictionary()
    meaning = dictionary.meaning(word)['Noun'][0]
    return meaning




def myList(request):
    message = ''
    words_list = None

    if request.user.is_authenticated:
        username = request.user.username
        try:
            # user = Users.objects.get(name=username)
            # personalDict = Personaldict.objects.get(user=user)
            personalDict = get_personaldict(username=username)
            words_list = Wordsindict.objects.all()

        except Users.DoesNotExist:
            message = 'User not found'
        except Personaldict.DoesNotExist:
            message = 'Personal dictionary not found'


        if request.method == 'POST':
            if 'buttonDelete' in request.POST:
                personalDict = get_personaldict(username=username)


    data = {
        'words': words_list,
        'message': message,
    }
    return render(request, 'dictionary/myList.html', data)


def get_personaldict(username):
    user = Users.objects.get(name=username)
    personalDict = Personaldict.objects.get(user=user)
    return personalDict