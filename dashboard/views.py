from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import render_to_response

from orders.models import Order

# Create your views here.
def dashboard(request):
	# template = loader.get_template('dashboard/dashboard.html')
	# return HttpResponse(template.render())
	# return render_to_response('static/dashboard.html')

	# get data here
	# orders = Order.objects.filter(company_name="Apple")
	# t = orders[0].json_object()
	orders = Order.objects.all()
	data = []

	for o in orders:
		data.append({'company_name': o.company_name, 'quantity': o.quantity})

	return render(request, 'dashboard/dashboard.html', {'apple': str(data)})