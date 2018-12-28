import setuptools

with open('README.md') as f:
    long_description = f.read()


setuptools.setup(
    name='gauth',
    version='0.1',
    scripts=['gauth'],
    author='Joshua Smith',
    author_email='whoopsie@example.com',
    description='A package to assist with Google OAuth',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/joshuasmith2021/gauth',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU GPLv3',
        'Operating System :: OS Independent'
    ]
)
