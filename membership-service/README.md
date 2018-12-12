# Membership Service

Using Django authentication system: django.contrib.auth.views module for the login and logout views.

Home page has two links: ->Register, ->Login

# Functionalities
## To register onto the membership service : register/

Enter username, email id and password through a form. Username and email id should be unique, if not registration fails.
Post call - (accounts/views/register)

## To login : login/

Using django authentication system, django.contrib.auth.views.login . Enter username and password to login.

## To logout : logout/

Using django authentication system, django.contrib.auth.views.logout
