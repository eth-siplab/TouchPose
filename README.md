# Research repository for TouchPose

[Karan Ahuja](https://www.karan-ahuja.com/), [Paul Streli](https://www.paulstreli.com) and [Christian Holz](https://www.christianholz.net)<br/>
[Sensing, Interaction & Perception Lab](https://siplab.org) <br/>
Department of Computer Science, ETH Zürich

This is the research repository for the ACM UIST 2021 Paper: "TouchPose: Hand Pose Prediction, Depth Estimation, and Touch Classification from Capacitive Images." This repository contains the part of the dataset we collected on pairs of capacitive touch images and depth maps of fingers and hands.

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]


## Dataset

The part of the dataset on capacitive touch images and depth maps will be released soon.


## Code

The code can be found in the src folder. The model weights for estimating depth maps from capacitive touch images will be released soon.


## Publication reference

Karan Ahuja, Paul Streli and Christian Holz. 2021. TouchPose: Hand Pose Prediction, Depth Estimation, and Touch Classification from Capacitive Images. Proceedings of the 34th Annual ACM Symposium on User Interface Software and Technology (UIST ’21). Association for Computing Machinery, New York, NY, USA, 13 pages. DOI: https://doi.org/10.1145/3472749.3474801

### Direct links

* [TouchPose paper PDF](https://siplab.org/papers/uist2021-touchpose.pdf)
* [TouchPose video](https://www.youtube.com/watch?v=CGnS18uGwC4)
* [TouchPose project page](https://siplab.org/projects/TouchPose)

### BibTeX reference

```
@inproceedings{10.1145/3472749.3474801,
  author = {Ahuja, Karan and Streli, Paul and Holz, Christian},
  title = {TouchPose: Hand Pose Prediction, Depth Estimation, and Touch Classification from Capacitive Images},
  year = {2021},
  isbn = {9781450386357},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3472749.3474801},
  booktitle = {Proceedings of the 34th Annual ACM Symposium on User Interface Software and Technology},
  numpages = {13}
}
```

## Abstract

Today's touchscreen devices commonly detect the coordinates of user input using capacitive sensing. Yet, these coordinates are the mere *2D manifestations* of the more complex 3D configuration of the whole hand&mdash;a sensation that touchscreen devices so far remain oblivious to  In this work, we introduce the problem of reconstructing a 3D hand skeleton from capacitive images, which encode the sparse observations captured by touch sensors. These low-resolution images represent intensity mappings that are proportional to the distance to the user's fingers and hands. 
We present the first dataset of capacitive images with corresponding depth maps and 3D hand pose coordinates, comprising 65,374 aligned records from 10 participants. We introduce our supervised method TouchPose, which learns a 3D hand model and a corresponding depth map using a cross-modal trained embedding from capacitive images in our dataset. We quantitatively evaluate TouchPose's accuracy in touch contact classification, depth estimation, and 3D joint reconstruction, showing that our model generalizes to hand poses it has never seen during training and that it can infer joints that lie outside the touch sensor's volume. 
Enabled by TouchPose, we demonstrate a series of interactive apps and novel interactions on multitouch devices. These applications show TouchPose's versatile capability to serve as a *general-purpose model*, operating independent of use-case, and establishing 3D hand pose as an integral part of the input dictionary for application designers and developers. We also release our dataset, code, and model to enable future work in this domain.

![TouchPose illustration of estimating the 3D hand pose and the depth image from a capacitive input image.](https://siplab.org/covers/touchpose.jpg)


## Disclaimer

The dataset and code in this repository is for research purposes only. If you plan to use either of these for commercial purposes, please [contact us](https://siplab.org/contact). If you are interested in a collaboration with us around this topic, please also [contact us](https://siplab.org/contact).


```
THE PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT WITHOUT ANY
WARRANTY. IT IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE
QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE
DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
CORRECTION.

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW THE AUTHOR WILL BE LIABLE TO YOU
FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL
DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT
NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES
SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH
ANY OTHER PROGRAMS), EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.
```

## License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

