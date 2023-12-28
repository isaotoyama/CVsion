import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='veesion',
    version='0.1',
    author="Isao Toyama",
    author_email="isao@isaotoyama.com",
    description="OpenCV library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isaotoyama/cvision",
    packages=setuptools.find_packages(),
    keywords=['OpenVision', 'Realtime Webcam', 'Utility', 'Face Detection'],
    install_requires=[
        'opencv-python',
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
