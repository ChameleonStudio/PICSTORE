from django.core.management.commands import makemessages


class Command(makemessages.Command):
    """
    http://jxqdjango.readthedocs.org/en/latest/_sources/topics/i18n/translation.txt
    """
    xgettext_options = makemessages.Command.xgettext_options + ['--keyword=_L']
