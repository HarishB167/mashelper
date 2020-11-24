from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import MASEntry
import requests
import os

# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

url = "https://docs.google.com/forms/d/e/1FAIpQLSfBWroDCSu8EJjCeRED1blUfEkEmGH-I8QKO4CU703et2KtOQ/formResponse"
data = "entry.1179087314=someunit&entry.1226761935=somequantity&entry.625439819=somematerial&entry.636386930=someremarks&entry.636920682=somelocation&entry.706492584=somedate&fvv=1&draftResponse=%5B%5B%5Bnull%2C706492584%2C%5B%22somedate%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C625439819%2C%5B%22somematerial%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C1226761935%2C%5B%22somequantity%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C1179087314%2C%5B%22someunit%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C636920682%2C%5B%22somelocation%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C636386930%2C%5B%22someremarks%22%5D%0D%0A%2C0%5D%0D%0A%5D%0D%0A%2Cnull%2C%22-4173904548167158905%22%5D%0D%0A&pageHistory=0&fbzx=-4173904548167158905"

def homepage(request):
    # return HttpResponse("pythonprogramming.net homepage! Wow so #amaze.")
	return render(request = request,
                  template_name='main/home.html',
                  context = {"tutorials":MASEntry.objects.all})
	
def submit_mas_entry(request):

	# A list to hold all saved data, to show after submission on submit_confirmed page.
	material_lines = []

	date = request.POST.get("mas_entry_date")
	
	no_of_materials = int(request.POST.get("no_of_materials"))
	print(f"No of materials {no_of_materials} : {type(no_of_materials)}")

	# Saving the First material line.
	material = request.POST.get("mas_entry_material")
	quantity = request.POST.get("quantity")
	unit = request.POST.get("unit")
	location = request.POST.get("location")
	remarks = request.POST.get("remarks")
	response = create_mas_entry(date, material, quantity, unit, location, remarks)
	material_lines.append([material, quantity, unit, location, remarks, response.status_code])
	
	# If there are more material lines then iterate over them and save them.
	if (no_of_materials > 1):
		for i in range(no_of_materials):
			counter = i+1
			if counter == 1:	# Ignoring first as it is already saved.
				continue
			material = request.POST.get(f"mas_entry_material_{counter}")
			quantity = request.POST.get(f"quantity_{counter}")
			unit = request.POST.get(f"unit_{counter}")
			response = create_mas_entry(date, material, quantity, unit, location, remarks)
			material_lines.append([material, quantity, unit, location, remarks, response.status_code])
	
	# material = request.GET.get("mas_entry_material")
	# quantity = request.GET.get("quantity")
	# unit = request.GET.get("unit")
	# location = request.GET.get("location")
	# remarks = request.GET.get("remarks")
	
	# raw_data = data.replace("somedate", date).replace("somematerial", material).replace("somequantity", quantity)
	# raw_data = raw_data.replace("someunit", unit).replace("somelocation", location).replace("someremarks", remarks)
	
	# r = requests.post(url, data=raw_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
	
	# return HttpResponse(f"Date : {date}, Material : {material}, Quantity : {quantity}, Unit : {unit}, location : {location}, remarks : \"{remarks}\" submit entry page.\n Response : {r.status_code}")
	return render(request = request,
				  template_name="main/submit_confirmed.html",
				  context = {"material_lines" : material_lines})


def create_mas_entry(mas_entry_date, mas_entry_material, quantity, unit, location, remarks):
	date = mas_entry_date
	material = mas_entry_material
	
	raw_data = data.replace("somedate", date).replace("somematerial", material).replace("somequantity", quantity)
	raw_data = raw_data.replace("someunit", unit).replace("somelocation", location).replace("someremarks", remarks)
	
	r = requests.post(url, data=raw_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
	
	return r



# https://docs.google.com/forms/d/e/1FAIpQLSfBWroDCSu8EJjCeRED1blUfEkEmGH-I8QKO4CU703et2KtOQ/viewform?usp=pp_url&entry.706492584=somedate&entry.625439819=somematerial&entry.1226761935=somequantity&entry.1179087314=someunit&entry.636920682=somelocation&entry.636386930=someremarks


# Post request
# https://docs.google.com/forms/d/e/1FAIpQLSfBWroDCSu8EJjCeRED1blUfEkEmGH-I8QKO4CU703et2KtOQ/formResponse

# data in request is
# entry.1179087314=someunit&entry.1226761935=somequantity&entry.625439819=somematerial&entry.636386930=someremarks&entry.636920682=somelocation&entry.706492584=somedate&fvv=1&draftResponse=%5B%5B%5Bnull%2C706492584%2C%5B%22somedate%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C625439819%2C%5B%22somematerial%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C1226761935%2C%5B%22somequantity%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C1179087314%2C%5B%22someunit%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C636920682%2C%5B%22somelocation%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C636386930%2C%5B%22someremarks%22%5D%0D%0A%2C0%5D%0D%0A%5D%0D%0A%2Cnull%2C%22-4173904548167158905%22%5D%0D%0A&pageHistory=0&fbzx=-4173904548167158905