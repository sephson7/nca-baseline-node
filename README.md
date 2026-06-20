# nca-baseline-node

# NCA Project Baseline: Core Node Prototype

This repository contains the foundational architecture for low-voltage relay controls, time-stamped habit logging, and predictive ambient intelligence loops designed to bridge software engineering with physical mechanical systems.

## System Topology & Wiring Architecture

```text
+-----------------------------------------------------------------------+
|                       SMARTPHONE / WEB BROWSER INTERFACE              |
+-----------------------------------------------------------------------+
                                    |  (Wireless Local Network via Wi-Fi/Flask)
                                    v
+-----------------------------------------------------------------------+
|                       RASPBERRY PI CONTROLLER NODE                     |
|                                                                       |
|   +--------------------------+        +---------------------------+   |
|   | SQLite Database Engine   |        | Predictive Python Daemon  |   |
|   | (nelson_core_logs.db)    |        | (Pattern Recognition)     |   |
|   +--------------------------+        +---------------------------+   |
|                |                                    |                 |
|                | GPIO Pin 23 (Bulb Output)          | GPIO Pin 24     |
+----------------+------------------------------------+-----------------+
                 |                                    | (Fan Output)
                 v                                    v
+-----------------------------------------------------------------------+
|                       5V OPTOMECHANICAL RELAY BOARD                   |
|       [Channel 1 Input]                    [Channel 2 Input]          |
|               |                                    |                  |
+---------------+------------------------------------+------------------+
                | (Breaks 12V+ Rail)                 | (Breaks 12V+ Rail)
                v                                    v
+-------------------------------+    +----------------------------------+
| ELEMENT 01: HEATING LOAD SLAB |    | ELEMENT 02: VOLUMETRIC AIR FLOW  |
|      (12V Practice Bulb)      |    |        (12V Brushless Fan)       |
+-------------------------------+    +----------------------------------+
                |                                    |
                +-----------------+------------------+
                                  |
                                  v
+-----------------------------------------------------------------------+
|                    EXTERNAL 12V DC TRANSFORMER BUS                    |
+-----------------------------------------------------------------------+
