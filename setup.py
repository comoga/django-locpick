import os
from setuptools import setup, find_packages


try:
    f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-locpick',
    version='0.2',
    url="https://github.com/comoga/django-locpick",
    description='',
    long_description=long_description,
    author='Comoga Django Team',
    author_email='dev@comoga.cz',
    license='BSD',
    keywords='django admin google maps'.split(),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    include_package_data=True,
    packages=find_packages(),
)

