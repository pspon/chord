from setuptools import setup, find_packages

setup(
    name="chord",
    version="0.2.3",
    packages=find_packages(),  # Finds all Python packages with __init__.py
    include_package_data=True,  # Ensures non-Python files (templates, CSS, JS) are included
    package_data={"chord": ["default.tmpl"]},  # Ensure template is included
    install_requires=[
        "mako",  # Required for template rendering
        "ipython",  # Required for Jupyter display functionality
    ],
    author="pspon",  # Replace with your name
    author_email="opsinput@gmail.com",  # Replace with your email
    description="A Python package for rendering chord diagrams using Mako templates.",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
