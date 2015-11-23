#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "online_store.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


# try:
#     if you.is_want_cookie():
#         cookies = you.take_some_cookie()
#         you.enjoy(cookies)
# except CookieNotFoundException():
#     cookies = you.find_cookie()
#     you.share_with_others(cookies)
