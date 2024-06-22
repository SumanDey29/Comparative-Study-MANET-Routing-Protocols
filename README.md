#Comparative Study of MANET Routing Protocols
Welcome to the "Comparative Study of MANET Routing Protocols" project! This repository contains the complete project work for comparing and analyzing different routing protocols in Mobile Ad hoc Networks (MANETs) using Network Simulator 3 (NS3). The primary focus of this project is to evaluate and contrast the performance of four major MANET routing protocols: DSDV, AODV, DSR, and OLSR.

##Table of Content
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Motivation](#motivation)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Tools Used](#tools-used)
- [Results and Analysis](#results-and-analysis)
- [Limitations](#limitations)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)

##Introduction
Mobile Ad hoc Networks (MANETs) are decentralized, infrastructure-less networks ideal for dynamic and resource-constrained environments. This project focuses on a detailed comparison of four MANET routing protocols: Destination-Sequenced Distance Vector (DSDV), Ad-hoc On-demand Distance Vector (AODV), Dynamic Source Routing (DSR), and Optimized Link State Routing (OLSR). Through rigorous simulations and performance evaluations, this study aims to provide essential insights into each protocol's strengths and weaknesses.

##Objectives
Compare and contrast DSDV, AODV, DSR, and OLSR routing protocols.
Evaluate protocols based on performance metrics: throughput, Packet Delivery Ratio (PDR), latency, and jitter.
Use NS3 for simulation and analysis.
Present findings through graphical comparisons to facilitate informed protocol selection.
Contribute to the understanding of MANET routing protocol performance in various scenarios.
Motivation
The growing importance of MANETs in modern communication scenarios motivated this study. MANETs' decentralized and infrastructure-less design makes them suitable for situations where traditional networks are impractical. This project aims to fill the gap in wireless networking research by providing comprehensive insights into both reactive and proactive MANET routing protocols through simulation-based assessments.

##Project Structure
src/: Contains the source code (.cc file) for the NS3 simulations.
output_files/: Contains the output files and data from the simulations, including pcap, flowmon, and trace files of different protocols.
output_plots/: Contains graphical representations of the simulation results.
plot_scripts/: Contains the required codes (GNU Plots, Python) for ploting the results.

##Installation
To set up the project, follow these steps:

**Install NS3 on Ubuntu 22.04 LTS.**

**Install required external tools:**

Wireshark
Trace Metric
Flow Monitor
NetAnim
GNUplot
Python

Analyze the output files:

Use Wireshark to analyze pcap files.
Use GNUplot to plot graphs from the data.

##Tools Used
NS3: Primary simulation framework.
Wireshark: For packet-level analysis.
NetAnim: For network visualization.
GNUplot: For generating graphical plots.
Flowmonitor: For traffic flow monitoring (not supported by DSR).
Pcap Tracefiles: For capturing packet-level details.

##Results and Analysis
The project compares the performance of DSDV, AODV, DSR, and OLSR protocols based on metrics like throughput, PDR, latency, and jitter. Graphical comparisons are provided to illustrate the strengths and weaknesses of each protocol.

##Limitations
A limitation encountered during this project was the inability to use Flowmonitor with the DSR protocol in NS3. As a result, comprehensive performance metrics for DSR were not available. Alternative methods were used to extract insights from pcap files for DSR.

##Future Work
Address security issues in MANET protocols.
Optimize protocols for better performance.
Enhance protocol parameters to improve QoS and energy efficiency.
Explore additional routing protocols beyond DSDV, AODV, DSR, and OLSR.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

Acknowledgements
We would like to thank our college for providing the necessary environment and resources for this project. Special thanks to our project supervisor, Prof. (Dr.) Anindya Sen, for his invaluable guidance.