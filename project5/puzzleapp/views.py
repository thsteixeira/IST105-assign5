import random
from django.shortcuts import render

from .forms import PuzzleForm, GuessForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def puzzle(request):
    messages = []
    if request.method == "POST":
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            if number % 2 == 0:
                sqr_root = number ** 0.5
                messages.append(f"The number {number} is even and its square root is: {sqr_root}")
            else:
                cube = number ** 3
                messages.append(f"The number {number} is odd and its cube is: {cube}")
            text = form.cleaned_data['text']
            binary_text = ' '.join(format(ord(char), '08b') for char in text)
            vowels = "aeiouAEIOU"
            vowels_count = sum(1 for char in text if char in vowels)
            messages.append(f"Binary representation of '{text}': {binary_text}")
            messages.append(f"Number of vowels in '{text}': {vowels_count}")
            return render(request, 'puzzle.html', {'form': form, 'messages': messages})
    else:
        form = PuzzleForm()
    return render(request, 'puzzle.html', {'form': form, 'messages': messages})

def guess(request):
    if 'random_number' not in request.session:
        request.session['random_number'] = random.randint(1, 100)
        request.session['attempts'] = 5  # Set the number of attempts

    random_number = request.session['random_number']
    remaining_attempts = request.session['attempts']
    message = ""

    if request.method == "POST":
        form = GuessForm(request.POST)
        if form.is_valid() and remaining_attempts > 0:
            guess = form.cleaned_data['guess']

            if guess == random_number:
                message = "Congratulations! You guessed the number!"
                del request.session['random_number']
                del request.session['attempts']
            else:
                request.session['attempts'] -= 1
                remaining_attempts = request.session['attempts']
                if remaining_attempts == 0:
                    message = f"You lost! The correct number was {random_number}."
                    del request.session['random_number']
                    del request.session['attempts']
                elif guess < random_number:
                    message = f"Try a higher number! Attempts left: {remaining_attempts}"
                else:
                    message = f"Try a lower number! Attempts left: {remaining_attempts}"
    else:
        form = GuessForm()

    return render(request, "guess.html", {"form": form, "message": message})