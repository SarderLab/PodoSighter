PodoSighter (V1): A cloud-based tool for label-free podocyte detection and quantification in renal tissue sections 
=============================================================================================

Podocytes play a crucial role in maintaining the structural and functional integrity of the glomerulus. Several renal diseases like diabetic kidney disease, minimal change disease, glomerulonephritis, etc. lead to podocyte injury, causing their eventual detachment from the glomerular basement membrane. Therefore, quantifying podocyte loss is of high clinical significance, especially in tracking disease progression. The current clinical standard for podocyte detection involves their manual identification from standard periodic acid-Schiff (PAS)-stained renal sections, which are extremely subjective and time consuming. In research practice, these limitations can be overcome by the use of podocyte-specific antibodies like p57, WT1, nephrin, etc., which is expensive and not in routine clinical practice. To address these limitations, we have developed 'PodoSighter', a cloud-based application to identify podocytes from brightfield images of renal tissue sections, stained using the standard clinical stain of PAS counterstained with hematoxylin. Our application framework encompasses two independent pipleines, utilizing two state-of-the-art deep learning techniques: convolutional neural network (CNN) and generative adversarial network (GAN). The PodoSighter pipeline is deployed as two independent plugins (PodoSighter_CNN and PodoSighter_pix2pix), using HistomicsTK, creating an online, interactive platform enabling multiple users from various locations to quantify podocytes on their respective PAS-stained whole slide images (WSIs). This pipeline not only detects podocyte nuclei, but also generates a CSV file containing the podocyte counts, apparent mean nuclear caliper diameters, true nuclear caliper diameters, and podocyte volume densities (based on the Wiggins method).

This repository contains the PodoSighter pipeline, developed by Darshana Govind (d8@buffalo.edu) at Sarder lab, University at Buffalo, (for the automated detection and quantification of podocytes from PAS-stained renal tissue sections) via Google's deeplab v3+ architecture (https://github.com/tensorflow/models/tree/master/research/deeplab) and the pix2pix conditional GAN developed by Isola et al (https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).


Running the PodoSighter pipeline
--------------------------------

In order to run the PodoSighter plugin on your PAS-stained renal section, follow the following steps:

1 - Download the PodoSighter codes to your computer

2 - In MainCode.py, enter the user parameters and the locations of the PAS whole slide image and the glomerulus annotation (.xml) file.

3 - In MainCode.py, enter the locations of the trained CNN or pix2pix models.

3 - In MainCode.py, specify 'METHOD' as 'CNN' or 'pix2pix' to select the respective pipelines.

Once steps 1-3 are done, the pipeline can be implemented by executing the following code in the command line:

```
$ python PodoSighter.py
```

## Input/output parameters

**PodoSighter_CNN**

- **Data Folder**: Select a temporary folder location where the glomeruli can be cropped and tested on. This folder will automatically be deleted after analysis.
- **Input Image**: Select the whole slide image (WSI) to be analyzed
- **Input Annotation File 1**: Select the xml file containing glomerulus annotations (either manually annotated or automatically extracted using the HAIL pipeline (...) 
- **Model**: Select the trained model
- **Model checkpoint**: Select the latest checkpoint of trained model
- **Model idx**: Select the index file of trained model 
- **Output Annotation File**: Select the name of output xml file (marking podocytes)
- **Csv_file_name**: Select the name of the output csv file containing the podocyte counts, mean nuclear caliper diameters, true caliper diameters, correction factors, and podocyte volume densities (based on Wiggins method)

**PodoSighter_pix2pix**

- **Data Folder**: Select a temporary folder location where the glomeruli can be cropped and tested on. This folder will automatically be deleted after analysis.
- **Input Image**: Select the whole slide image (WSI) to be analyzed
- **Input Annotation File 1**: Select the xml file containing glomerulus annotations (either manually annotated or automatically extracted using the HAIL pipeline (...) 
- **Trained Generator Model**: Select the trained generator model
- **Trained Discrimminator Model**: Select the trained discriminator model
- **Output Annotation File**: Select the name of output xml file (marking podocytes)
- **Csv_file_name**: Select the name of the output csv file containing the podocyte counts, mean nuclear caliper diameters, true caliper diameters, correction factors, and podocyte volume densities (based on Wiggins method)



**User parameters for both plugins**

Since each WSI is different in terms of staining, imaging, resolution, etc., we provide the option for users to adjust the parameters to generate optimal results for their       respective WSIs. 
Listed below are the different parameters and their definitions:

- **PASnucleiThreshold**: This parameter selects the threshold to segment hematoxylin stained nuclei (ranging from 0 to 1).
- **gauss_filt_size**: This parameter blurs the PAS image prior to application of threshold.
- **disc_size**: This parameter specifies the disc size of the structuring element to perform morphological opening of segmented nuclei. 
- **resolution**: This parameter can be used to specify if the analysis should be done in high resolution (0) or a downsampled (1) version of the WSI to save time. 
- **size_thre**: This parameter is used to remove unwanted noise from the segmented nuclei.
- **watershed_thre**: This parameter sets the distance parameter for the watershed segmentation of segmented nuclei (ranging from 0 to 1).
- **Tissue thickness**: The tissue thickness in microns, as entered by the user.


Listed below are the parameters we used for our study:

| Dataset  | species | PASnucleiThreshold  | gauss_filt_size | disc_size  | resolution  | size_thre  | watershed_thre |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Mouse WT1 data            | mouse       | 0.5                | 5                | 6             | 0               | 400           | 0.2                |
| Mouse p57 data            | mouse       | 0.5                | 5                | 6             | 0               | 400           | 0.2                |
| Rat WT1 data              | rat         | 0.4                | 5                | 4             | 0               | 300           | 0.2                |
| Rat p57 data              | rat         | 0.4                | 5                | 4             | 0               | 300           | 0.2                |
| Human autopsy WT1 data    | human       | 0.5                | 5                | 6             | 0               | 400           | 0.2                |
| Human autopsy p57 data    | human       | 0.5                | 5                | 6             | 0               | 400           | 0.2                |
| Human pediatric WT1 data  | human       | 0.4                | 5                | 6             | 0               | 400           | 0.2                |
| Human pediatric p57 data  | human       | 0.4                | 5                | 6             | 0               | 400           | 0.2                |


