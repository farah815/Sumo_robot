from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'robo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name,
            ['package.xml']),
        (os.path.join('share', package_name, 'urdf'),
            glob('urdf/*')),
        (os.path.join('share', package_name, 'meshes', 'STLs'),
            glob('meshes/STLs/*.STL') + glob('meshes/STLs/*.stl')),
        (os.path.join('share', package_name, 'launch'), 
            glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='farah',
    maintainer_email='farohaaa2005@gmail.com',
    description='Robot description package',
    license='Apache-2.0',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [],
    },
)
