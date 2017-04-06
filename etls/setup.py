from distutils.core import setup

setup(
      name='etl_processes',
      version='1.0',
      description='contains etl modules',
      author='Numinous, Inc',
      author_email='gman@gmail.com',
      packages=['indeed', 'eventbrite', 'Zillow'],
)