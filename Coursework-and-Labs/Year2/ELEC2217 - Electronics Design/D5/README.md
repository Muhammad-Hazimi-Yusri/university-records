# D5 -- Smart Meter Design Project (ELEC2217)

**Module:** ELEC2217 -- Second-Year Group Design Project, University of Southampton
**Team:** Team B (6 members)
**Duration:** 7 weeks (30 Jan -- 17 Mar 2023)
**Budget:** GBP 40 (spent GBP 13.55)

## Project Overview

Design and build an autonomous **smart electricity meter** that manages power from renewable sources (wind + solar), battery storage, and unreliable mains to keep a fictional field hospital ("StormMed") operational during a disaster recovery scenario. The meter must fit inside a small waterproof enclosure (110x110x110mm max), consume under 2W, and operate completely autonomously during the 24-minute real-time test (simulating 24 hours).

### The Test Scenario -- "StormMed"

A portable field hospital deployed after a typhoon in New Zealand. The smart meter manages power to maximise the local population's survival rate.

**Energy Sources:**
| Source | Max Capacity |
|---|---|
| Wind turbine | 3A |
| Solar farm (PV) | 1A |
| Mains (unreliable) | 2A |
| Battery | 1A/hr, infinite capacity |

**Loads:**
| Load | Purpose | Current | Priority |
|---|---|---|---|
| Load 1 | Outdoor lighting & search equipment (08:00-22:00 only) | 1.2A | High |
| Load 2 | Life support for critical care | 2.0A | Highest |
| Load 3 | Indoor lighting & heating for operating theatre | 0.8A | Lower |

**Scoring (competitive across all 11 teams):**
- Survival rate (30%) -- keep loads powered
- Mains usage minimised (30%) -- use renewables first
- Renewables usage maximised (20%)
- Busbar voltage stability (20%)

## Team Members & Roles

| Member | Role |
|---|---|
| Giulio Girelli | Team Leader, Housing/Box Design (CAD) |
| Abi Brett | Secretary, PSU Design/Testing, Interface Design |
| Jerry Wang | PSU Design and Testing |
| Thomas (Tom) Short | Budget Manager, Interface Circuitry Design/Testing |
| **Syazwan Zulkepli** | **Software Lead** -- wrote the embedded C firmware and algorithm |
| **Muhammad Yusri (me)** | **Quality Lead** -- Integration, QA, and LabVIEW Simulation |

## My Contributions (Muhammad)

### Integration & Quality Assurance
- Responsible for overall system integration -- bringing PSU, interface circuitry, software, and housing together
- Conducted quality checks at each project milestone
- Troubleshot hardware issues including circuit soldering problems on the PSU (had to identify faults for Jerry to fix)
- Managed the integration timeline during Weeks 5-7

### LabVIEW Simulation
- Ran Syazwan's algorithm through the **LabVIEW Smart Grid Testbed** emulator before the final physical test
- Tested against all 3 provided data profiles (wind, solar, load demand TDMS files)
- The simulation results showed strong performance -- **indicative mark of 78.18%** in emulation with metrics:
  - Mains usage: 35.9%
  - Renewables usage: 93.89%
  - Busbar transient stability: 97.68%
  - Battery usage ratio: 137.15%
  - Survival rate: 172/250 (68.8%)

### Reports & Presentation
- Wrote the progress/plans section, introduction, and conclusion of the group reports
- Presented quality checks and project plans during the first review presentation

## System Architecture

```
  230V AC Mains
       |
  [Capacitor-Drop PSU] --> 12.4V --> [Op-Amp Reference]
       |                         --> [LM3090 Regulator] --> 3.1V --> [Il Matto MCU]
       |
  [LabVIEW Testbed] <--RJ45--> [Interface Circuitry] <--> [ATmega644P "Il Matto"]
       |                              |                          |
   Wind/Solar/Load              Analog: PWM-to-DC,         Firmware (prog.c):
   TDMS Profiles              Full-wave rectifiers         - ADC readings
                              Digital: MOSFET level         - Algorithm logic
                                shifters (5V<->3.3V)       - PWM output
                                                           - TFT Display (ILI9341)
```

### Key Technical Details

**PSU (Jerry & Abi):**
- Capacitor-drop design: 230V AC --> full-wave bridge rectifier (1N4148) --> 12V Zener clamp --> smoothing (6800uF)
- 60% efficiency, 1.5W consumption, 0.9W output
- External LM3090 voltage regulator for stable 3.1V to MCU

**Interface Circuitry (Tom & Abi):**
- PWM-to-analog: RC filter (33k/10nF) + op-amp, scales 0-3.3V PWM to 0-10V DC for mains capacity control
- Busbar measurement: full-wave diode bridge rectifiers with RC smoothing
- Digital level shifters: single MOSFET inverting circuits (5V to 3.3V, one per load)
- Designed and simulated in LTSpice

**Software (Syazwan):**
- Embedded C for ATmega644P
- ADC reads: wind, solar, busbar voltage, busbar current
- Digital reads: 3 load demand signals
- Algorithm: prioritises Load 2 (life support) > Load 1 (search) > Load 3, uses renewables first, battery as buffer, mains as last resort
- PWM output for mains current request
- TFT display with colour-coded status indicators and bar charts

**Housing (Giulio):**
- 105x105x105mm, 4-piece 3D-printed enclosure (SolidWorks)
- Laser-cut acrylic display cover + rubber gaskets for IP55-level water resistance
- PSU segregated in top section with printed floor divider
- 4x RJ45 connectors (left), TFT display (right), green LED indicator

## Project Timeline

| Week | Milestone |
|---|---|
| 1 | Team roles assigned, Gantt chart created, initial design discussions |
| 2 | PSU design (capacitor-drop chosen, 60% efficiency), box CAD started, software begun |
| 2 | **First Review** -- presentation: box, PSU, interface, software progress, QA plans |
| 3 | Component orders, box redesigned (4-part, 100x100x100 internal), interface finalised |
| 4 | PSU soldered & tested at testbed, interface tested on breadboard, box 3D-printed & assembled |
| 4 | **Second Review** -- PSU trial, box water test, group report submitted |
| 5 | Interface soldered to stripboard, algorithm tested in LabVIEW, full integration started |
| 6-7 | Final integration, testing, adjustments |
| 7 | **Final Review** -- autonomous 24-min test on LabVIEW testbed |
| 7 | Final report, spec sheet, reflective accounts submitted |

## Results

### Simulation (LabVIEW Emulator) -- What the Algorithm Could Do
| Metric | Score |
|---|---|
| Mains usage | 35.9% |
| Renewables usage | 93.89% |
| Busbar transient stability | 97.68% |
| Survival rate | 172/250 (68.8%) |
| **Indicative mark** | **78.18%** |

### Actual Physical Test -- What We Got
| Metric | Score |
|---|---|
| Mains usage | 36.32% |
| Renewables usage | 0% |
| Busbar transient stability | 89.25% |
| Survival rate | 71/250 (28.4%) |
| **Group mark** | **45.47%** |

### What Went Wrong

The massive gap between simulation (78%) and physical test (45%) was primarily due to **hardware issues with the PSU**:

- The PSU couldn't cope with the algorithm's switching demands, causing unreliable power delivery
- Renewables usage dropped from 93.89% to **0%** in the physical test -- the signals were too degraded
- The busbar voltage stability graphs showed wild oscillations in the physical test vs clean signals in simulation
- The TFT display was noticeably dim during testing -- a symptom of insufficient/unstable power
- The PSU also had grounding issues that **electrically shocked a team member (Abi)** during one test session

The software/algorithm (Syazwan) and integration/simulation (myself) performed well in isolation -- the LabVIEW emulator results prove the logic was sound. The bottleneck was the PSU and potentially the interface circuitry's ability to produce clean signals when powered by an unstable supply.

## Assessment Breakdown

| Component | Weight | Type |
|---|---|---|
| First Review (logbook + design quality) | 20 marks | 10 individual + 10 group |
| Second Review (PSU trial + water test) | 25 marks | 10 individual + 7 PSU + 8 box |
| Final Review (compliance + test score) | 15 marks | 5 compliance + 10 test |
| Final Report + Spec Sheet | 20 marks | 15 report + 5 spec |
| Individual Reflective Account + Logbook | 20 marks | Individual |

**Overall split:** 40% individual / 60% group

## Folder Structure

```
D5/
├── README.md                          # This file
├── Datasheets/                        # TFT display datasheets (DT022B, ILI9341)
├── Housing/                           # Box design files
│   └── Box/
│       ├── overall/                   # SolidWorks CAD, acrylic (CorelDRAW), gaskets
│       │   ├── housing/              # Multiple design iterations (1/, 2/, attempt/, final/)
│       │   ├── acrylic/              # Laser-cut acrylic panel designs (.cdr)
│       │   └── gaskets/              # Gasket designs (.cdr)
│       ├── tests/                    # Test prints (bolt, display, RJ45 fit tests)
│       └── PRINT/                    # Final 3D-printable STL + SLDPRT files
├── Interface Circuitry/               # LTSpice schematics
│   ├── D5(1).asc                     # All interface sub-circuits (early version)
│   └── Final_Interface.asc           # Final refined interface design
├── PSU/                               # Power supply design
│   ├── Final_PSU.asc                 # Final LTSpice schematic
│   ├── PSUv1.asc                     # Earlier version
│   ├── Components order.docx         # Component order list
│   └── Team_B_Capacitor_PSU_.pdf     # PSU design document
├── Simulation/                        # LabVIEW simulation files
│   ├── In Lab/                       # VIs for physical lab testbed
│   ├── Remote/                       # VIs for remote emulation
│   ├── Profile 1-3/                  # TDMS data profiles (wind, solar, loads)
│   ├── D5 Data Profiles.xlsx         # Simulation data profiles
│   └── *_output*.png                 # Simulation result screenshots
├── Software/                          # Embedded firmware
│   ├── prog.c                        # Main C firmware (ATmega644P)
│   ├── cmd.txt                       # AVR build/flash commands
│   ├── Smartmeter logic_*.pdf        # Algorithm flowchart
│   └── *.pdf                         # Reference docs (Il Matto QR, C ref, ASCII)
├── Report/                            # Formal team reports
│   ├── TeamB-2ndReview-24.2.2023.docx
│   └── TeamB-FinalReport-17.3.2023.docx
├── images/                            # Photos of the physical prototype
├── TeamB-FinalReport2docx.docx        # Final report (copy)
├── TeamB-SpecSheet.docx               # Product specification sheet
├── Software section of group report.docx
├── PSU Final report.docx
├── Team B - Meeting Minutes.docx      # 12 meeting minutes across 5 weeks
├── Team B.pptx                        # First review presentation
├── Project_Gant_Chart.xlsx            # Project Gantt chart
├── Deadlines.xlsx                     # Module deadline tracker
├── ELEC2217 Mark Scheme 2023 v2.pdf   # Assessment criteria
├── Final Test Scenario 2023 v3UoS.pdf # StormMed test scenario spec
├── Southampton Handbook 2023v1.18.pdf # Module handbook
└── gantt chart.jpg                    # Gantt chart image
```
