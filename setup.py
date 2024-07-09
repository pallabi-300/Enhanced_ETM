from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('dev_requirements.txt') as f:
    dev_requirements = f.read().splitlines()

setup(
    author='Pallabi Biswas ',
    author_email='pallabiju27@gmail.com',
    python_requires='>=3.9',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Operating System :: MacOS',
        'Operating System :: Unix'
    ],
    description='A package to run embedded topic modelling',
    install_requires=requirements,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='embedded_topic_model',
    name='embedded_topic_model',
    packages=find_packages(include=['embedded_topic_model', 'embedded_topic_model.models', 'embedded_topic_model.utils']),
    setup_requires=dev_requirements,
    test_suite='tests',
    tests_require=dev_requirements,
    url='https://github.com/pallabi-300/my_etm',
    version='1.0.0',
    zip_safe=False,
)
