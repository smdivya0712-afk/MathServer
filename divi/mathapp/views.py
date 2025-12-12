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