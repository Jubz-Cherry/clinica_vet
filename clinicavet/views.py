from django.http import JsonResponse

def animals(request):
    if request.method == 'GET':
        animal = {
            'id': '1',
            'name': 'Rex',
            'gender': 'Male',
            'race': 'Labrador',
            'age': '3 years',
        }

        return JsonResponse(animal)
    
def donos(request):
    if request.method == 'GET':
        owner = {
            'id': '1',
            'name': 'Angelo',
            'email': 'angelo@example.com',
            'telephone': '123456789',
        }

        return JsonResponse(owner)