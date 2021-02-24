import sys

from django.core.management import call_command
from configure import configure_django


configure_django()
call_command(*sys.argv[1:])
