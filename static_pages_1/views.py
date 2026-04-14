from django.shortcuts import render
from django.http import HttpResponse

nav = """
    <nav>
        <a href='/'>Home</a> |
        <a href='contact/'>Contact</a>
        <a href='/page1/'>Page 1</a> |
        <a href='/page2/'>Page 2</a> |
        <a href='/page3/'>Page 3</a> |
        <a href='/page4/'>Page 4</a>
    </nav>
"""
name = "John"
age = 45
gains = 100.5634224

home_body = f"""
    <ol>
        <li>Name: {name}</li>
        <li>Age: {age}</li>
        <li>Gains: {gains:.2f}</li>
        <li>
    </ol>
    
"""



def home(request):
    content= """
            <h1>Welcome to my Page</h1>
            <h2>Visit around</h2>
            <p>Enjoy the content</p>
    """
    
    return HttpResponse(nav + content + home_body)

def contact(request):
    return HttpResponse(nav + "Contact Us")

def p1(reqest):
    user = "John"
    login = True
    password_length = 16

    body = f"""
        <ul>
            <li>USER: {user}</li>
            <li>Active: {login}</li>
            <li>Password length: {password_length}</li>
        </ul>
        """
    return HttpResponse(nav + "<h1>Page 1</h1><h2>User Profile</h2><p>Data types examples</p>" + body)  


# Create your views here.
