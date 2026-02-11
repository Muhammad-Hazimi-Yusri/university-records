# ELEC3227 -- Embedded Networked Systems

**Module:** ELEC3227 -- Third-Year Individual Coursework, University of Southampton
**Team:** Team E2 (3 members)
**Academic Year:** 2023/24
**Duration:** 11 weeks (24 Oct 2023 -- 8 Jan 2024)
**Assessment Weight:** 40% of ELEC3227 final grade

## Project Overview

Design and implement a **full network protocol stack** for a smart lighting application on embedded hardware. The coursework required creating a distributed system where multiple nodes (with switches and lights) communicate wirelessly to control lighting across the network. Each input can control one or more outputs, supporting distributed applications rather than a centralized hub architecture.

### The Challenge

Build a complete layered networking architecture (Application, Transport, Network, Data Link, Physical) capable of supporting smart lighting applications. The system must:

- Run on resource-constrained **Il Matto** microcontrollers (ATmega644P with 16K Flash, 2K EEPROM, 1K SRAM)
- Use **RFM12B** radio modules for wireless communication
- Support reliable, connection-oriented data transfer (TCP-like protocol)
- Handle distributed control (e.g., Node 1 button controls Node 2 LED, multi-hop routing)
- Implement protocol standards collaboratively while maintaining individual implementations

### Individual vs Team Work

This was **individual coursework**, but students worked in **teams** to:
- Design and standardize protocol specifications for each layer
- Define inter-layer interfaces
- Test integrated protocol stacks

Each team member implemented different layer(s) independently. **Peer-teammates** (students working on the same layers across different teams) collaborated on layer standards. For example, Team E1 and E2's Transport/Application developers jointly defined the Transport Layer Standard.

## Team Members & Layer Responsibilities

| Member | Layers Responsible |
|---|---|
| **Muhammad Hazimi (me)** | **Transport Layer + Application Layer** |
| Jade | Network Layer |
| Syazwan | Data Link Layer + Physical Layer |

**Note:** Students from **Team E1** and **Team E2** (peer-teams) collaborated on defining layer-specific standards:
- **Application/Transport Standard** -- co-authored by Muhammad Hazimi (E2) and Law Shew Zuan (E1)
- **Network Layer Standard** -- authored by team network layer developers
- **Data Link Layer Standard** -- authored by team DLL developers

## My Contributions (Muhammad Hazimi)

### Transport Layer -- TCP-Like Reliable Protocol

Designed and implemented a **connection-oriented, reliable transport protocol** modeled after TCP, tailored for the Il Matto's constrained resources.

**Key Features:**
- **3-Way Handshake (SYN-SYNACK-ACK):** Establishes reliable connections between nodes before data transfer
- **Segment Structure:** Custom 17-byte segment format with control bits, ports, sequence/acknowledgment numbers, length field, application data, and XOR checksum
- **Flow Control:** Sliding window mechanism with buffer (BUF) control to prevent receiver overflow
- **Error Detection:** XOR checksum (2 bytes) for data integrity verification
- **Disconnect Request (DR):** Graceful connection teardown
- **Retransmission Logic:** Handles lost segments with timeout-based retransmission

**Segment Field Structure:**

| Field | Size | Description |
|---|---|---|
| Control [2] | 2 bytes | SYN, ACK, DR, BUF flags + reserved bits |
| SRC Port [1] | 1 byte | Source port (0x00 for buttons, 0xFF for UART) |
| DEST Port [1] | 1 byte | Destination port (0x00 for LEDs, 0xFF for UART) |
| Length [1] | 1 byte | APP data length (0 during handshake, max 9 bytes) |
| APP Data [1-14] | 1-9 bytes | Application layer payload |
| Checksum [2] | 2 bytes | XOR checksum for error detection |
| SEQ NUM (left byte) | 7:4 bits | Sequence number |
| ACK NUM (right byte) | 3:0 bits | Acknowledgment number |

**Control Bits:**
- **SYN:** Synchronize (handshake initiation)
- **ACK:** Acknowledgment
- **BUF:** Buffer space indicator
- **DR:** Disconnect request
- **PERSONALUSE:** Reserved for custom features

**Why TCP over UDP?**
Chose TCP-like reliability for smart lighting because:
- Data integrity is critical (incorrect LED commands could cause flickering or wrong states)
- Connection-oriented model suits request-response patterns (button press → LED change)
- Error checking and retransmission ensure stable lighting control
- CSMA p-persistent MAC (from DLL) + TCP minimizes collision impact

**Trade-offs:**
- **No bandwidth allocation or congestion control** -- periodic, bursty data with low overhead; microcontroller efficiency prioritized
- **Multicast via flooding:** For commands to multiple recipients, Application layer sends multiple TCP segments or Network layer uses flooding (IP 0)

### Application Layer -- Smart Lighting Interface

Designed the **user-facing application protocols** that interface with hardware (buttons, LEDs, UART) and translate user actions into network traffic.

**Two Main Applications:**

**1. Button-LED Interaction (1 byte APP data)**
- Button press on one node controls LEDs on adjacent or remote nodes
- **Button ON:** Sends `0xFF` → Turns on target LED
- **Button OFF:** Sends `0x00` → Turns off target LED
- Ports: `0x00` for buttons/LEDs
- Example: Node E11 button press → E12 LED lights up (1-hop), or E11 → E13 (2-hop via E12)

**2. UART Communication (9 bytes APP data)**
- Serial terminal commands for debugging and advanced control
- 9-byte maximum message length (constrained by Il Matto memory)
- Ports: `0xFF` for UART source/destination
- **Command Examples:**
  - `SEND E11 <MESSAGE>` -- Send string to Node E11
  - `ON E11` -- Turn on LED on Node E11
  - `OFF E23` -- Turn off LED on Node E23
  - `ON E11 R5G9B7` -- Optional: Control RGB LED with brightness levels
- **Special character `"/"`:** Toggle between input/output mode in UART CLI

**Hostname Resolution:**
- Hostname-to-IP address table for user-friendly addressing
- Hostnames: **E11, E12, E13** (Team E1) and **E21, E22, E23** (Team E2)
- Application layer resolves hostname → IP address → passes to Transport layer

**Hardware Pin Assignments:**
- **LED:** PC6 (additional LEDs on Port C for standardization)
- **Button:** PA6 (additional buttons on Port A, debounced in software)
- **UART:** Port D
- **RFM12B Radio:** Port B

### Protocol Standards Documentation

Co-authored the **Team E Application and Transport Layer Standards** document with Law Shew Zuan (Team E1), defining:
- Application layer packet formats and service interfaces
- Transport layer segment structure, handshake procedures, and error handling
- Inter-layer APIs (APP ↔ TRAN ↔ NET interfaces)
- Memory-efficient design considerations for AVR architecture

### Integration & Testing

- Integrated Transport and Application layers with Jade's Network layer and Syazwan's DLL/Physical layer
- Tested on Il Matto hardware during practical demonstration (15 Dec 2023)
- Debugged inter-layer communication issues (e.g., segment size mismatches, checksum failures)
- Validated multi-hop routing scenarios with team protocol stack

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│  User Interaction (Buttons, LEDs, UART Terminal)       │
└─────────────────┬───────────────────────────────────────┘
                  │
┌─────────────────▼────────────────────────────────────────┐
│  APPLICATION LAYER (Muhammad Hazimi)                     │
│  - Button-LED protocol (1 byte: 0xFF/0x00)              │
│  - UART messaging (9 bytes max)                          │
│  - Hostname → IP resolution                              │
└─────────────────┬────────────────────────────────────────┘
                  │ Destination port, source port, APP data
┌─────────────────▼────────────────────────────────────────┐
│  TRANSPORT LAYER (Muhammad Hazimi)                       │
│  - TCP-like 3-way handshake (SYN/ACK/DR)                │
│  - Segmentation, sequencing, acknowledgment              │
│  - XOR checksum, retransmission, flow control            │
│  - 17-byte segment structure                             │
└─────────────────┬────────────────────────────────────────┘
                  │ Destination IP, segment
┌─────────────────▼────────────────────────────────────────┐
│  NETWORK LAYER (Jade)                                    │
│  - Routing (multi-hop support)                           │
│  - IP addressing (E11-E23)                               │
│  - Flooding for multicast (IP 0)                         │
└─────────────────┬────────────────────────────────────────┘
                  │ Frame
┌─────────────────▼────────────────────────────────────────┐
│  DATA LINK LAYER (Syazwan)                               │
│  - CSMA p-persistent MAC                                 │
│  - Error control (CRC from NET/DLL)                      │
│  - Framing                                               │
└─────────────────┬────────────────────────────────────────┘
                  │ Bits
┌─────────────────▼────────────────────────────────────────┐
│  PHYSICAL LAYER (Syazwan)                                │
│  - RFM12B radio module (wireless transmission)           │
│  - Modulation, bit encoding                              │
└──────────────────────────────────────────────────────────┘
```

### Transport Layer Flow (Connection Lifecycle)

**Sender Side (Establishing Connection):**
1. Check if TCP connection established?
   - **No:** Send SYN flag → Wait for SYNACK
   - **Yes:** Proceed to data transfer
2. Have APP data to send?
   - **Yes:** Send segment with APP data → Record sent segment for acknowledgment
   - **No:** Send disconnect request (DR)

**Receiver Side (Accepting Connection):**
1. TCP connection established?
   - **No:** Receive SYN → Send SYN+ACK flag → Wait for final ACK
   - **Yes:** Receive APP data
2. SYN flag set?
   - **Yes:** Connection established
   - **No:** Discard segment
3. Receive APP data → Extract acknowledgment from segment → Forward to APP layer

**For integrated version, virtual connections pass parameters between layers (not shown in per-layer testing).**

## Key Technical Details

**Hardware Platform:**
- **Microcontroller:** ATmega644P (Il Matto variants: 164P/324P/644P/1284P)
  - Flash: 16K (164P/PA) to 128K (1284P)
  - EEPROM: 2K (164P/PA)
  - SRAM: 1K (164P/PA)
  - Target: Fit entire protocol stack under 64KB compiled code
- **Radio:** RFM12B-S2 wireless module (868 MHz ISM band)
- **Programming:** Embedded C (avr-gcc toolchain), compiled for AVR architecture

**Memory Optimization:**
- Used `uint8_t` (1-byte unsigned integer) for most variables to minimize memory usage
- SRAM constraint (1K) required careful buffer management
- Protocol designed to avoid deep call stacks and large data structures

**Protocol Standards:**
- **Team E Application/Transport Standard** -- 9-page document defining APP and TRAN layers
- **Team E Network Layer Standard** -- Routing algorithms, IP addressing
- **Team E DataLink Standard** -- MAC protocols, framing
- **Team E Combined Standard** -- Full integrated protocol stack specification

**Development Environment:**
- Linux WSL (Windows Subsystem for Linux) for avr-gcc toolchain
- Git version control (branch-specific development, integrated testing)
- VSCode / Embedded IDE (EIDE)
- LabVIEW for earlier lab exercises (not used in final coursework)

## Project Timeline

| Date | Milestone |
|---|---|
| 24 Oct 2023 | Coursework assigned, team roles decided |
| Oct-Nov 2023 | Layer-specific design and protocol standardization |
| 17 Nov 2023 | **Standard Document Submission** -- Protocol specifications finalized |
| Nov-Dec 2023 | Individual layer implementation (Transport + Application layers coded) |
| Dec 2023 | Integration testing with team (APP ↔ TRAN ↔ NET ↔ DLL ↔ PHY) |
| 15 Dec 2023 | **Practical Demonstration** -- Live test on Il Matto hardware, oral feedback |
| 8 Jan 2024 | **Written Report Submission** -- Individual coursework report |

## Deliverables

### Protocol Standards (Team Collaboration)
- `Team_E_Application_Transport_Standard.pdf` (co-authored with Law Shew Zuan, E1)
- `Team_E_Network_Layer_Standards.pdf` (Jade + peer-teammates)
- `Team_E_DataLink_Standard.pdf` (Syazwan + peer-teammates)
- `Team_E_Combined_Standard.pdf` (Full protocol stack integration)

### Individual Submissions
- **Coursework Report** (`Report.pdf`, `Report.docx`) -- 10+ pages detailing Transport/Application layer design, implementation, and testing
- **Coursework Logbook** (`cw logbook.docx`) -- Weekly progress tracking
- **Source Code:**
  - `Coursework/branch-specific/` -- Modular development (application, transport, network folders)
  - `Coursework/integrated/` -- Final integrated protocol stack (E1main.c, E1main.hex)
  - `apptran.c`, `apptran.h` -- Application + Transport layer implementation

### Practical Demonstration
- Live demo on Il Matto hardware (3-4 nodes from Team E)
- Demonstrated button-LED control, multi-hop routing, UART messaging
- Oral Q&A with Prof Geoff Merrett and Dr Alex Weddell

## Assessment Breakdown

| Component | Deadline | Type |
|---|---|---|
| Standard Document | 17 Nov 2023, 11:00 | Team collaboration (peer-teammates) |
| Practical Demonstration | 15 Dec 2023, 12:00-17:00 | Individual demo, oral feedback |
| Written Report | 8 Jan 2024, 16:00 | Individual report |

**Overall Weight:** 40% of ELEC3227 final grade
**Examiners:** Professor Geoff Merrett, Dr Alex Weddell
**Expected Effort:** Up to 60 hours

**Note:** Individual coursework, but collaborative protocol standards. Working with **peer-teammates** (same layer, different teams) for standardization was **explicitly allowed and encouraged**. Implementation and report were individual work.

## Learning Outcomes Achieved

- **Layered Networking Models:** Designed and implemented OSI-inspired protocol stack (APP, TRAN, NET, DLL, PHY)
- **Protocol Standardization:** Co-authored technical standards documents following RFC-style conventions
- **Technical Communication:** Documented complex protocols, presented work in written report and oral demo
- **Embedded Networking:** Implemented protocols on resource-constrained hardware (Il Matto + RFM12B), handling memory limits, real-time constraints

**Key Skills:**
- Embedded C programming (AVR/ATmega architecture)
- TCP protocol design (handshake, sequencing, acknowledgment, checksum)
- Wireless sensor networking (RFM12B radio)
- Protocol layering and interface design
- Git version control for embedded projects
- Cross-compilation (Linux WSL, avr-gcc, avrdude flashing)

## Folder Structure

```
ELEC3227 Embedded Networked System/
├── README.md                                        # This file
├── Coursework/                                      # Main coursework implementation
│   ├── ELEC3227c-202324-v4.pdf                     # Coursework specification
│   ├── Report.pdf / Report.docx                     # Individual coursework report
│   ├── cw logbook.docx                              # Weekly progress logbook
│   ├── branch-specific/                             # Modular development (per-layer branches)
│   │   ├── application/                             # Application layer module
│   │   ├── transport/                               # Transport layer module
│   │   ├── network/                                 # Network layer module (Jade)
│   │   ├── apptran.c / apptran.h                   # Combined APP+TRAN implementation
│   │   ├── E1main.c / E1main.hex                   # Main program for Team E
│   │   ├── Makefile                                 # Build configuration (avr-gcc)
│   │   ├── MyAddresses.txt                          # Hostname/IP mapping
│   │   └── lib/                                     # Shared libraries (RFM12B drivers)
│   ├── integrated/                                  # Fully integrated protocol stack
│   │   ├── E1main.c / E1main.hex                   # Final integrated firmware
│   │   ├── apptran.c / apptran.h                   # APP + TRAN layers
│   │   ├── network.c / network.h                    # Network layer (Jade)
│   │   ├── application/, transport/, network/       # Layer-specific test programs
│   │   └── demo/                                    # Demo applications
│   └── Lab 2 and 3 Solution/                        # Earlier lab exercise solutions
├── Slides/                                          # Lecture materials
│   ├── L0 Welcome to ELEC3227 and ELEC6255.pdf
│   ├── L1 Computer Networks.pdf
│   ├── 01 Network Layer 1.pdf
│   ├── 02 Transport Layer 1.pdf
│   ├── 03 Application Layer 1.pdf
│   ├── 04-05 Security 1-2.pdf
│   ├── 07 Application Layer - 2.pdf
│   ├── 08-09 Transport Layer 2-4.pdf
│   ├── 10-11 Network Layer 2-3.pdf
│   ├── L15 IEEE 802.15.4.pdf                        # Wireless sensor networks
│   ├── L16 Bluetooth.pdf
│   └── ELEC3227 - Energy Efficient Networking.pdf
├── Past Papers/                                     # Exam papers (2019-2022)
│   ├── ELEC3227_202223_q.pdf
│   ├── ELEC3227-202122q.pdf
│   ├── ELEC3227-202021q.pdf
│   └── ELEC3227-201920-01-ELEC3227W1.pdf
├── Team E Network Layer Standards/                  # LaTeX source for standards
│   ├── Weekly_Report_Michael.tex                    # Network layer standard (LaTeX)
│   ├── reference-file.bib                           # Bibliography
│   ├── figures/                                     # Diagrams and figures
│   └── notes/                                       # Design notes
├── Team_E_Application_Transport_Standard.pdf        # APP+TRAN standard (2 versions)
├── Team_E_Network_Layer_Standards.pdf               # Network layer standard
├── Team_E_DataLink_Standard.pdf                     # DLL standard
├── Team_E_Combined_Standard.pdf                     # Full integrated standard (2 versions)
├── Andrew Tanenbaum - Computer Networks.pdf         # Reference textbook
├── Coursework.zip                                   # Archived coursework files
├── Team E Network Layer Standards.zip               # Archived standards
└── deprecated/                                      # Earlier implementations (not used)
    ├── .git/                                        # Old git repository
    ├── include/, librfm12/, test/                   # Old code structure
    └── build/                                       # Old build artifacts
```

## References & Resources

- **Textbook:** Andrew Tanenbaum & David Wetherall, *Computer Networks* (5th Edition, Pearson 2021)
- **Hardware:** Il Matto Quick Reference Sheet (ATmega644P pinout, memory specs)
- **RFC Standards:** TCP/IP protocols (RFC 793 - TCP, RFC 791 - IP)
- **AVR Programming:** AVR-GCC documentation, ATmega644P datasheet
- **RFM12B Radio:** RFM12B-S2 datasheet, librfm12 C library

---

**Note:** This coursework emphasized **protocol design principles** and **embedded systems programming** in a constrained environment. The challenge was balancing feature-rich networking (reliable TCP, routing, application services) with severe memory and processing limitations (1K SRAM, 16K Flash). The experience mirrors real-world IoT and wireless sensor network development.
