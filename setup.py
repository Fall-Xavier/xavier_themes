from distutils.core import setup, Extension

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = "xavier",
  packages = ["xavier"],
  version = "0.7",
  license ="MIT",
  description = "This library is used to make it easier for developers or users to get random user agents from https://useragents.io.",
  long_description = long_description,
  long_description_content_type = "text/markdown", 
  author = "Fall Xavier",
  author_email = "fallxavier@gmail.com",
  url = "https://github.com/Fall-Xavier/xavier",
  download_url = "https://github.com/Fall-Xavier/xavier/archive/xavier.tar.gz", 
  keywords = ["rich", "module rich", "xavier", "module xavier"], 
  install_requires = [
          "requests",
      ],
  classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.10",
  ],
)
