from setuptools import setup, find_packages

setup(
    # Basic Information ===============================================================================
    name='buildautomation',
    version='1.0.0',
    description='Python3 CMake build automation tool.',

    # Classifiers help users find your project by category ===============================================================================
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],

    # Package details ===============================================================================
    packages=find_packages(),  # Automatically find packages in the current directory

    # Dependencies ===============================================================================
    python_requires='>=3.10',  # Python version requirement
    install_requires=[  # List of runtime dependencies
        'os',
        'subprocess',
        'argparse',
        'platform'
    ],
)
