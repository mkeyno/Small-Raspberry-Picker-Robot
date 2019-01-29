
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FruitDetector",
    version="0.0.1-edf01",
    author="Mehrdad Keyno",
    author_email="hrsk1980@gmail.com",
    description="A primilarly fuction to detect berries on the camera",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkeyno/Small-Raspberry-Picker-Robot/blob/master/firmware/OpenCV",
    packages=setuptools.find_packages(),
    install_requires=[
          'numpy',
          'cv2',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
