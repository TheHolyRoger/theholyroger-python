from setuptools import setup, find_packages
setup(
    name='theholyroger-python',
    version='0.3',
    description='FriendlyThe Holy RogerJSON-RPC API binding for Python',
    long_description='This package allows performing commands such as listing the current balance'
    ' and sending coins to the Satoshi (original) client from Python. The communication with the'
    ' client happens over JSON-RPC.',
    maintainer='Jeff Cook',
    maintainer_email='jeff@deseret-tech.com',
    url='http://deseret-tech.github.com/theholyroger-python/doc/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial'
    ],
    packages=find_packages("src"),
    package_dir={'': 'src'}
)
