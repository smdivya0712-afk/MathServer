# Ex.04 Design a Website for Server Side Processing
## Date:12.12.2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
math.html
<html>
    <head>
        <title>Vehical Mileage Calculator</title>
        <h1 style="color:black;">
            DIVYA S (25013279)
        </h1>
        <style type="text/css">
        body
{
    background-color:red;
}
.edge {
width:1440px;
margin-left:auto;
margin-right:auto;
padding top: 250px;
padding-left:300px;
}
.box {
display:block;
border:Thick dashed lime;
width:500px;
min-height:300px;
font-size: 20px; 
background-color:blue;
}
.formelt{ 
    color:orange; 
    text-align: center; 
    margin-top: 7px; 
    margin-bottom: 6px;
}
h1
{
color:rgb(255,0,179);
text-align:center;
padding-top: 20px;
}    
</style>
</head>
<body>
    <div class="edge">
    <div class="box">
    <h1>Mileage Calculator</h1>
    <form method="POST">
    {% csrf_token %}
    <div class="formelt">
        Distance : <input type="text" name="distance" value="{{d}}"></input>(in km)<br/>
    </div>
    <div class="formelt">
        Fuel : <input type="text" name="fuel" value="{{f}}"></input>(in litres)<br/>
    </div>
    <div class="formelt">
        <input type="submit" value="calculate"></input><br/>
    </div>
    <div class="formelt">
       Mileage :<input type="text" name="mileage" value="{{mileage}}"></input>km/1<sup>2</sup><br/>
    </div>
    </form>
    </div>
    </div>
</body>
</html>

views.py
from django.shortcuts import render
def mileage(request):
    context={}
    context['mileage'] = "0"
    context['distance'] = "0"
    context['fuel'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        d= request.POST.get('distance', '0')
        f= request.POST.get('fuel', '0')
        print('request=', request)
        print('distance=',d)
        print('fuel=',f)
        a=float(d)
        b=float(f)
        mileage = a / b
        context['mileage']=mileage
        context['distance'] = d
        context['fuel'] = f
        print('mileage=', mileage)
    return render(request, 'mathapp/math.html',context)

    urls.py
    from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('',views.mileage,name="mileage root")
]

```

## OUTPUT - SERVER SIDE:
![alt text](<divi/mathapp/Screenshot (53).png>)

## OUTPUT - WEBPAGE:
![alt text](<divi/mathapp/Screenshot (54).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
