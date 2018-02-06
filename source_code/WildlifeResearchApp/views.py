import datetime
import mysql.connector
import sys
 
from django.template.loader import get_template
from django.template import Context
 
from django.http import HttpResponse
 
def home(request):
    dt = datetime.datetime.now()
    html = '''
         <html><body><h1>From django</h1>
         <p>Time now: %s.
        </body></html>''' % (dt,)
    return HttpResponse(html)
 
def listanimals(request):
        data = dict()
	try:
	        conn = mysql.connector.connect(user="root", password="admin123", host="localhost", database="WildlifeDB")
	        cursor = conn.cursor()
	        cursor.execute("select Animalname, Airtemperature, Color, Otherfeatures, DateTimeOfImageCapture, LocationOfAnimal from WildLifeData")
	        data['animals'] = cursor.fetchall()
	
	        html = get_template('template2.html').render(Context(data))
        	
	except mysql.connector.Error as err:
		print ("Error %s:" % err.args[0])
		sys.exit(1)
	finally:
		if conn:
		   conn.close()
	return HttpResponse(html)
			

def tableAnimals(request):
        data = dict()
        try:
            conn = mysql.connector.connect(user="root", password="admin123", host="localhost", database="WildlifeDB")
            cursor = conn.cursor()
            cursor.execute("select Animalname, Airtemperature, Color, Otherfeatures, DateTimeOfImageCapture, LocationOfAnimal from WildLifeData")
            data['animals'] = cursor.fetchall()

            html = get_template('template_table.html').render(Context(data))

        except mysql.connector.Error as err:
		print ("Error %s:" % err.args[0])
		sys.exit(1)
	finally:
		if conn:
		   conn.close()
	return HttpResponse(html)
