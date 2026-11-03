# 🌳 TreeSense AI

## AI-Based Urban Tree Health Monitoring System

TreeSense AI is an AI-powered urban tree health assessment and
geospatial monitoring platform developed for tree surveys and
environmental monitoring.

The system is designed to combine artificial intelligence,
field observations and GPS information to classify and map
the health condition of urban trees.

## Project Objective

The primary objective is to classify surveyed trees into three
health categories:

- 🟢 Healthy
- 🟠 Moderately Stressed
- 🔴 Diseased / Damaged

## Input Parameters

The system considers:

- Tree and leaf photographs
- Tree species
- Leaf colour
- Canopy density
- Visible disease symptoms
- Trunk damage
- Pest infestation
- GPS location

## AI Approach

The image-classification component can be developed using
transfer-learning models such as:

- MobileNetV2
- EfficientNet
- Convolutional Neural Networks (CNN)

## System Workflow

1. Collect tree and leaf photographs.
2. Label images according to tree health.
3. Divide the dataset into training and testing datasets.
4. Train the image-classification model.
5. Test the model using unseen tree photographs.
6. Calculate prediction accuracy.
7. Record tree survey information.
8. Associate trees with GPS coordinates.
9. Visualise tree health using an interactive map.

## Expected Outputs

TreeSense AI will provide:

- AI-based tree-health classification
- Prediction confidence
- Model accuracy
- Digital tree inventory
- GPS-based tree-health map
- Survey statistics and visualisations

## Application

The initial study is intended for urban tree-health assessment
and mapping on the UPES campus.
