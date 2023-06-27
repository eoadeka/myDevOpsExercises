from setuptools import setup, find_packages

description='Python package that performs simply calculations.'
long_description='Python package that performs simply calculations.'
setup(
    name='A simple addition module',
    version='1.0.0',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Elsa Deks',
    license='NIT',
    classifiers= [
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords='simple python calculator',
    packages=find_packages(),
    install_requires=["requests>=2"],
    python_requires=">=3.10"
)