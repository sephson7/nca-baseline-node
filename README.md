# Nelson Core Automation (NCA) — N.E.L.S.O.N. Baseline Node

Welcome to the foundational repository for **N.E.L.S.O.N.** (*Networked Element Local System & Optimized Node*), developed by Nelson Core Automation.

## 🎯 The Core Vision
N.E.L.S.O.N. is an ecosystems-focused smart home controller engineered for modern families, dedicated athletes, and structured individuals. Traditional smart hubs rely entirely on unstable, privacy-invasive cloud networks. N.E.L.S.O.N. fundamentally changes this by processing behavioral data entirely at the edge on localized hardware. 

The goal of this system is to observe daily routines, store behavioral logs locally, learn host family patterns, and ultimately automate linked smart appliances (HVAC, Lighting, Refrigeration, and Laundry) to optimize energy use, protect privacy, and maximize human performance.

---

## 🛠️ Current Project Phase: Core Logic Simulation
**Status:** Pure Software Behavioral Testing

Before deploying to physical relays, microcontrollers, or customized chassis, the system's "brain logic" must be thoroughly simulated. This repository contains purely software-driven scenarios running in standard Python. 

By changing the input conditions (like the time of day, occupancy, or utility grid pricing), the localized core logic calculates and outputs immediate automation commands to simulated home appliances.

### Demonstrable Features in this Commit:
1. **Athlete Recovery Optimization:** Automatically scales HVAC down to an optimal cooling profile during targeted sleeping windows to assist muscle recovery.
2. **Grid-Aware Peak Intercept:** Minimizes utility costs by detecting high-rate peak hours and commanding energy-heavy smart appliances (like a refrigerator defrost cycle or laundry unit) to pause until rates drop.
3. **Privacy-First Local Computation:** Demonstrates how complex ecosystem decisions can be completely calculated without sending data to an external server.

---

## 📈 How to Run the Simulations
Because this code relies 100% on pure software logic and standard Python variables, **anyone can run this scenario node on their own system.**

To pull this repository down and execute the appliance ecosystem simulation on your local machine, open your terminal and run:

```bash
git clone [https://github.com/sephson7/nca-baseline-node.git](https://github.com/sephson7/nca-baseline-node.git)
cd nca-baseline-node
python nelson-ecosystem.py
