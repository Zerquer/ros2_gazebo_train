import os
from setuptools import setup
from glob import glob

package_name = 'gazebo_train_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luigi',
    maintainer_email='luigi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            #'teleop.py = tb3_teleop.teleop:main',
            #'new_teleop.py = tb3_teleop.new_teleop:main',
            #'joy_node.py = tb3_teleop.joy_node:main',
        ],
    },
)

