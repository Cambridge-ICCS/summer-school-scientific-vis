<img src="https://iccs.cam.ac.uk/sites/iccs.cam.ac.uk/files/logo2_1.png"  width="355" align="left">

<br><br><br><br><br>

# ICCS Scientific visualisation with Matplotlib

![GitHub](https://img.shields.io/github/license/Cambridge-ICCS/practical-ml-with-pytorch)
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This repository contains documentation, resources, and code for the Scientific Visualisation with matplotlib session designed and delivered by [Jack Atkinson](https://jackatkinson.net/) ([**@jatkinson1000**](https://github.com/jatkinson1000))
and James Emberton ([**@j-emberton**](https://github.com/j-emberton)) of [ICCS](https://github.com/Cambridge-ICCS).  
The material has been delivered at the [ICCS](https://iccs.cam.ac.uk/events/iccs-summer-school-2024) summer school.  
All materials, including slides and videos, are available such that individuals can cover the course in their own time.

## Contents

- [Learning Objectives](#learning-objectives)
- [Teaching material](#teaching-material)
- [Preparation and prerequisites](#preparation-and-prerequisites)
- [Installation and setup](#installation-and-setup)
- [JOSE Publication](#jose-publication)
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

The 



## Building

The slides are written using quarto.
To build them run:
```
quarto render Scientific_Vis.qmd 
```
from this directory and inspect the output .html file.


## Requirements

To build these slides you need a virtual environment with:

- jupyter
- matplotlib
