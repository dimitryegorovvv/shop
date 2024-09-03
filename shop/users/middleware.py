from .models import YandexUser

class YandexUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                request.yandex_user = YandexUser.objects.get(user=request.user)
            except YandexUser.DoesNotExist:
                request.yandex_user = None
        else:
            request.yandex_user = None

        response = self.get_response(request)
        return response