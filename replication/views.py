from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Order, Order_copy

from .models import Order, Order_copy

def index(request):
  order = Order.objects.all().values()
  order_copy = Order_copy.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'Order': order,
    'Order_copy': order_copy,
  }
  return HttpResponse(template.render(context, request))

# def index(request):
#   order_copy = Order_copy.objects.all().values()
#   template = loader.get_template('myfirst.html')
#   context = {
#     'Order_copy': order,
#   }
#   return HttpResponse(template.render(context, request))


def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['firstname']
  y = request.POST['lastname']
  z = request.POST['address']
  w = request.POST['numb']
  order = Order(fname=x, ldate=y, addr = z, num = int(w), bill = int(w)*100)
  order_copy = Order_copy(fname=x, ldate=y, addr = z, num = int(w), bill = int(w)*100)
  order_copy.save()
  order.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, fname):
  order = Order.objects.get(fname=fname)
  order_copy = Order_copy.objects.get(fname=fname)
  order.delete()
  order_copy.delete()
  return HttpResponseRedirect(reverse('index'))

# def delete2(id):
# #   order = Order.objects.get(id=id)
#   order_copy = Order_copy.objects.get(id=id)
# #   order.delete()
#   order_copy.delete()
# #   return HttpResponseRedirect(reverse('index'))