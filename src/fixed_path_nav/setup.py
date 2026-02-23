from setuptools import setup

package_name = 'fixed_path_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vinnu',
    maintainer_email='vinnu@todo.todo',
    description='Fixed circular path infinite loop using Nav2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'path_sender = fixed_path_nav.path_sender:main',
        ],
    },
)
