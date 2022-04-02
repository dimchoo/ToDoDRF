from django.core.management.base import BaseCommand
from django.conf import settings
import os
import json
from users.models import UserDRF


class Command(BaseCommand):
    def handle(self, *args, **options):
        json_path = os.path.join(settings.BASE_DIR, 'user_data.json')
        with open(json_path, encoding='UTF-8') as file:
            user_data = json.load(file)
        try:
            UserDRF.objects.bulk_create([UserDRF(**i) for i in user_data])
            print('Users are successfully created!')
        except Exception as error:
            print('Something gone wrong! Check error:\n', error)
