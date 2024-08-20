from setuptools import setup, find_packages

setup(
    name='ransomware-detection-system',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'watchdog==2.1.3',
        'requests==2.26.0',
        'scikit-learn==0.24.2',
        'pandas==1.3.3'
    ],
    entry_points={
        'console_scripts': [
            'start-monitoring=app.monitor:start_monitoring',
        ],
    },
    author='Your Name',
    description='A real-time ransomware detection system.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ransomware-detection-system',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
