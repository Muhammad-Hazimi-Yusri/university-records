# ELEC3224 -- Guidance, Navigation and Control

| | |
|---|---|
| **Module:** | ELEC3224 - University of Southampton |
| **Year:** | Year 3, Semester 1 |
| **Credits:** | 15 CATS |
| **Assessment:** | Exam-based |
| **Status:** | Completed 2019/2020 |

## Module Overview

This module provides a comprehensive introduction to **Guidance, Navigation, and Control (GNC)** systems, which form the foundation of autonomous vehicles, spacecraft, missiles, and UAVs. GNC integrates three critical functions: navigation (determining position and velocity), guidance (computing desired trajectories), and control (actuating systems to follow commands).

The module covers advanced control theory, optimal estimation techniques, and guidance strategies for autonomous systems. Starting from classical frequency-domain control design, it progresses through state-space methods, Kalman filtering, and specialized guidance laws for aerospace applications. Real-world examples include space systems, UAV navigation, ballistic missile trajectories, and homing guidance strategies.

This module is essential for careers in aerospace engineering, robotics, autonomous vehicles, and defense systems, providing both theoretical foundations and practical implementation skills for safety-critical autonomous systems.

## Key Topics Covered

### Control System Design
- **Frequency Domain Control Design**
  - Classical control techniques (root locus, Bode plots, Nyquist criteria)
  - Compensator design for stability and performance
  - Part 1: Single-loop feedback systems
  - Part 2: Advanced compensation techniques
- **Robust Control**
  - Uncertainty modeling and disturbance rejection
  - H-infinity control concepts
  - Gain and phase margins
- **State-Space Based Control**
  - State-space modeling of dynamic systems
  - Pole placement and observer design
  - Linear Quadratic Regulator (LQR)
  - Full-state feedback and output feedback

### Estimation & Filtering
- **Random Processes**
  - Stochastic signals and noise characterization
  - Autocorrelation and power spectral density
  - White noise and colored noise models
- **Kalman Filtering**
  - Optimal recursive estimation for linear systems
  - Prediction and update equations
  - Sensor fusion applications
  - Extended Kalman Filter (EKF) for nonlinear systems
- **Complementary Filters**
  - Sensor fusion for attitude estimation
  - Low-pass/high-pass filter combinations
  - Applications in IMU integration

### Guidance & Navigation Systems
- **Introduction to GNC Systems**
  - GNC architecture and subsystem integration
  - Requirements for autonomous vehicles
  - Performance metrics and trade-offs
- **Guidance Systems**
  - Guidance law fundamentals
  - Trajectory generation and optimization
  - Waypoint navigation vs. continuous guidance
- **UAV Guidance**
  - Path planning for unmanned aerial vehicles
  - Obstacle avoidance strategies
  - Loitering and formation flight
- **Navigation Systems**
  - Inertial navigation systems (INS)
  - GPS integration and sensor fusion
  - Position and velocity estimation
- **Homing Guidance**
  - Pursuit guidance laws
  - Line-of-sight guidance
  - Command-to-line-of-sight (CLOS)
  - Beam rider guidance
- **Proportional Navigation**
  - PN guidance law derivation
  - Miss distance analysis
  - Optimal evasion strategies
  - Applications in missile guidance

### Application Domains
- **Space Systems**
  - Spacecraft attitude control
  - Orbital mechanics integration
  - Thruster control systems
- **Ballistic Dynamics**
  - Projectile motion and trajectory prediction
  - Atmospheric effects and drag modeling
  - Terminal guidance phase
- **Autonomous Vehicle Systems**
  - Long-range autonomy challenges
  - Multi-sensor integration
  - Real-time decision making

## Technical Skills Demonstrated

- **Advanced Control System Analysis & Design**
  - Frequency-domain analysis (Bode, Nyquist, root locus)
  - Time-domain state-space methods
  - Multi-input multi-output (MIMO) control
  - Stability analysis and robustness assessment

- **Optimal Estimation & Sensor Fusion**
  - Kalman filter design and implementation
  - Complementary filter development
  - Noise modeling and covariance analysis
  - Real-time estimation algorithms

- **Guidance Law Development**
  - Trajectory optimization techniques
  - Pursuit and evasion strategies
  - Proportional navigation implementation
  - Line-of-sight guidance

- **System Integration**
  - GNC subsystem architecture design
  - Navigation/guidance/control loop closure
  - Performance specification and verification

- **MATLAB/Simulink Simulation**
  - Dynamic system modeling
  - Control system design and tuning
  - Monte Carlo analysis for robustness
  - Hardware-in-the-loop (HIL) concepts

- **Mathematical Foundations**
  - Linear algebra and matrix theory
  - Differential equations for dynamic systems
  - Stochastic processes and probability
  - Optimization theory

## Assessment Structure

The module was assessed through a comprehensive **written examination** covering all lecture topics. Assessment included:

- **Theoretical Understanding**: Control theory, estimation, and guidance principles
- **Mathematical Derivations**: Kalman filter equations, guidance laws, stability analysis
- **Problem Solving**: Design of controllers and estimators for given specifications
- **Application**: Analysis of GNC systems for aerospace scenarios

**Supporting Materials:**
- **3 Tutorial Sheets** with worked solutions covering key concepts
- **Past Exam Papers** (2020, 2021, 2022, 2023) with full solutions
- **Practice Questions** compiled by module lecturer Daniel Clark
- **Reference Slides** providing comprehensive lecture coverage

## Practical Applications & CV Highlights

This module provides **industry-critical skills** for careers in:

### Aerospace & Defense
- **Spacecraft GNC Engineers**: Satellite attitude control, orbital maneuvering
- **Missile Guidance Systems**: Proportional navigation, homing seekers, terminal guidance
- **Flight Control Systems**: Aircraft autopilot design, flight management systems

### Autonomous Systems
- **UAV/Drone Control**: Autonomous navigation, waypoint following, obstacle avoidance
- **Autonomous Vehicles**: Sensor fusion, path planning, trajectory tracking
- **Robotics**: Mobile robot navigation, manipulator control, SLAM integration

### Advanced Research & Development
- **Control System Design**: Model-based control for complex dynamic systems
- **Estimation Theory**: Kalman filtering for multi-sensor fusion
- **Optimal Control**: LQR/LQG design for performance optimization

**Key Transferable Skills:**
- Safety-critical system design and verification
- Real-time algorithm implementation
- System-level architecture and requirements analysis
- MATLAB/Simulink modeling for aerospace applications
- Understanding of industry standards (DO-178C for airborne software, MIL-STD for defense systems)

**Relevant to Industries:**
- Aerospace (Boeing, Airbus, Lockheed Martin, BAE Systems)
- Autonomous Vehicles (Tesla, Waymo, Cruise, Aurora)
- Robotics (Boston Dynamics, ABB, KUKA)
- Defense (Raytheon, Northrop Grumman, MBDA)
- Space (SpaceX, Blue Origin, NASA, ESA)

## Folder Structure

```
ELEC3224 Guidance, Navigation and Control/
│
├── Lecture Materials/
│   ├── 1 - Introduction.pdf                                          # Course overview, GNC fundamentals
│   ├── 2 -  Space Systems Example.pdf                                # Spacecraft control case study
│   ├── 3 - Frequency Domain Control Design Part 1.pdf                # Classical control theory
│   ├── 4 - Frequency Domain Control Design.pdf                       # Advanced compensation techniques
│   ├── 5 - Robust Control.pdf                                        # Uncertainty and disturbance handling
│   ├── 6 - State-Space based Control.pdf                             # Modern control methods, LQR
│   ├── 7 - Random Processes.pdf                                      # Stochastic signals, noise modeling
│   ├── 8 - Kalman Filtering.pdf                                      # Optimal estimation theory
│   ├── 9 - Introduction to GNC Systems.pdf                           # Integrated GNC architecture
│   ├── 10 - Guidance Systems.pdf                                     # Guidance law fundamentals
│   ├── 11 - UAV Guidance.pdf                                         # UAV path planning and navigation
│   ├── 12 - Ballistic Dynamics.pdf                                   # Projectile motion, trajectory control
│   ├── 13 - Complementary Filters.pdf                                # Sensor fusion for attitude estimation
│   ├── 14 - Proportional Navigation.pdf                              # PN guidance law derivation
│   ├── 15 - Beam Rider and CLOS.pdf                                  # Command-to-line-of-sight guidance
│   ├── 16 - Homing Guidance.pdf                                      # Terminal homing strategies
│   └── 17 - Proportional Navigation and Optimal Evasion.pdf          # PN miss distance, evasion tactics
│
├── Examinations/
│   ├── exam22.pdf                                                    # 2022 examination paper
│   ├── exam23.pdf                                                    # 2023 examination paper
│   ├── exam23q2fig.jpg                                               # Supporting figure for 2023 Q2
│   ├── sols20.pdf                                                    # 2020 solutions
│   ├── sols21.pdf                                                    # 2021 solutions
│   └── sols22.pdf                                                    # 2022 solutions
│
├── Tutorials/
│   ├── tut1.pdf                                                      # Tutorial sheet 1
│   ├── tut2.pdf                                                      # Tutorial sheet 2
│   └── tut3.pdf                                                      # Tutorial sheet 3
│
├── Reference Materials/
│   ├── elec3224_slides - Daniel Clark.pdf                            # Complete slide deck
│   ├── questions3224 - Daniel Clark.pdf                              # Practice questions compilation
│   ├── readmefirst.pdf                                               # Module introduction guide
│   ├── ELEC3224-201920-01-ELEC3224W1.pdf                            # Module handbook 2019/20
│   ├── trigo.jpg                                                     # Trigonometry reference sheet
│   └── longrange auto (1).pptx                                       # Long-range autonomy presentation (87 MB)
│
└── README.md                                                          # This file
```

## Key Learning Outcomes

Upon completion of this module, I achieved the following learning outcomes:

1. **Design and Analyze Control Systems**
   - Apply frequency-domain and state-space methods to design controllers for dynamic systems
   - Evaluate stability, performance, and robustness of closed-loop control systems
   - Implement pole placement, LQR, and robust control techniques

2. **Implement Optimal Estimation Algorithms**
   - Derive and implement Kalman filters for linear and nonlinear systems
   - Design complementary filters for sensor fusion applications
   - Characterize and model stochastic processes and measurement noise

3. **Understand Guidance Strategies for Autonomous Systems**
   - Develop and analyze guidance laws (pursuit, PN, CLOS, beam rider)
   - Optimize trajectories for performance criteria (time, fuel, miss distance)
   - Evaluate guidance system performance through simulation

4. **Apply GNC Principles to Real-World Applications**
   - Integrate navigation, guidance, and control subsystems
   - Design GNC systems for spacecraft, UAVs, missiles, and autonomous vehicles
   - Analyze performance trade-offs and system requirements

5. **Mathematical and Computational Proficiency**
   - Solve differential equations governing dynamic systems
   - Apply linear algebra and matrix theory to control and estimation
   - Implement algorithms in MATLAB/Simulink for simulation and analysis

---

**Note:** This module provides foundational knowledge for advanced topics in autonomous systems, and is particularly valuable for roles requiring expertise in control theory, estimation, and guidance system design for safety-critical aerospace applications.
