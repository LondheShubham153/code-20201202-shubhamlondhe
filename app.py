from aiohttp import web
import logging
import json
import os

from bmi_utils import BMIUtils

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s -%(message)s', 
                    datefmt='%d-%b-%y %H:%M')

routes = web.RouteTableDef()
bmi = BMIUtils()

@routes.get('/')
async def healthcheck_handler(re):
    """
    This end-point allow to test that service is up.
    """
    return web.json_response({'status': 'up'}, status=200)

@routes.get('/bmi')
async def get_handler(request):
    """
    This end-point allows to get the BMI data from json file.
    """
    results = []

    with open('data.json') as f:        #reading the sample json data
        data_samples = json.load(f)

    for sample in data_samples:         #calculating bmi for sample json
        mass = sample["WeightKg"]
        height = sample["HeightCm"]
        gender = sample["Gender"]
        calculated_bmi = bmi.calculate_bmi(mass,height) #using bmi calculator using formula 1
        calculated_range = bmi.calculate_range(calculated_bmi) #using range calculator using table 1
        
        recordData = {
            "Gender":gender,
            "WeightKg":mass,
            "HeightCm":height,
            "Bmi":calculated_bmi,
        }
        data = {**recordData, **calculated_range}   #merging the user data with bmi deductions
        results.append(data)
    response_obj = {
        'message': 'success',
        'results': results
    }
    return web.json_response(response_obj, status=200)

@routes.post('/bmi')
async def post_handler(request):
    """
    This end-point allows to get the BMI data of user input data.
    """
    results = []
    payload = await request.json()      #reading the user input json data from payload
    mass = payload["WeightKg"]
    height = payload["HeightCm"]
    gender = payload["Gender"]
    calculated_bmi = bmi.calculate_bmi(mass,height) #using bmi calculator using formula 1
    calculated_range = bmi.calculate_range(calculated_bmi)  #using range calculator using table 1
    
    recordData = {
        "Gender":gender,
        "WeightKg":mass,
        "HeightCm":height,
        "Bmi":calculated_bmi,
    }
    data = {**recordData, **calculated_range}   #merging the user data with bmi deductions

    response_obj = {
        'message': 'success',
        'result': data
    }
    return web.json_response(response_obj, status=200)

def init_bmi_app(argv=None):
    app = web.Application()     #initializing an instance of web app
    app.add_routes(routes)      #adding url routes to app instance
    web.run_app(app,port=os.environ['PORT'])  #running web app
    return app

app = init_bmi_app()
