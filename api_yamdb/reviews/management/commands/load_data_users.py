import csv
import os

from django.core.management import BaseCommand
from django.conf import settings

from reviews.models import User


class Command(BaseCommand):
    help = "Заполняет БД из CSV"

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'static/data',
                                 'users.csv')

        #        if User.objects.exists():
        #            print(ALREDY_LOADED_ERROR_MESSAGE)
        #            return

        User.objects.all().delete()

        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)

            for row in reader:
                if reader.line_num == 1:
                    continue

                _, created = User.objects.get_or_create(
                    id=row[0],
                    username=row[1],
                    email=row[2],
                    role=row[3],
                    bio=row[4],
                    first_name=row[5],
                    last_name=row[6]
                )
            f.close()

        print('Данные успешно загружены')
