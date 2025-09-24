from setuptools import find_packages, setup

package_name = 'autopilot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Antoni pialucha',
    maintainer_email='antoni.pialucha@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'azimuth = autopilot.azimuth:main',
            'checkpoints = autopilot.checkpoints:main',
            'add_markers = autopilot.add_markers:main',
        ],
    },
)
