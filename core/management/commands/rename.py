from django.core.management import BaseCommand
import os


class Command(BaseCommand):
    help = 'Rename a Django Project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django Project name')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # a bit of logic to rename the project
        files_to_rename = ['src_files/settings/base.py', 'src_files/wsgi.py', 'manage.py']
        folder_to_rename = 'src_files'

        for f in files_to_rename:
            with open(f, 'r') as file:
                file_data = file.read()

            file_data = file_data.replace('src_files', new_project_name)

            with open(f, 'w') as file:
                file.write(file_data)

            os.rename(folder_to_rename, new_project_name)

            self.stdout.write(self.style.SUCCESS('Project has been renamed to %s' % new_project_name))