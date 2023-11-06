from setuptools import setup, find_packages

setup(
    name='nine_relay_linux_python',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'hidapi'
    ],
    author='Bluewhitep',
    author_email='20318684+bluewhitep@users.noreply.github.com',
    description='Use python control ADUBRU9 board on linux',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bluewhitep/nine_relay_linux_python',  # 可以是你的代码仓库链接
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)
