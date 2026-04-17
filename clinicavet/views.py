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

        return JsonResponse(animals)