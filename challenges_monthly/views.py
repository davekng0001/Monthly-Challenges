from django.shortcuts import render, redirect


def challenge_redirect(request):
    return redirect('/challenges')