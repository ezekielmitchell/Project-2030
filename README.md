# Enviro pHAT Sensor Data Collection

Ezekiel A. Mitchell | Seattle University | May 30, 2024

## Table of Contents

- [Introduction](#introduction)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Introduction

This project was created for my data structures and algorithms course for Spring 2024. It utilizes a Raspberry Pi and the Enviro pHAT sensor to collect and log environmental data such as temperature and light levels. The data is collected in real-time and stored in a CSV file for further analysis.

## Hardware Requirements

- Raspberry Pi (any model with GPIO header)
- Enviro pHAT sensor
- MicroSD card with Raspbian installed
- Power supply for Raspberry Pi
- Internet connection for Raspberry Pi

## Software Requirements

- Python 3.x
- Enviro pHAT library
- CSV module (comes with Python standard library)
- Threading module (comes with Python standard library)

## Installation

1. **Set up your Raspberry Pi**:
   - Install [Raspbian](https://www.raspberrypi.com/documentation/computers/getting-started.html) on your Raspberry Pi.
   - Connect the Enviro pHAT sensor to the GPIO header of the Raspberry Pi.


2. **Update and upgrade your system**:
   ```bash
   sudo apt update
   sudo apt upgrade

3. **Install Python & pip (if not already installed):**
    ```bash
    sudo apt install python3 python3-pip

4. **Install the Enviro pHAT library:**
    ```bash
    sudo pip3 install envirophat

5. **Clone the repository:**
    ```bash
    git clone https://gitlab.com/ezekielmitchell/project_2030.git
    cd envirophat-data-collection
    ```

## Usage

1. **Run the script**
    ```bash
    python3 main.py
    ```

    *in the case you are prompted to run the script as root*

    ```bash
    sudo python3 main.py
    ```

2. **Data Logging:**
* The collected data will be saved to envirophat_data.csv in the same directory as the script.

## Project Structure

```bash
    envirophat-data-collection/
│
├── main.py               # Main script for data collection
├── envirophat_data.csv   # Output CSV file with sensor data
├── README.md             # Project documentation
└── requirements.txt      # List of dependencies (if needed)


```