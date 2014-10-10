from distutils.core import setup

VERSION = '1.0.1'

setup(
    name='githubdate',
    description="Send update statuses to your repository pull-requests.",
    long_description="""
==========
githubdate
==========

You've got dozens of pull-requests on hold. Some of them are ready to be
merged. But as a release manager, you need to warn everyone with "merge"
rights **not to** merge any of these pull-requests. Because you're on a hot
lava field, you have to stabilize things, etc.

Anyway. Just push a "it's not cool to merge this" status. And then, when the
situation is cooler, just send an update with a green light.

License
-------

This is a MIT-licensed software, by Bruno Bord (c) 2014.

    """,
    url='https://github.com/brunobord/githubdate/',
    author="Bruno Bord",
    author_email='bruno@jehaisleprintemps.net',
    license="MIT",
    platforms='any',
    version=VERSION,
    install_requires=['requests', "click"],
    scripts=['bin/githubdate']
)
