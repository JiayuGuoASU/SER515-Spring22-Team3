from setuptools import setup
from glob import glob
import os

package_name = 'Anton_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/**')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/**')),
        (os.path.join('share', package_name, 'config'), glob('config/**')),
        (os.path.join('share', package_name, 'world'), glob('world/**')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zhuoran',
    maintainer_email='zhuoran3@asu.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "autoControl = Anton_description.autoControl:main",
            "autoControlJointState = Anton_description.autoControlJointState:main",
            "mC = Anton_description.manullayControl:main",
            "lmC = Anton_description.laserScanAndRotate:main",
            "lmC2 = Anton_description.laserScanAndRotate2:main"
        ],
    },
)
