import setuptools

setuptools.setup(
    name="random_number_generator",
    version="0.1.0",
    author="Devin",
    author_email="devin@example.com",
    description="A simple package to generate a random number",
    long_description="This package provides a simple function to generate a random number. It's useful for applications that need random number generation.",
    long_description_content_type="text/markdown",
    url="https://github.com/user/random_number_generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
