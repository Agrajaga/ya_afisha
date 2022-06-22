from pathlib import Path
from typing import Any, Optional
from urllib.parse import unquote, urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandParser
from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Получить локацию с картинками'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('json_url', type=str)

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        try:
            location_response = requests.get(options['json_url'])
            location_response.raise_for_status()
            location = location_response.json()
            image_links = location['imgs']

            place, is_created = Place.objects.get_or_create(
                title=location['title'],
                coord_lng=location['coordinates']['lng'],
                coord_lat=location['coordinates']['lat'],
                defaults={
                    'description_short': location['description_short'],
                    'description_long': location['description_long'],
                }
            )
            if not is_created:
                place.imgs.all().delete()

            for index, img_link in enumerate(image_links):
                try:
                    filename = unquote(Path(urlparse(img_link).path).name)
                    image_response = requests.get(img_link)
                    image_response.raise_for_status()
                    image_content = ContentFile(image_response.content)

                    place_image = PlaceImage(index=index, place=place)
                    place_image.image.save(filename, content=image_content)
                except requests.exceptions.HTTPError:
                    self.stderr.write(self.style.ERROR(
                        f'Картинка {img_link} не найдена'))
            self.stdout.write(self.style.SUCCESS('Локация загружена!'))
        except requests.exceptions.HTTPError:
            self.stderr.write(self.style.ERROR(
                f'Описание локации {options["json_url"]} недоступно'))
        except KeyError as e:
            self.stderr.write(self.style.ERROR(
                f'В описании локации не найдено поле "{e.args[0]}"'))
