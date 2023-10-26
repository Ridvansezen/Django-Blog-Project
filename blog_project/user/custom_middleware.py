class custom_login_middleware():
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            print("Kullanıcı giriş yaptı {}".format(request.user.username))

        response = self.get_response(request)
        return response