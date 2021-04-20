from setuptools import setup

setup(
   name='CronParser',
   version='0.1',
   description='Parse crontab entry line to human readable format',
   author='Konrad Partas',
   author_email='kpart@softserveinc.com',
   packages=['cron_parser'],
   install_requires=['celery']
)
