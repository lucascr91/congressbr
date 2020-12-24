from distutils.core import setup
setup(
  name = 'congressbr',
  packages = ['congressbr'], 
  version = '0.0.3',
  license='MIT',
  description = 'Easily download data from Brazilian Congress votations',
  author = 'Lucas Cavalcanti Rodrigues',
  author_email = 'lucas.ecomg@gmail.com', 
  url = 'https://github.com/lucascr91/congressbr.git', 
  download_url = 'https://github.com/lucascr91/congressbr/archive/v_0.0.3.tar.gz', 
  keywords = ['CONGRESS', 'DEMOCRACY', 'BRAZIL'], 
  install_requires=[
          'pandas',
          'pandas_read_xml',
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)