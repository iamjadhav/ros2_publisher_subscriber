from setuptools import setup

package_name = 'data_processor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aditya',
    maintainer_email='adi30jadhav@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "temp_subscriber = data_processor.temp_subscriber:main",
            "speed_subscriber = data_processor.speed_subscriber:main",
            "laser_subscriber = data_processor.laser_subscriber:main"
        ],
    },
)
