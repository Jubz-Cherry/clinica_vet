from django.http import JsonResponse


def clientes(request):
    if request.method == 'GET':
        cliente = {
            'id': 1,
            'name': 'Angelo',
            'email': 'angelo@example.com',
            'telephone': '123456789',
        }
        return JsonResponse(cliente)


def animals(request):
    if request.method == 'GET':
        animal = {
            'id': 1,
            'animal_name': 'Rex',
            'gender': 'Male',
            'specie': 'Dog',
            'race': 'Labrador',
            'age': 3,
        }
        return JsonResponse(animal)


def appointments(request):
    if request.method == 'GET':
        appointment = {
            'id': 1,
            'animal': 'Rex',
            'date': '2024-06-01',
            'hour': '14:00',
            'description': 'Regular check-up',
        }
        return JsonResponse(appointment)