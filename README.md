# Nelson Core Automation (NCA) — Baseline Node

Welcome to the foundational repository for **N.E.L.S.O.N.** (*Networked Element Local System & Optimized Node*), developed by Nelson Core Automation.

## 🎯 The Vision
N.E.L.S.O.N. is an ecosystems-focused smart home controller engineered for the modern family, dedicated athletes, and structured individuals. Unlike traditional smart hubs that rely entirely on unstable cloud networks, N.E.L.S.O.N. processes data locally at the edge. 

It is designed to seamlessly learn the routines, habits, and physiological environments of its host family—anticipating localized climate adjustments, maximizing athletic sleep recovery, and calculating optimal energy-saving configurations by recommending when to scale peripheral hardware components up or down.

---

## 🛠️ Current Project Phase: Square One (Pure Simulation)
**Status:** Software Architecture & Logic Prototyping

Every great automation machine starts with a single line of logic. To ensure stability, safety, and core competency, this phase of the project uses **pure software simulations** running on local computing hardware (Laptop) to map out how environmental inputs directly dictate automated system actions.

### Core Concepts Demonstrated:
1. **The Input Loop:** Reading state data (simulated temperatures, occupancy tracking, and recovery targets).
2. **The Logic Bridge:** Processing data points against user routines (e.g., Athlete Sleep Optimization Window).
3. **The Localized Output:** Dictating system decisions locally without external cloud dependency to protect consumer privacy.

---

## 🚀 Future Roadmap
As my engineering and programming education scales, this software repository will transition through the following physical development cycles:

* **Phase 1 (Current):** Pure Python environment simulation (laptop-side testing).
* **Phase 2:** Local API integrations using lightweight web frameworks (Flask) to interact with localized devices.
* **Phase 3:** Hardware deployment onto physical localized nodes utilizing relay switches and low-voltage external circuitry.
* **Phase 4:** Production of the localized industrial chassis, featuring modular Universal Inputs and a customized, host-nameable HMI automation persona.

---

## 📈 Running the Simulations
To run the local behavioral scenario logic on your machine, clone this repository and execute the primary node script:

```bash
git clone [https://github.com/sephson7/nca-baseline-node.git](https://github.com/sephson7/nca-baseline-node.git)
cd nca-baseline-node
python nelson_simulation.py
