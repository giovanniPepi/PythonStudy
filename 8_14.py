def build_car(model, manufacturer, **build_info):
    """Builds a car"""
    build_info['Model name'] = model
    build_info['Manufacturer name'] = manufacturer
    return(build_info)

car = build_car('onix', 'GM', year =2020, color='black', transmission = 'automatic')
print(car)