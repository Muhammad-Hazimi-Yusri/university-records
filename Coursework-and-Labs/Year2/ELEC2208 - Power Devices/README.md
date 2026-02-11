# ELEC2208 -- Power Devices

**Module:** Power Devices
**Type:** Individual Coursework and Laboratory Work
**Academic Year:** Year 2
**Duration:** Full Academic Year (Semester 1 & 2)
**Assessment:** Theory Examination + CAD Coursework + Laboratory Work (EE75)

## Module Overview

ELEC2208 Power Devices is a comprehensive Year 2 module covering the fundamentals of power electronics and motor drive systems. The module is divided into two complementary parts:

**Part 1: Power Electronics** (Taught by Prof. Yoshiharu Takeshita)
Focuses on the characteristics, operation, and applications of power semiconductor devices including diodes, thyristors, transistors, and their applications in power converters, rectifiers, inverters, and DC-DC converters.

**Part 2: Motor Drive Systems** (Taught by Prof. Suleiman Abu-Sharkh)
Covers electromagnetic and mechanical fundamentals of electrical machines, control strategies for DC and AC motors, and the integration of power electronics with motor drive systems.

The module combines theoretical understanding with practical skills through CAD-based mechanical design coursework and hands-on embedded systems laboratory work focused on BLDC motor control.

## Key Topics Covered

### Power Electronics Fundamentals

- **Power Semiconductor Devices**
  - Diodes and their switching characteristics
  - Thyristors (SCRs, TRIACs) and gate control
  - Power transistors (BJTs, MOSFETs, IGBTs)
  - Heating and cooling considerations for power devices

- **Power Converters and Control**
  - AC voltage controllers (phase control)
  - Rectifiers (single-phase and three-phase, controlled and uncontrolled)
  - Inverters (voltage source and current source)
  - DC-DC converters (buck, boost, buck-boost topologies)
  - Cycloconverters for frequency conversion

### Motor Drive Systems

- **Electromagnetic and Mechanical Fundamentals**
  - Magnetic circuits and electromagnetic force
  - Torque production and mechanical dynamics
  - Motor-load matching and mechanical time constants
  - Transducers and feedback systems

- **Motor Control Strategies**
  - DC motor drives and control (armature and field control)
  - AC motor drives (induction motors and synchronous motors)
  - Variable frequency drives (VFDs)
  - Brushless DC (BLDC) motor control

## Coursework Component: Mechanical Design (CAD)

### Overview
The coursework involved designing a complete mechanical positioning system using AutoCAD, integrating various electromechanical components including motors, linear actuators, encoders, and limit switches.

### Design Components

**Primary Assemblies:**
- **Carriage Assembly** - Movable platform carrying the load
- **Slideway System** - Linear guide rails for precision motion
- **Load Interface** - Mounting system for payload attachment
- **Full Assembly** - Complete integrated system with all components

### Technical Approach

- Designed mechanical components using **AutoCAD** (DWG format)
- Selected and integrated off-the-shelf electromechanical components:
  - **BLDC Motor:** Kollmorgen AKM11X series
  - **Linear Actuator:** THK ball screw mechanism
  - **Encoder:** Omron E6B2-CWZ6C 2000P/R rotary encoder
  - **Limit Switches:** End-of-travel safety switches
  - **Couplings and Mounting Hardware:** Various standard components

- Created engineering drawings showing:
  - Dimensional specifications and tolerances
  - Assembly relationships and constraints
  - Component mounting details
  - Electrical and mechanical interfaces

### Skills Demonstrated

- Mechanical CAD design and drafting
- Component selection and specification
- System integration and assembly planning
- Engineering documentation and technical drawings
- Understanding of mechatronic system requirements

## Laboratory Work: BLDC Motor Control (EE75)

### Objective
This laboratory exercise (worth 5% of module marks) provides hands-on introduction to BLDC motor drive systems using a three-phase inverter/electronic commutator controlled by Hall sensor signals. Through guided experimental work, the lab demonstrates how to integrate power electronics with microcontroller-based control to operate a brushless DC motor.

### Implementation

Following the lab manual instructions, the exercise involves:

**Hardware Platform:** Il Matto microcontroller with experimental platform
**Programming Language:** C (using AVRDUDE with C232HM patch)
**Control Method:** Six-step commutation with Hall effect sensor feedback
**Approach:** Step-by-step guided implementation building from PWM generation to full motor control

### Lab Exercise Components

The laboratory work progresses through three main sections:

1. **Three-Phase Voltage Source Inverter (Six Step Operation)**
   - Program Il Matto to generate 6 PWM signals with specified frequency and dead-time
   - Construct three-phase inverter using MOSFETs and gate drivers
   - Verify correct operation with oscilloscope measurements

2. **Rotor Position and Hall Sensor Analysis**
   - Manually energize stator windings using bench power supply
   - Observe and record Hall sensor signals (H1, H2, H3) at different rotor positions
   - Construct commutation tables for clockwise and counter-clockwise rotation

3. **BLDC Motor Control Implementation**
   - Program Il Matto to read Hall sensor signals and generate appropriate PWM patterns
   - Implement commutation logic based on experimentally derived tables
   - Test motor operation and observe speed control through voltage adjustment

**Code files** ([bldc.c](EE75/bldc.c), [pwm.c](EE75/pwm.c), [debug.h](EE75/debug.h)) contain the implemented firmware following lab manual specifications, with original reference code preserved in `original codes/` folder.

### Key Concepts Explored

- **Hall sensor operation** - Understanding open-collector Hall effect sensors and their relationship to rotor position
- **Commutation sequences** - Six-step commutation patterns for BLDC motors in both rotation directions
- **Dead-time implementation** - Preventing shoot-through in three-phase inverter bridges
- **PWM control** - Generating appropriate gate drive signals for power MOSFETs
- **Experimental validation** - Manually determining commutation tables through hands-on testing

### Laboratory Documentation

- **Lab Prints** - Detailed lab reports documenting experimental setup, observations, and results
- **Notes** - Laboratory instruction manual and task specifications

## Technical Skills Demonstrated

### CAD & Mechanical Design
- **AutoCAD proficiency** - 2D and 3D mechanical design
- **Component selection** - Electromechanical actuators, motors, sensors
- **Engineering drawings** - Dimensional specifications, assembly drawings, part details
- **System integration** - Mechanical and electrical interface design
- **Standards compliance** - Technical documentation following engineering conventions

### Embedded Systems & Firmware Development
- **C programming** - Embedded firmware for microcontroller applications
- **PWM control** - Timer configuration, duty cycle modulation, frequency selection
- **Motor control algorithms** - BLDC six-step commutation, Hall sensor interpretation
- **Real-time systems** - Interrupt-driven event handling, timing-critical code
- **Hardware interfacing** - GPIO, timers, ADC, communication peripherals
- **Debugging techniques** - Serial debugging, oscilloscope analysis, system troubleshooting

### Power Electronics & Motor Drives
- **Power semiconductor devices** - Understanding of diodes, thyristors, MOSFETs, IGBTs
- **Power converter topologies** - Rectifiers, inverters, DC-DC converters, cycloconverters
- **Motor drive systems** - DC motor control, AC motor control, BLDC motor control
- **Control strategies** - Open-loop and closed-loop control, PWM modulation techniques
- **Thermal management** - Heat sink design, thermal calculations for power devices
- **System analysis** - Load matching, efficiency calculations, transient analysis

### Documentation & Technical Communication
- **Technical report writing** - Lab reports, design documentation, coursework reports
- **Engineering diagrams** - Circuit diagrams, block diagrams, assembly drawings
- **Note-taking and synthesis** - Comprehensive notes from lectures covering complex topics
- **Problem-solving documentation** - Recording design decisions, troubleshooting steps, and results

## Module Materials

This repository contains comprehensive materials for the ELEC2208 module:

### Core Notes
- **Main Study Notes** - Extensive 15 MB PDF covering all lecture material, combining both power electronics and motor drive systems content with personal annotations and worked examples

### Lecture Content
- **Part 1: Power Electronics** - 11 lecture PDFs covering introduction, diodes, thyristors, transistors, heating/cooling, AC voltage controllers, rectifiers, cycloconverters, inverters, and DC-DC converters
- **Part 2: Drive Systems** - Chapter-based content covering electromagnetic fundamentals, DC motor control, and AC motor control, with detailed derivations and examples

### Assessment Support
- **Past Papers** - 7 years of past examination papers (2013-2019) for revision and exam preparation
- **Tutorial Solutions** - Worked solutions for tutorial problems from Part 1 (Power Electronics)

### Practical Work
- **CAD Design Files** - Complete mechanical design project with all component drawings and assemblies
- **Embedded Firmware** - BLDC motor control code implementing Il Matto programs for lab exercises
- **Lab Documentation** - Lab reports, instruction manual, and experimental observations

## Folder Structure

```
ELEC2208 - Power Devices/
├── README.md                                    # This file - module overview and documentation
├── afiah Notes electronic n drives_230529_202223.pdf    # Comprehensive notes covering entire module
│
├── Coursework/                                  # Mechanical design coursework (CAD-based)
│   ├── Full.dwg                                 # Complete assembly drawing
│   ├── Carriage.dwg                             # Carriage component design
│   ├── Load.dwg                                 # Load interface component
│   ├── Slideway.dwg                             # Linear slideway design
│   ├── Drawing1.dwg                             # Additional design views
│   ├── *.bak, *.dwl, *.dwl2                     # AutoCAD backup and lock files
│   ├── downloaded_CAD/                          # Off-the-shelf component CAD models
│   │   ├── AKM11X-AKCN1-00.dwg                  # Kollmorgen BLDC motor
│   │   ├── E6B2-CWZ6C 2000P_R 2M.dwg            # Omron rotary encoder
│   │   ├── 2R32-32A1-FSKC-*.dwg                 # Linear actuator components
│   │   ├── [Various sensors, couplings, and mounting hardware]
│   │   ├── Full.pdf, test.pdf, print*.pdf      # Generated drawings and prints
│   │   └── readme-and-terms-of-use-3d-cad-models.txt
│   ├── soton elec 2208 coursework 2023 -Soton.pdf   # Coursework specification
│   ├── elec 2208 coursework 2020 drawing(1).pdf    # Reference drawing
│   ├── chapter 1 sumary.pdf                     # Chapter 1 summary notes
│   ├── diagram final.pdf                        # Final system diagram
│   └── mhby1g21.pdf                             # Additional coursework documentation
│
├── EE75/                                        # Laboratory work: BLDC motor control
│   ├── bldc.c                                   # BLDC motor control implementation
│   ├── pwm.c                                    # PWM generation module
│   ├── debug.h                                  # Debug and utility functions header
│   ├── original codes/                          # Original/reference code versions
│   │   ├── bldc.c
│   │   ├── debug.h
│   │   └── pwm.c
│   ├── Lab Prints.docx                          # Laboratory report and documentation
│   └── notes.pdf                                # Laboratory instruction manual
│
├── Past Papers/                                 # Examination papers for revision
│   ├── 201314/02/ELEC2208-201314-02-ELEC2208W1.pdf
│   ├── 201415/02/ELEC2208-201415-02-ELEC2208W1.pdf
│   ├── 201516/02/ELEC2208-201516-02-ELEC2208W1.pdf
│   ├── 201617/02/ELEC2208-201617-02-ELEC2208W1.pdf
│   ├── 201718/02/ELEC2208-201718-02-ELEC2208W1.pdf
│   ├── 201819/02/ELEC2208-201819-02-ELEC2208W1.pdf
│   └── 201920/02/ELEC2208-201920-02-ELEC2208W1.pdf
│
├── Slides/                                      # Lecture slides and materials
│   ├── ELEC2208_ModuleOverview.pdf              # Module introduction and structure
│   ├── Part 1 - Power Electronics by Yoshi/
│   │   └── Lectures/
│   │       ├── ELEC2208YTLecture01_Introduction.pdf
│   │       ├── ELEC2208YTLecture02_Diode.pdf
│   │       ├── ELEC2208YTLecture03_Thyristor.pdf
│   │       ├── ELEC2208YTLecture04_Transistor.pdf
│   │       ├── ELEC2208YTLecture05_HeatingCooling.pdf
│   │       ├── ELEC2208YTLecture06_ACVoltageController.pdf
│   │       ├── ELEC2208YTLecture07_Rectifier1.pdf
│   │       ├── ELEC2208YTLecture08_Rectifier2.pdf
│   │       ├── ELEC2208YTLecture09_Cycloconverter.pdf
│   │       ├── ELEC2208YTLecture10_Inverter.pdf
│   │       ├── ELEC2208YTLecture11_DCDCConverter.pdf
│   │       └── ELEC2208YTLecture_Topics.pdf
│   └── Part 2 - Drive Systems/
│       ├── Chapter 1 - Electromagnetic and Mechanical Fundamentals/
│       │   ├── slides ELEC 2208 chapter 1_lecture 1.pptx
│       │   ├── slides ELEC 2208 chapter 1-lecture 2.pptx
│       │   ├── slides ELEC 2208 chapter 1-lecture 3.pptx
│       │   ├── slides ELEC 2208 chapter 1-lecture 4.pptx
│       │   ├── Derivation of polynominal lecture 2.pdf
│       │   ├── transducer chapter.pdf
│       │   ├── intro coursework and lab.pptx
│       │   ├── ELEC2208_Motor_drives_vMar18-chapter 1.pdf
│       │   └── Revision lecture.pptx
│       ├── ELEC2208_Motor_drives_vMar18-chapter 2.pdf
│       ├── Chapter 2_Control of DC motor.pdf
│       ├── ELEC2208_Motor_drives_vMar18-chapter 3.pdf
│       └── Chapter 3_Control of AC motor.pdf
│
├── Tutorials/                                   # Tutorial problems and solutions
│   └── Part 1 - Yoshi/
│       ├── ELEC2208YT_TutorialSolution1.pdf
│       └── ELEC2208YT_TutorialSolution2.pdf
│
└── ef.txt, hf.txt, lf.txt                       # Reference markers

```

## CV Highlights

This module demonstrates proficiency in:
- **Multidisciplinary Engineering** - Integration of electrical, mechanical, and software engineering
- **Power Electronics Design** - Understanding of high-power circuits, converters, and control
- **Embedded Systems Development** - Real-time firmware for motor control applications
- **CAD/CAM Skills** - Professional mechanical design and documentation
- **Motor Drive Systems** - Practical experience with BLDC motor control implementation
- **Project Management** - Self-directed coursework and laboratory project completion
- **Technical Documentation** - Clear, professional engineering documentation and reporting

---

*This module provided comprehensive coverage of power electronics and motor drive systems, combining theoretical understanding with practical skills in CAD design and embedded firmware development. The hands-on experience with BLDC motor control and mechanical system design has directly prepared me for roles in power electronics, motor drives, embedded systems, and mechatronic system engineering.*
