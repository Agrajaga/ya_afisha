from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from places.models import Place


def show_start(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coord_lng, place.coord_lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": f"/places/{place.id}"
                }
            }
        )
    geo = {
        "type": "FeatureCollection",
        "features": features,
    }
    context = {"places": geo}
    return TemplateResponse(request, "index.html", context)


def get_place_details(_, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = {
        "title": place.title,
        "imgs": [img.image.url for img in place.imgs.order_by('index')],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.coord_lat,
            "lng": place.coord_lng,
        },
    }

    return JsonResponse(
        place_details, 
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False,
        }
    )
