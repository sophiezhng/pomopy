import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pomopy",
    version="0.0.1",
    author="Sophie Zhang",
    author_email="sophie.zhangg@icloud.com",
    description="Pomopy is a fun ASCII-art-filled, customizable time-management solution to optimize productivity.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sophiezhng/pomopy",
    project_urls={
        "Bug Tracker": "https://github.com/sophiezhng/pomopy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    platforms='any',
    scripts=['pomopy'],
    data_files=['tomato.txt','about.txt', 'preferences.json', 'troll.txt', 'banner.txt', 'digital_watch_alarm.mp3'],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
