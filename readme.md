Serializers serialization
Serializers serialization is a very important part of DRF star

The main function is to serialize the Python structure into other formats, such as our commonly used JSON.

Add serializers.py to musics and enter the code below

Sometimes I need to customize the serialization.
we have to customize the serialization, that is through the .to_representation(self, value) method, please refer to Custom relational fields for more explanation.


viewset.ModelView set defines all CRUD operations
A viewset provides create, retrieve, update, destroy and list actions

Routers:
DRF provides DefaultRouter to let us quickly establish Routers routing.
Use Register method to register route

Now test the API
RESTful api is a specification
GET: read resource

PUT: Replace resource

DELETE: delete resources

POST: Add resource

PATCH: Update part of the content of the resource
To check if serializers are working perfectly, update view and try in postman.

Viewset:
 combine the logic for a set of related views in a single class
provides actions such as .list() and .create()


Authorization:
In REST API, authorization is very important. If there is no authorization, others will operate your API arbitrarily and unrestrictedly, which is very dangerous.
So DRF provides Authentications

In REST API, authorization is very important. If there is no authorization, others will operate your API arbitrarily and unrestrictedly, which is very dangerous.

So DRF provides Authentications, let's give it a try~

First, please add permission_classes in views.py
Then add api-auth in urls.py
Then in postman, go to Authorization & under basic-auth, give username & password.

I hope I don’t need permissions for GET, but I need permissions for POST. For that:


Parser class:
Parser class mainly can control the received Content-Type,

Say you want the design to allow only one Content-Type like json to be specified.

Setting Parsers is also very simple. If you want global settings, you can add it to settings.py. This means that I only allow the Content-Type to be application/json.

It can also be set for a specific view or viewsets, and you can directly add parser_classes to views.py

When we use REST framework, we will inevitably want to make additional routes. At this time, we can use @detail_route or @list_route.
We can add decorator as the route @detail_route before the method.