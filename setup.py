import setuptools


setuptools.setup(
    name="django-skd-better-drf",
    version="0.1.8",
    author="Steelkiwi",
    author_email="dobrovolsky@steelkiwi.com",  # temp
    url="https://github.com/steelkiwi/django-skd-better-drf",
    license="MIT",
    description="Steelkiwi Django Tools for DRF",
    keywords="django tools helpers",
    packages=["skd_better_drf", "skd_better_drf.swagger"],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'])
