from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'research'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', 'msg_interfaces', 'msg'), 
        glob('msg/*.msg')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='antoni',
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
            'position_error = research.position_error:main',
            'analize_position_error = research.analize_position_error:main',
            'rosbag_compare = research.rosbag_compare:main',
        ],
    },
)
