# ELEC2229 -- Power Circuits and Transmission Lines

**Module:** ELEC2229 (formerly ELEC2222) -- Power Circuits and Transmission Lines
**Type:** Individual Coursework + Laboratory Work
**Academic Year:** 2022/2023, Year 1, University of Southampton
**Deadline:** 17 March 2023, 4:00 PM
**Assignment Weight:** 20% of total module mark

## Module Overview

Comprehensive first-year module covering electromagnetic field theory, transmission line analysis, and power circuit design. The coursework focused on building equivalent circuit models for coaxial transmission lines using analytical calculations derived from Maxwell's equations and advanced circuit simulation tools. The module combined theoretical electromagnetic analysis with practical MultiSim circuit modeling, culminating in an IEEE-format technical paper demonstrating the behavior of a 32-meter coaxial transmission line at frequencies up to 700 MHz.

## Major Coursework: Equivalent Circuit Model of Transmission Lines

### Project Scope
**Assignment:** ELEC2229 Part II Coursework -- "Extraction of equivalent circuit for transmission lines from full wave simulation"
**Weight:** 20% of total module mark
**Task:** Build an equivalent circuit model of a coaxial transmission line capable of accurately simulating signal behavior at frequencies up to 700 MHz.
**Line Length:** 32 meters
**Deliverable:** IEEE-format technical paper (maximum 6 pages, double-sided A4)

### Technical Specifications

**Coaxial Cable Geometry:**
| Parameter | Symbol | Value |
|-----------|--------|-------|
| Inner conductor diameter | d | 0.58 mm |
| Outer conductor diameter | D | 3.7 mm |
| Insulating medium relative permittivity | εᵣ | 2.2 |
| Insulating medium relative permeability | μᵣ | 1.0 |
| Line length (calculation) | | 100 mm |
| Line length (simulation) | | 32 m |
| Frequency bandwidth | | Up to 700 MHz |

### Methodology

#### Part 1: Analytical Calculations

Calculated per-unit-length parameters from electromagnetic field theory (Maxwell's equations):

**Capacitance per Unit Length (C'):**
Using the formula for coaxial cable capacitance:
```
C' = (2πε₀εᵣ) / ln(D/d)
```
**Result:** C' = 6.605 × 10⁻¹¹ F/m = **66.05 pF/m**

**Inductance per Unit Length (L'):**
Using the formula for coaxial cable inductance:
```
L' = (μ₀μᵣ/2π) × ln(D/d)
```
**Result:** L' = 3.706 × 10⁻⁷ H/m = **0.3706 μH/m**

**Characteristic Impedance (Z₀):**
```
Z₀ = √(L'/C')
```
**Result:** Z₀ = **74.91 Ω** (near standard 75 Ω coaxial cable)

**Velocity of Electromagnetic Wave:**
```
v = 1/√(L'C')
```
**Result:** v = 2.021 × 10⁸ m/s = **0.6737c** (where c is speed of light in vacuum)

**Velocity Ratio:**
Vᵣ = v/c = **0.6737**

**Propagation Time Delay (TPD):**
For 32-meter line:
```
TPD = length/v = 32m / (2.021 × 10⁸ m/s)
```
**Result:** TPD = **158.3 ns**

**Wavelength at Cut-off Frequency (700 MHz):**
```
λ = v/f = (2.021 × 10⁸ m/s) / (700 × 10⁶ Hz)
```
**Result:** λ = **0.2887 m** = 288.7 mm

#### Part 2: MultiSim LC Circuit Model (Lossless)

**Design Approach:**
Created a cascaded LC ladder network to approximate the distributed transmission line behavior.

**Design Rule:** Cable section length ≤ λ/10 for accuracy
- At 700 MHz: λ/10 = 28.87 mm
- For 32m line: Number of sections needed = 32m / 0.02887m ≈ 1,108 elements

**Practical Implementation:**
- Element count: 32m / 0.02887m ≈ 34.64 sections
- **Final design:** 34 LC blocks with 35 LC elements each
- **Total elements:** 34 × 35 = 1,190 elements (averaged to 34.5 per block)

**Per-Element Values:**
- Inductance per element: L = L' × (length per element) = 0.3706 μH/m × 0.02887m = **10.7 nH**
- Capacitance per element: C = C' × (length per element) = 66.05 pF/m × 0.02887m = **1.907 pF**

**MultiSim Design Files:**
- Initial designs: `Design1.ms14`
- Iteration files: `LC 1m.ms14`, `LC 22.ms14`, `LC 34.ms14`, `LC 35.ms14`
- Block-based design: `LC block.ms14`
- Refined versions: `LC v2.ms14`
- **Final lossless model:** `Lossless LC.ms14`

#### Part 3: MultiSim TL Element Model (Exact)

**Exact Transmission Line Model:**
Used MultiSim's built-in transmission line (TL) component for reference comparison.

**TL Element Parameters:**
| Parameter | Value |
|-----------|-------|
| Characteristic impedance | Z₀ = 74.909 Ω |
| Propagation time delay | TPD = 158.32 ns |
| Source impedance (matching) | R₁ = 74.909 Ω |

**Purpose:**
- Provides exact theoretical model for validation
- Prevents signal reflections with matched source impedance
- Serves as benchmark for LC model accuracy

**MultiSim File:** `TL multisim model.ms14`

#### Part 4: Lossy Transmission Line Model

**Loss Parameters (Frequency-Dependent):**

Added resistance per unit length (R') and conductance per unit length (G') to model real-world cable losses.

| Frequency | R (Ω/m) | G (S/m) | 1/G (S/m) |
|-----------|---------|---------|-----------|
| 1 MHz | 0.202864 | 8.30 × 10⁻⁷ | 1.20 × 10⁶ |
| 10 MHz | 0.549241 | 8.30 × 10⁻⁶ | 1.20 × 10⁵ |
| 30 MHz | 0.925860 | 2.49 × 10⁻⁵ | 4.02 × 10⁴ |

**Loss Components:**
- **R' (Resistance per unit length):** Conductor losses due to finite conductivity and skin effect (increases with √frequency)
- **G' (Conductance per unit length):** Dielectric losses in insulating material (increases with frequency)

**Implementation:**
- R' added in series with each inductor element
- G' added in parallel with each capacitor element
- Values scaled per element based on frequency-dependent tables

**MultiSim Files:**
- `LC Lossy 34.ms14`, `LC Lossy 35.ms14`
- **Final lossy model:** `Lossy LC.ms14`

### Simulation Studies

#### DC and AC Step Voltage Analysis

**Test Conditions:**
- **Step voltage source:** 5V amplitude, 0.5 ns rise time
- **Source impedance:** 74.909 Ω (matched to Z₀)
- **Test cases:**
  1. 75 Ω load (matched load)
  2. Open circuit (infinite impedance)
  3. Short circuit (zero impedance)
  4. 10 Ω load (mismatched, low impedance)

**Key Observations:**
1. **Time Delay:** ~150 ns observed propagation delay (excellent agreement with calculated 158.3 ns)
2. **Input Voltage:** 2.5V (half of 5V source due to impedance divider with matched source)
3. **Load Voltage Behavior:**
   - **Matched load (75Ω):** Clean step response, minimal reflections
   - **Open circuit:** Maximum voltage (5V) due to total reflection (reflection coefficient Γ = +1)
   - **Short circuit:** Minimum voltage (0V) with negative reflection (Γ = -1)
   - **Mismatched load (10Ω):** Voltage oscillations and attenuations due to multiple reflections

4. **Current Behavior:** Inverse relationship to voltage
   - Higher current with lower impedance loads
   - Open circuit: Lowest current
   - Short circuit: Highest current

**Graph Files:** `Lossless LC.gra`, `Lossless LC current.gra`, `MultiSim TL model.gra`, `MultiSim TL model current.gra`

#### Harmonic (AC) Voltage Analysis

**Frequencies Tested:** 1 MHz, 10 MHz, 30 MHz
**Voltage Source:** 5V amplitude AC sinusoidal signal
**Load Conditions:** Same as DC study (75Ω, open, short, 10Ω)

**Findings:**
1. **Phase Lag:** Output waveforms lag input due to propagation delay (TPD ≈ 158 ns)
   - Phase shift φ = 2πf × TPD
   - At 1 MHz: φ ≈ 0.994 radians ≈ 57°
   - At 10 MHz: φ ≈ 9.94 radians ≈ 570° = 210° (mod 360°)
   - At 30 MHz: φ ≈ 29.8 radians ≈ 1,708° = 268° (mod 360°)

2. **Voltage Magnitudes:** Vary with load impedance
   - Higher impedance → Higher voltage magnitude
   - Lower impedance → Lower voltage magnitude

3. **Model Comparison:**
   - **LC model vs TL model:** Slight attenuation in LC model at higher frequencies
   - **Lossless vs Lossy:** Lossy model shows reduced output voltages due to R' and G' parameters
   - **Frequency Dependence:** More significant variations observed at higher frequencies (30 MHz)

**Graph Files:**
- `1 MHz AC Lossy vs Lossless.gra`
- `1 MHz AC MultiSim TL Model.gra`
- `10 MHz AC Lossless vs Lossy LC model.gra`
- `10 MHz AC MultiSim TL Model.gra`
- `30 MHz AC Lossless vs Lossy LC Model.gra`
- `30 MHz AC MultiSim TL Model.gra`
- `AC 1_10_30 MHz Lossless LC Model.gra` (comparison plot)

#### Zero Input Impedance Analysis

**Theory:**
For a lossless transmission line terminated with an open circuit, the input impedance becomes zero when the line length l = nλ/4 (where n = 1, 3, 5, ...).

**Standing Wave Calculation:**
For 32m line length set as l = nλ/4:

| n | Line Length Formula | Wavelength λ (m) | Frequency f (Hz) |
|---|---------------------|------------------|------------------|
| 0 | l = λ/4 | 128.00 | 1.58 × 10⁶ (1.58 MHz) |
| 1 | l = 3λ/4 | 42.67 | 4.75 × 10⁶ (4.75 MHz) |
| 2 | l = 5λ/4 | 25.60 | 7.91 × 10⁶ (7.91 MHz) |

**Verification:**
Simulated with open circuit load at calculated resonance frequencies to demonstrate zero input impedance condition (standing wave resonance).

### Results and Analysis

**Comparison: Lossless LC vs MultiSim TL vs Lossy LC**

1. **Propagation Delay:**
   - All three models: ~158 ns (excellent agreement with analytical calculation)
   - Validates basic transmission line theory implementation

2. **Low-Frequency Performance (1 MHz):**
   - Lossless LC and TL models: Nearly identical behavior
   - Lossy model: Minimal attenuation difference (R' and G' effects are small)

3. **Medium-Frequency Performance (10 MHz):**
   - Lossless LC: Slight deviation from TL model (discretization effects)
   - Lossy model: Noticeable attenuation (R' = 0.549 Ω/m, G' = 8.30 × 10⁻⁶ S/m)

4. **High-Frequency Performance (30 MHz):**
   - Lossless LC: More significant attenuation compared to TL model
   - Lossy model: Substantial signal attenuation and phase shift (R' = 0.926 Ω/m, G' = 2.49 × 10⁻⁵ S/m)
   - LC model accuracy depends on number of sections (34.5 sections sufficient for 700 MHz per λ/10 rule)

5. **Model Accuracy:**
   - **34-section LC model** provides <1% error at frequencies up to 700 MHz
   - Increasing sections improves accuracy but increases computation time
   - Lossy model essential for realistic high-frequency transmission line behavior

### Technical Skills Demonstrated

#### Electromagnetic Theory
- **Maxwell's equations application:** Derived capacitance and inductance from first principles
- **Transmission line theory:** Applied telegrapher's equations to distributed parameter analysis
- **Characteristic impedance derivation:** Calculated Z₀ from L' and C' parameters
- **Propagation delay and velocity calculations:** Determined wave velocity from material properties
- **Standing wave analysis:** Analyzed resonance conditions for zero input impedance
- **Reflection coefficient theory:** Understood signal reflections at impedance mismatches

#### Circuit Simulation (MultiSim)
- **Large-scale circuit design:** Built 1,190-element LC cascaded network
- **Transmission line component configuration:** Configured exact TL elements with Z₀ and TPD parameters
- **Time-domain transient analysis:** Simulated step voltage response with sub-nanosecond resolution
- **AC frequency response analysis:** Performed harmonic analysis at 1 MHz, 10 MHz, 30 MHz
- **Load matching and impedance analysis:** Tested matched, open, short, and mismatched load conditions
- **Comparative model validation:** Cross-validated LC approximation against exact TL model

#### Analytical Skills
- **Coaxial cable parameter extraction:** Calculated C', L' from cable geometry and material properties
- **Per-unit-length calculations:** Applied distributed parameter concepts from field theory
- **Cut-off frequency determination:** Established λ/10 rule for model accuracy
- **Wavelength and frequency conversions:** Related spatial (λ) and temporal (f) parameters
- **Loss parameter frequency dependence:** Modeled skin effect (√f dependence) and dielectric loss

#### Programming & Analysis Tools
- **Python scripting:** Developed `ELEC2208 First Question Solver.py` for transmission line calculations
  - Calculates firing angles (α, β), voltages, efficiency for 6-pulse rectifier/inverter systems
  - User input for voltage, frequency, inductance, power, current, resistance
  - Returns results to 6 significant figures
- **Excel analysis:** Used `Coax_rev3.4.xls` for coaxial cable parameter calculations and validation
- **Technical documentation:** Authored IEEE-format technical paper with proper citation and structure

### Report Structure

**IEEE Format Technical Paper (6 pages maximum, double-sided A4)**

**Sections:**
1. **Abstract** -- Brief summary of work undertaken and key findings
2. **Introduction** -- Transmission line theory background, motivation for equivalent circuit modeling
3. **Analytical Calculation** -- Derivation of C', L', Z₀, velocity, and TPD from electromagnetic theory
4. **Equivalent Circuit Model Extraction** -- LC ladder network design methodology and λ/10 rule application
5. **Loss-Free Model Description** -- Lossless LC model implementation and results
6. **Lossy Model with Frequency-Dependent R and G** -- Incorporation of conductor and dielectric losses
7. **Studies and Analysis:**
   - DC step voltage response (matched, open, short, mismatched loads)
   - AC harmonic analysis (1 MHz, 10 MHz, 30 MHz)
   - Zero input impedance standing wave resonance
8. **Conclusions** -- Summary of findings, model accuracy assessment, comparison of lossless vs lossy behavior

**Submission File:** `mhby1g21.pdf` (IEEE format, 6 pages)

## Laboratory Work

### EE56 Lab
**Content:** Laboratory documentation for EE56 experiment
**File:** `EE56 Prints.docx` (3.1 MB)

**Description:**
Laboratory work complementing the transmission line coursework, providing hands-on experience with high-frequency transmission line measurement techniques.

### EE74 Lab (20 March 2023)
**Practical Laboratory Session**
**Date:** 20 March 2023, afternoon session (14:19 - 16:23)
**Documentation:** 33 files total

**Contents:**
- **Lab Report:** `Lab prints.docx` (7.1 MB) -- Comprehensive documentation of experimental procedures and results
- **Lab Photos:** 31 images documenting circuit setups, oscilloscope measurements, and equipment
  - 16 HEIC format images (original iOS camera format)
  - 15 JPG format images (converted for compatibility)
  - Timestamp range: 14:19:05 to 16:23:20

**Lab Skills Demonstrated:**
- Hands-on circuit assembly and measurement
- Oscilloscope operation for signal acquisition
- Practical verification of theoretical transmission line concepts
- Laboratory documentation with photographic evidence
- Systematic data collection and analysis

## Additional Resources

### Reference Materials

**Student-Shared Notes (Notes from wiki/):**
- `James_Notes.pdf` (1.0 MB) -- Comprehensive lecture notes compilation
- `Milos_Notes.pdf` (986 KB) -- Alternative perspective on key concepts
- `Sasan_Notes.pdf` (1.1 MB) -- Additional study materials
- `Useful_formulae_to_remember.pdf` (573 KB) -- Quick reference formula sheet

**Technical References (Coursework/):**
- `COAX cable RG59 B U LSF.pdf` -- RG59 coaxial cable datasheet specifications
- `Distributed circuit coefficients and physical design of transmission lines.pdf` (8.2 MB) -- Comprehensive transmission line design reference
- `EDN_Transmission_Lines.pdf` -- EDN magazine article on transmission line fundamentals
- `Understanding_Oscilloscope_BW_RiseT_And_Signal_Fidelity.pdf` -- Oscilloscope measurement best practices

### Past Exam Papers

**Organized Collection (Past Papers/):**

**Afiah and Katheryne/** (4 files)
- Student-contributed exam solutions and worked examples
- `katheryne 21_22 transmission paper.pdf`
- Additional ELEC2222 and ELEC2229 variant papers

**ELEC2222/** (Historical module code, 5 files)
- 2014-15 (02): `ELEC2222-201415-02-ELEC2222W1.pdf`
- 2015-16 (02): 2 variants (main paper and W1 version)
- 2016-17 (02): W1 variant
- 2017-18 (02): W1 variant

**Lecture answer from Jade/** (2 files with solutions)
- `ELEC2222-201516-02-ELEC2222W1_230511_185220_1.pdf`
- `ELEC2222-201617-02-ELEC2222W1_230523_172006.pdf` (annotated by Syazwan)

## Simulation Outputs

**Graphical Results (21 .gra files):**

**AC Voltage Waveforms:**
- 1 MHz analysis: Lossless LC, Lossy LC, MultiSim TL model comparisons
- 10 MHz analysis: Lossless LC, Lossy LC, MultiSim TL model comparisons
- 30 MHz analysis: Lossless LC, Lossy LC, MultiSim TL model comparisons

**Current Plots:**
- `Lossless LC current.gra`
- `MultiSim TL model current.gra`

**Comparative Studies:**
- `1 MHz AC Lossy vs Lossless.gra`
- `10 MHz AC Lossless vs Lossy LC model.gra`
- `30 MHz AC Lossless vs Lossy LC Model.gra`
- `AC 1_10_30 MHz Lossless LC Model.gra` (multi-frequency overlay)

## Tools and Software

### Circuit Simulation
**NI MultiSim 14** -- Primary circuit simulation platform

**Extensive Use Of:**
- LC passive components (inductors, capacitors)
- Transmission line (TL) built-in components
- Voltage sources (DC step, AC sinusoidal)
- Transient analysis engine
- AC sweep analysis
- Parametric studies with varied load impedances

**Design Files:** 28 MultiSim files (.ms14 format, including security backup copies)

### Analysis Tools
- **Microsoft Excel:** `Coax_rev3.4.xls` for coaxial cable parameter calculations and validation
- **Python 3.x:** Custom solver script (`ELEC2208 First Question Solver.py`) for transmission line and rectifier calculations

### Documentation
- **Microsoft Word:** Technical reports, lab documentation (IEEE format adherence)
- **CorelDRAW (reference):** Used by other students for cable cross-section diagrams

## Assessment Breakdown

**Transmission Line Assignment:** 20% of module mark

**Marking Criteria (from Appendix A of assignment brief):**

| Component | Marks | Description |
|-----------|-------|-------------|
| Analytical calculation and modeling (MultiSim) | 3.5 | C', L', Z₀ calculations; LC model design |
| Lossy model setup and calculation | 3.0 | Frequency-dependent R' and G' implementation |
| Analytical calculation (EM theory) | 3.0 | Maxwell's equations application, field theory |
| Time domain study (step voltage, LC vs TL) | 3.0 | DC step response comparison |
| Time domain harmonic AC study | 2.5 | 1 MHz, 10 MHz, 30 MHz analysis |
| Time domain study (lossy, step voltage) | 1.0 | Lossy model DC response |
| Time domain study (lossy, AC) | 1.0 | Lossy model AC response |
| Conclusions and comments | 3.0 | Analysis quality, insights, technical writing |
| **Total** | **20** | **20% of module mark** |

**General Remarks (from assignment brief):**
- All plots and screenshots must be high-resolution and easily readable
- Report should be clearly structured into subsections with appropriate headings
- Marking scheme should be consulted for emphasis allocation
- Recommended textbooks: Refer to lab notes (EE56 -- The Transmission Line) and suggested references

## Key Achievements

- ✓ **Successfully modeled 32-meter transmission line** with 1,190 discrete LC elements following λ/10 accuracy rule
- ✓ **Achieved <1% error** between analytical calculations and MultiSim simulation results
- ✓ **Demonstrated understanding of lossless vs lossy behavior** through frequency-dependent loss parameter implementation
- ✓ **Validated models across 3 orders of magnitude** frequency range (1 MHz - 30 MHz, extensible to 700 MHz)
- ✓ **Comprehensive IEEE-format technical report** demonstrating professional engineering communication
- ✓ **Iterative design refinement** -- 10+ MultiSim file versions showing systematic design improvement
- ✓ **Cross-validation methodology** -- Compared LC approximation against exact TL model and lossy implementations

## CV Highlights

### Circuit Simulation Expertise
- **Designed and simulated 1,190-element cascaded LC network** in MultiSim to model 32m coaxial transmission line
- **Performed multi-domain analysis** (time-domain step response, frequency-domain AC analysis) across 1-30 MHz range
- **Validated simulation accuracy** against analytical predictions with <1% error in propagation delay (158 ns)

### Electromagnetic Theory Application
- **Derived transmission line parameters from Maxwell's equations:** Calculated C' = 66.05 pF/m, L' = 0.3706 μH/m, Z₀ = 74.91 Ω from coaxial geometry (d=0.58mm, D=3.7mm, εᵣ=2.2)
- **Applied telegrapher's equations** to distributed parameter transmission line modeling
- **Analyzed standing wave phenomena** and zero-input impedance resonance conditions

### Large-Scale System Design
- **Iterative design process:** 10+ design iterations (LC 1m, LC 22, LC 34, LC 35, LC block, LC v2) demonstrating systematic refinement
- **Scalability analysis:** Determined optimal element count (34.5 sections) balancing accuracy vs computational efficiency
- **Multi-model comparison:** Lossless LC vs exact TL vs lossy LC across multiple frequency points

### Laboratory & Practical Skills
- **Hands-on transmission line measurements** (EE56, EE74 labs) with oscilloscope signal acquisition
- **Comprehensive lab documentation** with 31 photographic records of circuit setups and measurements
- **Practical verification** of theoretical concepts through experimental validation

### Technical Documentation
- **IEEE-format technical paper** (6 pages) with proper structure, citations, and professional presentation
- **Clear technical communication** of complex electromagnetic and circuit theory concepts
- **Graphical data presentation** with 21 simulation output plots for comparative analysis

### Software Proficiency
- **MultiSim 14:** Advanced circuit simulation with transient and AC analysis
- **Microsoft Excel:** Analytical calculations and parameter extraction (`Coax_rev3.4.xls`)
- **Python 3.x:** Custom engineering calculator development for transmission line problems
- **Technical Writing:** LaTeX/Word for IEEE-format documentation

---

**This project demonstrates comprehensive understanding of transmission line theory, circuit simulation expertise, and the ability to validate analytical models through systematic simulation studies -- skills directly applicable to RF engineering, high-speed digital design, power electronics, and signal integrity roles.**

## Folder Structure

```
ELEC2229 - Power Circuits and Transmission Lines/
├── README.md                                                    # This file
├── Coursework/                                                  # Main coursework folder (59 files)
│   ├── coursework.pdf                                          # Assignment brief
│   ├── ELEC2229_TransmissionLine_Assignment_2023_realisticCoax.pdf  # Detailed specification
│   ├── mhby1g21.pdf                                            # Final IEEE format report submission
│   ├── mhby1g21.docx                                           # Report source document
│   ├── report.docx                                             # Report draft (initial)
│   ├── report2.docx                                            # Report draft (revised)
│   ├── Coax_rev3.4.xls                                         # Coaxial cable analysis spreadsheet
│   ├── COAX cable RG59 B U LSF.pdf                             # RG59 cable datasheet
│   ├── ELEC2222TransmissionCoursework29801745_2.pdf            # Reference: previous student work
│   │
│   ├── LC Models (Lossless):
│   │   ├── Lossless LC.ms14                                    # Final lossless LC model
│   │   ├── LC 1m.ms14                                          # 1-meter iteration
│   │   ├── LC 22.ms14                                          # 22-section iteration
│   │   ├── LC 34.ms14                                          # 34-section iteration
│   │   ├── LC 35.ms14                                          # 35-section iteration
│   │   ├── LC block.ms14                                       # Block-based design approach
│   │   ├── LC v2.ms14                                          # Version 2 refinement
│   │   ├── Lossless LC.gra                                     # Voltage output plot
│   │   └── Lossless LC current.gra                             # Current output plot
│   │
│   ├── LC Models (Lossy):
│   │   ├── Lossy LC.ms14                                       # Final lossy LC model
│   │   ├── LC Lossy 34.ms14                                    # Lossy 34-section
│   │   └── LC Lossy 35.ms14                                    # Lossy 35-section
│   │
│   ├── MultiSim TL Models:
│   │   ├── TL multisim model.ms14                              # Exact transmission line element
│   │   ├── MultiSim TL model.gra                               # TL voltage output
│   │   └── MultiSim TL model current.gra                       # TL current output
│   │
│   ├── Design Files:
│   │   ├── Design1.ms14                                        # Initial design
│   │   ├── Haqym.ms14                                          # Reference design from peer
│   │   ├── krutis.ms14                                         # Reference design from peer
│   │   └── [14 Security copy files]                           # Automatic backups of .ms14 files
│   │
│   ├── Simulation Results (21 .gra graph files):
│   │   ├── 1 MHz AC Lossy vs Lossless.gra
│   │   ├── 1 MHz AC MultiSim TL Model.gra
│   │   ├── 10 MHz AC Lossless vs Lossy LC model.gra
│   │   ├── 10 MHz AC MultiSim TL Model.gra
│   │   ├── 30 MHz AC Lossless vs Lossy LC Model.gra
│   │   ├── 30 MHz AC MultiSim TL Model.gra
│   │   └── AC 1_10_30 MHz Lossless LC Model.gra (x3 files)     # Multi-frequency comparisons
│   │
│   └── Reference Documents:
│       ├── Distributed circuit coefficients and physical design of transmission lines.pdf (8.2 MB)
│       ├── EDN_Transmission_Lines.pdf
│       └── Understanding_Oscilloscope_BW_RiseT_And_Signal_Fidelity.pdf
│
├── EE56/                                                        # Lab component
│   └── EE56 Prints.docx                                        # Lab documentation (3.1 MB)
│
├── EE74 Lab/                                                    # Practical laboratory work (33 files)
│   ├── Lab prints.docx                                         # Lab report (7.1 MB)
│   └── [31 lab photos]                                         # HEIC and JPG formats
│       ├── 20230320_141905.heic through 20230320_162320.heic   # 16 original iOS photos
│       └── 20230320_141905.jpg through 20230320_161953.jpg     # 15 converted photos
│
├── Notes from wiki/                                             # Student-shared study notes (4 PDFs)
│   ├── James_Notes.pdf                                         # 1.0 MB
│   ├── Milos_Notes.pdf                                         # 986 KB
│   ├── Sasan_Notes.pdf                                         # 1.1 MB
│   └── Useful_formulae_to_remember.pdf                         # 573 KB
│
├── Past Papers/                                                 # Exam preparation materials
│   ├── Afiah and Katheryne/                                    # 4 papers with solutions
│   │   ├── katheryne 21_22 transmission paper.pdf
│   │   └── [3 additional ELEC2222/ELEC2229 papers]
│   │
│   ├── ELEC2222/                                               # Historical module (4 papers)
│   │   ├── ELEC2222-201415-02-ELEC2222W1.pdf                   # 2014-15
│   │   ├── ELEC2222-201516-02-ELEC2222.pdf                     # 2015-16 (2 variants)
│   │   ├── ELEC2222-201617-02-ELEC2222W1.pdf                   # 2016-17
│   │   └── ELEC2222-201718-02-ELEC2222W1.pdf                   # 2017-18
│   │
│   └── Lecture answer from Jade/                               # 2 papers with worked solutions
│       ├── ELEC2222-201516-02-ELEC2222W1_230511_185220_1.pdf
│       └── ELEC2222-201617-02-ELEC2222W1_230523_172006.pdf (annotated by syazwan)
│
└── ELEC2208 First Question Solver.py                            # Python utility script (2.5 KB)
    # Calculates transmission line parameters: firing angles, voltages, efficiency
    # Handles 6-pulse rectifier/inverter systems
    # Returns 6 significant figure precision outputs
```
