import sys
from unittest import TestSuite

from configure import configure_django


configure_django()


default_labels = [
    "stonegrading.tests",
]


def get_suite(labels=default_labels):
    """
    Gets and run test cases. This is somewhat similar to what django's test management command does
    :param labels:
    :returns:
    """
    from django.test.runner import DiscoverRunner

    runner = DiscoverRunner(verbosity=1)

    failures = runner.run_tests(labels)
    if failures:
        sys.exit(failures)

    return TestSuite()  # This is return in case it is called from setuptools


if __name__ == "__main__":
    labels = default_labels
    if len(sys.argv[1:]) > 0:
        labels = sys.argv[1:]

    get_suite(labels)