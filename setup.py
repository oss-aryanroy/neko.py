from distutils.core import setup
from setuptools import find_packages
import os

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
	name='neko.py',
	packages=find_packages('.'),
	version='1.0.0',
	license='MIT',
	description='An API Wrapper for the NekoBot API', 
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Burham',
	author_email='',
	url='https://github.com/Bur-ham/neko.py',
	download_url='',
	keywords=['neko', 'nekobot', 'neko.py', 'nekobot.py', 'neko.py'],
	install_requires=['aiohttp'],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
	]
)
