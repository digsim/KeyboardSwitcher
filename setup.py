import os
from setuptools import setup, find_packages



packages = ['src']
scripts = ['bin/keyboardswitcher']
data_files = [('/etc/KeyboardSwitcher/', ['etc/keyboardswitcher.cfg',  'etc/logging.conf'])]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="KeyboardSwitcher",
    version="1.1",
    author="Andreas Ruppen",
    author_email="andreas.ruppen@gmail",
    description="Switch Between different physical keyboard layouts",
    license="GPL",
    keywords="Keyboard Layout",
    url="http://diufpc46.unifr.ch/projects/projects/thesis",
    packages=find_packages(),
    scripts=scripts,
    data_files=data_files,
    install_requires=['colorama'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        'Intended Audience :: Developers',
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL License",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
    platforms='any',
    #install_requires=[
    #    'Pylons>=0.97',
    #    'SQLAlchemy==0.5',
    #    'Genshi<=0.4',
    #    'tw.forms!=1.9.2',
    #    'Elixir'
    #],
)
