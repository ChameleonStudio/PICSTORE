import logging
from django.utils import text
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import Promise


def _class_name_to_human(name):
    return text.camel_case_to_spaces(name).capitalize()


def _var_name_to_human(name):
    return name.replace('_', ' ').capitalize()


def _pluralize(name):
    if name.endswith('y'):
        return name[:-1] + 'ies'
    return name + 's'


def _camel_case_to_underscores(value):
    return text.re_camel_case.sub(r'_\1', value).strip(' _').lower()


def humanize_verbose_names(cls):

    cls._meta.verbose_name = _(_class_name_to_human(cls.__name__))
    cls._meta.verbose_name_plural = _(_pluralize(
        _class_name_to_human(cls.__name__)))

    for f in cls._meta.fields:
        if hasattr(f, 'verbose_name'):
            if isinstance(f._verbose_name, Promise):
                continue
            if not f._verbose_name:
                name = f.name
                verbose_name = _var_name_to_human(name)
                f.verbose_name = _(verbose_name)
                f._verbose_name = _(verbose_name)
        else:
            logging.warning('No verbose name in {} of type {}'.format(f.name, f.__class__.__name__))

    return cls
