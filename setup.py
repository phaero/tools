from setuptools import setup

version = '0.1.dev0'


setup(name='tools',
      version=version,
      description="Tools and scripts",
      long_description='',
      classifiers=[],
      keywords='',
      author='Johan Segolsson',
      author_email='johan.segolsson@gmail.com',
      url='http://phaero.segolsson.se',
      license='GPL',
      packages=['tools'],
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'checkoutmanager',
          'docutils',
          'dotfiles',
          'eolfixer',
          'pep8',
          'pyflakes',
          'zc.rst2',
          'zest.releaser',
          ],
      entry_points={
        'console_scripts': [
            ],
        },
      )
