from django.http import HttpResponse

def user(request, user_id):
    return HttpResponse(f'This is user {user_id}')
