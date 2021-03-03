def my_middleware(get_response):  # This is the name of middleware(my_middleware)
    # All the one time initialization code will be coded here
    print("One time initializations")

    def my_function(request):
        print("The code written here will get executed before view function present in view.py file")
        response = get_response(request)
        print(response)
        print("The code written here will get executed after the view function present in view.py file")
        return response
    return my_function


# Concept of middleware
'''
 The middleware act as a interface between a user and a server. So whenever a user sends a request to
 a server, the request will firt come in middleware(execute all its code) and then the request will go 
 server after that server will send response to user but again the response has to go through the middleware.

 Middleware is a plugin.
'''
