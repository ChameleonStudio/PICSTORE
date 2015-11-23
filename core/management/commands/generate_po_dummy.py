import sys
import inspect
from django.core.management.base import BaseCommand
from django.db import models
from django.db.models.fields import related


DUMMY_FILE = 'core/dummy.py'


class Command(BaseCommand):
    help = 'Generate po dummy for core'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self._file = open(DUMMY_FILE, 'wt')

    def _print_string(self, s, comment=None):
        print("    _('{}'){}".format(
            s,
            '  # {}'.format(comment) if comment else ''), file=self._file)

    def _print(self, s):
        print(s, file=self._file)

    def handle(self, *args, **options):
        self._print(
            'from django.utils.translation import ugettext_lazy as _\n\n')
        self._print('def dummy():\n')

        # model_modules = [n for n in sys.modules.keys() if n.endswith('.models')]
        model_modules = [
            'core.models',
         ]
        # print(model_modules)
        for module in model_modules:
            # self._print('Handling {}'.format(module))
            for name, obj in inspect.getmembers(
                    sys.modules[module], inspect.isclass):
                if not inspect.isclass(obj) or not issubclass(obj, models.Model):
                    continue
                if not hasattr(obj, '_meta'):
                    self._print('# Warning: no _meta in class {}'.format(name))
                    continue

                instance = obj()

                self._print('\n    # Class: {}'.format(name))
                self._print_string(instance._meta.verbose_name)
                self._print_string(instance._meta.verbose_name_plural)

                for f in instance._meta.get_fields():
                    if hasattr(f, 'verbose_name'):
                        self._print_string(f.verbose_name, f.name)
                    elif not isinstance(f, related.ForeignObjectRel):
                        self._print('# Warning: no verbose_name in field {}.{}'.
                                    format(name, f.name))