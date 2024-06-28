<img src="https://iccs.cam.ac.uk/sites/iccs.cam.ac.uk/files/logo2_1.png"  width="355" align="left">

<br><br><br><br><br>

# ICCS Scientific visualisation

![GitHub](https://img.shields.io/github/license/Cambridge-ICCS/summer-school-scientific-vis)
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This repository contains documentation, resources, and code for the Scientific Visualisation with matplotlib session designed and delivered by [Jack Atkinson](https://jackatkinson.net/) ([**@jatkinson1000**](https://github.com/jatkinson1000))
and James Emberton ([**@j-emberton**](https://github.com/j-emberton)) of [ICCS](https://github.com/Cambridge-ICCS).  
This material was originally prepared for the [ICCS](https://iccs.cam.ac.uk/events/iccs-summer-school-2024) 2024 summer school.  
All materials, including slides and videos, are available such that individuals can cover the course in their own time.

## Contents

- [Learning Objectives](#learning-objectives)
- [Teaching material](#teaching-material)
- [Preparation and prerequisites](#preparation-and-prerequisites)
- [Installation and setup](#installation-and-setup)
- [License information](#license)
- [Contribution Guidelines and Support](#contribution-guidelines-and-support)

# Learning Objectives

The key learning objective from this workshop is to build skills in scientific visualisation through python and its libraries.

However, more specifically we aim to:

summarise key considerations when visualising scientific data,
provide an understanding of the Matplotlib package and how to use it effectively,
introduce the Cartopy package and show how it extends Matplotlib functionality for geospatial plotting,
introduce common climate data formats and show how these can be parsed to generate plottable data,
and encourage good research software engineering (RSE) practice while using code to generate scientific visualisations.

# Teaching material

The course material is supplied as Quarto markdown slides with an accompanying jupyter lab notebook.

Slides can be found in the  [presentation](presentation/) directory.

Notebook can be found in the [notebook](notebook/) directory.

## Preparation and pre-requisites

To get the most out of the session we assume a basic understanding in a few areas and 
for you to do some preparation in advance.
Expected knowledge is outlined below, along with resources for reading if you are unfamiliar.

### Python
The course will be taught in python using netCDF4, Matplotlib and Cartopy python packages.
Whilst no prior knowledge of these python packages is expected we assume users are familiar with the basics of Python3.
This includes:
- Basic mathematical operations
- Writing and running scripts/programs
- Writing and using functions
- The concept of [object orientation](https://eli5.gg/Object-oriented%20programming)  
  i.e. that an object, e.g. a dataset, can have associated functions/methods associated with it.
- Familiarity with the [concept of a jupyter notebook](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/index.html)

### git and GitHub
You will be expected to know how to
- clone and/or fork a repository

The [workshop from the 2022 ICCS Summer School](https://www.youtube.com/watch?v=ZrwzK4CnJ3Q) 
should provide the necessary knowledge.

### Preparation
In preparation for the course please ensure that your computer contains the following:
- A text editor - e.g. vim/[neovim](https://neovim.io/), [gedit](https://gedit.en.softonic.com/), [vscode](https://code.visualstudio.com/), [sublimetext](https://www.sublimetext.com/) etc. to open and edit code files
- A terminal emulator - e.g. [GNOME Terminal](https://help.gnome.org/users/gnome-terminal/stable/), [wezterm](https://wezfurlong.org/wezterm/index.html), [Windows Terminal (windows only)](https://learn.microsoft.com/en-us/windows/terminal/), [iTerm (mac only)](https://iterm2.com/)
- python virtual environment (see [Installation and setup](#installation-and-setup))

Note for Windows users: _We have linked suitable applications for windows in the above lists.
However, you may wish to refer to [Windows' getting-started with python information](https://learn.microsoft.com/en-us/windows/python/beginners)
for a complete guide to getting set up on a Windows system._

If you require assistance or further information with any of these please reach out to
us before a training session.

## Building

The slides are written using quarto.
To build them run:
```
quarto render Scientific_Vis.qmd 
```
from this directory and inspect the output .html file.


## Installation and setup

There are three options for participating in this workshop for which instructions are provided below:

* via a [local install](#local-install)
* on [Google Colab](#google-colab)
* on [binder](#binder)

We recommend the [local install](#local-install) approach, especially if you forked
the repository, as it is the easiest way to keep a copy of your work and push back to GitHub.

However, if you experience issues with the installation process or are unfamiliar with
the terminal/installation process there is the option to run the notebooks in
[Google Colab](#google-colab) or on [binder](#binder).

### Local Install

#### 1. Clone or fork the repository
Navigate to the location you want to install this repository on your system and clone
via https by running:
```
git clone https://github.com/Cambridge-ICCS/summer-school-scientific-vis.git
```
This will create a directory `summer-school-scientific-vis/` with the contents of this repository.

Please note that if you have a GitHub account and want to preserve any work you do
we suggest you first [fork the repository](https://github.com/Cambridge-ICCS/summer-school-scientific-vis/fork) 
and then clone your fork.
This will allow you to push your changes and progress from the workshop back up to your
fork for future reference.

#### 2. Create a virtual environment
Before installing any Python packages it is important to first create a Python virtual environment.
This provides an insulated environment inside which we can install Python packages 
without polluting the operating systems' Python environment.

If you have never done this before don't worry: it is *very* good practise, especially 
when you are working on multiple projects, and easy to do.

```
python3 -m venv SVvenv
```
This will create a directory called `SVvenv` containing software for the virtual environment.
To activate the environment run:
```
source SVvenv/bin/activate
```
You can now work on python from within this isolated environment, installing packages
as you wish without disturbing your base system environment.

When you have finished working on this project run:
```
deactivate
```
to deactivate the venv and return to the system python environment.

You can always boot back into the venv as you left it by running the activate command again.

#### 3. Install dependencies

It is now time to install the dependencies for our code, for example PyTorch.
The project has been packaged with a [`pyproject.toml`](pyproject.toml) so can be installed in one go.
From within the root directory in a active virtual environment run:
```
pip install .
```
This will download the relevant dependencies into the venv as well as setting up the
datasets that we will be using in the course.\

#### 4. Run the notebook

From the current directory, launch the jupyter notebook server:
```
jupyter notebook
```
This command should then point you to the right location within your browser to use the notebook, typically [http://localhost:8888/](http://localhost:8888/).

## License

The code materials in this project are licensed under the [MIT License](LICENSE).

The teaching materials are licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

## Contribution Guidelines and Support

If you spot an issue with the materials please let us know by
[opening an issue](https://github.com/Cambridge-ICCS/summer-school-scientific-vis/issues/new/choose)
here on GitHub clearly describing the problem.

If you are able to fix an issue that you spot, or an
[existing open issue](https://github.com/Cambridge-ICCS/summer-school-scientific-vis/issues)
please get in touch by commenting on the issue thread.

Contributions from the community are welcome.
To contribute back to the repository please first
[fork it](https://github.com/Cambridge-ICCS/summer-school-scientific-vis/fork),
make the neccessary changes to fix the problem, and then open a pull request back to
this repository clerly describing the changes you have made.
We will then preform a review and merge once ready.

If you would like support using these materials, adapting them to your needs, or
delivering them please get in touch either via GitHub or via
[ICCS](https://github.com/Cambridge-ICCS).