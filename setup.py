from setuptools import setup
setup(
    name ="find_ext",
    version = "0.1",
    py_modules = "find_ext",
    install_requires = [
                    'Click'
                    ],
    entry_points = '''
                    [console_scripts]
                    find_ext=find_ext:find_ext
                   ''',
)
