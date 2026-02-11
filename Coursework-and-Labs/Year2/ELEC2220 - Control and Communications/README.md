# ELEC2220 -- Control and Communications

**Module:** ELEC2220 -- Control Systems and Communications Theory
**Type:** Individual Coursework
**Academic Year:** 2021/2023, Year 2, University of Southampton
**Assessment:** Two coursework assignments (Control Systems and Communications Theory)
.
## Module Overview

This second-year module provided comprehensive coverage of control systems engineering and communications theory. The module combined mathematical analysis with practical problem-solving, covering classical control techniques (root locus, Nyquist stability) and modern digital communications (QAM, QPSK, BPSK modulation schemes). The coursework emphasized analytical skills, system stability analysis, and signal processing fundamentals essential for electrical and electronic engineering.

## Key Topics Covered

### Control Systems
- **Root locus analysis and design** -- Sketching root locus plots from open-loop transfer functions, determining break-in/break-away points, centroid calculations, and angles of asymptotes
- **Forward path controller design** -- PD (Proportional-Derivative) controller implementation for non-oscillatory closed-loop response
- **System stability analysis** -- Analyzing stability using pole locations, determining minimum gain values for desired response characteristics
- **Nyquist stability criterion** -- Plotting Nyquist diagrams, determining gain and phase margins for industrial process control systems
- **Time delay effects** -- Analyzing the impact of pure time delays on closed-loop system stability
- **Transfer function manipulation** -- Working with s-domain representations, pole-zero analysis, and frequency response

### Communications Theory
- **Frequency Modulation (FM)** -- Bandwidth calculations, normalized power analysis, frequency sensitivity factors
- **Quadrature Amplitude Modulation (QAM)** -- Block diagram design, modulation/demodulation processes
- **Quadrature Phase Shift Keying (QPSK)** -- Digital modulation technique analysis, constellation diagrams
- **Binary Phase Shift Keying (BPSK)** -- Transmission analysis, error probability calculations
- **Channel impulse response modeling** -- Analyzing communication channels with noise and interference
- **Signal-to-Noise Ratio (SNR) analysis** -- 3dB calculations, performance degradation assessment
- **Probability and error analysis** -- Conditional probability density functions, error rate calculations

## Coursework Assignments

### Assignment 1: Control Systems (2nd Coursework)
**Total Marks:** 50 marks (25 marks per question)

#### Question 1: Root Locus Plots and Forward Path Controllers (25 Marks)
A highly oscillatory plant with transfer function P(s) = 1/(s²+4) was to be controlled using a forward path controller K(s) with unity feedback.

**Part (a) -- Root Locus Sketching and Minimum Gain (12 Marks):**
- Task: Sketch the root locus for an ideal PD controller K(s) = 4k + ks
- Determine the minimum allowable value of k to ensure non-oscillatory closed-loop impulse response
- **Key Analysis:**
  - Open-loop transfer function: K(s)P(s) = k(4+s)/(s²+4)
  - Open-loop zeros: s = -4
  - Open-loop poles: s = 2j, -2j (imaginary axis)
  - Number of poles/zeros: n=2 (poles), m=1 (zero) → 2-1=1 asymptote
  - Centroid: σ = (Σ real parts of OL poles - Σ real parts of OL zeros)/(n-m) = (0-(-4))/1 = 4
  - Angle of asymptote: φₐ = (2q+1)·180°/(n-m) = 180°, where q=0,1,...,(n-m-1)
  - Break-in point: s = -8.4721 (calculated from dk/ds = 0)
  - **Minimum gain: k > 16.944** for non-oscillatory response

**Part (b) -- Implemented Controller Analysis (8 Marks):**
- Implemented controller: K(s) = (120k+30ks)/(50+s)
- Task: Sketch new root locus as k increases from zero to infinity, comment on system response
- **Key Analysis:**
  - Open-loop transfer function: K(s)P(s) = k(30s+120)/((s²+4)(s+50))
  - Open-loop zeros: s = -4 (30s=-120)
  - Open-loop poles: s = -50, 2j, -2j
  - Rank: n-m = 3-1 = 2
  - Centroid: σ = ((-50+0) - (-4))/2 = -23
  - Number of asymptotes: 3 (at angles related to pole excess)
  - Break-in points: s ≈ -21.50 and s ≈ -9.93, 0.43
  - **Conclusion:** System is stable for all positive k values, as all poles remain in the left-hand plane

**Part (c) -- Stability with Additional Open Loop Pole (5 Marks):**
- Scenario: Maximum value of k exists for system stability when an additional open loop pole exists at s = -100
- Task: Sketch root locus diagram and explain the finite maximum k
- **Key Finding:** The additional pole modifies the root locus such that branches can cross into the right-half plane at high k values, creating instability

#### Question 2: Nyquist Stability Criterion and Time Delays (25 Marks)
An industrial process with open-loop transfer function GH(s) = k/(s(s+2)(s+8))

**Part (a) -- Nyquist Diagram and Margins (8 Marks):**
- Task: Plot the Nyquist diagram and clearly indicate gain and phase margins
- **Analysis:** Standard Nyquist plot for type-1 system with three poles

**Part (b) -- Maximum Allowable Gain and Frequency (7 Marks):**
- Task: Determine maximum gain k and frequency ω (rad s⁻¹) for system stability
- **Calculation approach:** Find the frequency where phase angle = -180° and corresponding gain

**Part (c) -- Time Delay Effect on Stability (5 Marks):**
- Scenario: Open-loop transfer function includes pure time delay of 10 ms
- Task: Sketch locus of closed-loop system
- **Analysis:** Time delay adds phase lag: e^(-sT_d) where T_d = 10ms = 0.01s

**Part (d) -- Phase Angle Calculation (5 Marks):**
- Task: Show that phase of time-delayed closed loop system is 180° when π/2 - 0.01ω = tan⁻¹(10ω/(16-ω²))
- Given identity: tan⁻¹x ± tan⁻¹y = tan⁻¹((x±y)/(1∓xy))
- **Mathematical proof using trigonometric identities**

### Assignment 2: Communications Theory
**Submission:** mhby1g21 coursework_comms_221216_151346.pdf (16 December 2022)

**Topics Covered:**
- **FM Signal Analysis:**
  - Bandwidth calculations using Carson's rule
  - Normalized power in modulated signals
  - Frequency sensitivity factor (k_f) applications

- **Digital Modulation Block Diagrams:**
  - QAM modulator/demodulator block diagrams
  - QPSK transmitter and receiver architecture
  - Baseband representation and carrier recovery

- **Channel Modeling:**
  - Channel impulse response h(t) characterization
  - Additive White Gaussian Noise (AWGN) modeling
  - Received signal representation

- **BPSK Transmission Analysis:**
  - Binary phase shift keying signal generation
  - SNR calculations (3dB degradation scenarios)
  - Conditional probability density functions
  - Error probability (bit error rate) calculations

## Technical Skills Demonstrated

### Mathematical & Analytical
- **Complex variable analysis** -- Working with s-domain transfer functions, pole-zero manipulations, complex conjugate poles
- **Root locus techniques** -- Applying root locus rules (break-in/break-away points, asymptote angles, centroid calculations)
- **Nyquist stability criterion** -- Constructing Nyquist diagrams, determining gain/phase margins
- **Trigonometric identities** -- Phase angle calculations using inverse tangent identities
- **Statistical signal analysis** -- Probability density functions, conditional probabilities, error rate calculations
- **Differential equations** -- Solving control system differential equations, impulse response characterization

### Control Theory
- **PD controller design** -- Proportional-Derivative controller synthesis for oscillatory plant stabilization
- **System stability assessment** -- Analyzing closed-loop stability using Routh-Hurwitz criterion and root locus
- **Time domain vs frequency domain analysis** -- Relating pole locations to transient response characteristics
- **Feedback loop analysis** -- Unity feedback systems, forward path design
- **Time delay compensation** -- Understanding pure time delay effects (e^(-sT)) on system stability

### Communications
- **Digital modulation schemes** -- QAM, QPSK, BPSK modulation/demodulation principles
- **Analog modulation** -- Frequency modulation (FM) analysis and bandwidth estimation
- **Signal-to-Noise analysis** -- SNR degradation impact on communication system performance
- **Baseband representation** -- In-phase and quadrature components of modulated signals
- **Error probability calculations** -- BER (Bit Error Rate) analysis for binary communication systems

## Assessment Results

**Control Systems Coursework (2nd Coursework):**
- Question 1 Total: 25 marks
  - Part (a): 12 marks (Root locus sketching and minimum k calculation)
  - Part (b): 8 marks (Implemented controller analysis)
  - Part (c): 5 marks (Stability with additional pole)

- Question 2 Total: 25 marks
  - Part (a): 8 marks (Nyquist diagram and margins)
  - Part (b): 7 marks (Maximum allowable gain and frequency)
  - Part (c): 5 marks (Time delay locus)
  - Part (d): 5 marks (Phase angle proof)

**Communications Coursework:**
- Submitted: 16 December 2022 (15:13:46)
- Covered FM, QAM, QPSK, BPSK analysis with comprehensive calculations

## CV Highlights

- **Classical Control Systems Expertise** -- Applied root locus and Nyquist techniques to industrial process control problems, demonstrating strong understanding of feedback system stability
- **Analytical Problem-Solving** -- Solved complex control and communications problems using mathematical analysis (complex variables, differential equations, probability theory)
- **Digital Communications Knowledge** -- Analyzed modern digital modulation schemes (QAM, QPSK, BPSK) essential for wireless communications and signal processing roles
- **System Stability Analysis** -- Determined stability criteria, gain/phase margins, and controller parameters for closed-loop systems
- **Signal Processing Fundamentals** -- Applied SNR analysis, error probability calculations, and frequency-domain techniques to communication system design

## Folder Structure

```
ELEC2220 - Control and Communications/
├── README.md                                           # This file
├── control2.pdf                                        # Assignment questions and specifications (13 MB)
├── mhby1g21 2ndCourseworkELEC2220.pdf                 # Control systems coursework submission (13 MB)
└── mhby1g21 coursework_comms_221216_151346.pdf        # Communications coursework submission (7.3 MB)
```
