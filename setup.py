from distutils.core import setup

setup(
    name='pyvision',
    packages=['pyvision'],
    version='1.0',
    license='MIT',
    description='Py OpenVision -  Library',
    author='Isao Toyama',
    author_email='isao@isaotoyama.com',
    url='https://github.com/isaotoyamqa',
    keywords=['OpenVision', 'Realtime Webcam', 'Utility', 'Face Detection'],
    install_requires=[
        'opencv-python',
        'numpy'
    ],
    python_requires='>=3.6',  # Requires any version >= 3.6

    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
    ],
)
