# from functools import wraps
# from django.shortcuts import redirect
#
#
# def authorization_check(function):
#     @wraps(function)
#     def wrap(request, *args, **kwargs):
#         path = request.path
#         authorization_list = authorization_dict[request.user.profile.access]
#         allowed_urls = [i['urls'] for i in authorization_list]
#         if path in allowed_urls:
#             return function(request, *args, **kwargs)
#         else:
#             return redirect('no_access')
#
#     return wrap
