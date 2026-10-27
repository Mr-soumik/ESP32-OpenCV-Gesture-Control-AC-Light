# ⚡ ESP32 & OpenCV Hand Gesture AC Load Control (Offline USB-Serial)

A professional DIY IoT and Computer Vision project that allows you to control a high-voltage 220V AC appliance (like a light bulb or fan) using simple hand gestures captured by your laptop's webcam. This system runs completely **offline**, leveraging USB Serial communication between Python (OpenCV + MediaPipe) and an ESP32 microcontroller.

# Demo Video Link👇
## YouTube Tutorial👉 
## YouTube shorts👉
## Facebook👉 
## Instagram👉
<img width="4096" height="1840" alt="IMG_20261027_124338 jpg" src="https://github.com/user-attachments/assets/882b0867-4127-4ec8-b7f8-9a5e370a4bb5" />



# Connect with TechTadka360💝👇

- YouTube: [@techtadka360official](https://youtube.com/@techtadka360official?si=GdlIntZKv30kPgBk)
- Instagram: [@techtadka360official](https://www.instagram.com/techtadka360official?igsh=cWR4bnhjdWw1MHdh)
- Facebook: [TechTadka360](https://www.facebook.com/share/1EkKAJNLdB/)
---

## 🚀 Features
* **Real-Time Computer Vision:** Tracks hand landmarks locally using MediaPipe and OpenCV.
* **Offline & Secure:** Uses direct USB Serial communication—no Wi-Fi network, cloud dependency, or internet connection required.
* **AC Mains Control:** Safely controls 220V AC appliances via a 1-Channel Relay module.
* **Low Latency:** Instant hardware response upon gesture recognition.

---

## 📦 Components Required

| Component | Description | Qty |
| :--- | :--- | :--- |
| **ESP32 DevKit V1** | Microcontroller board | 1 |
| **1-Channel Relay Module** | Optocoupler-isolated relay (5V/3.3V) | 1 |
| **AC Load / Bulb Holder** | 220V Bulb and connection wires | 1 |
| **Connecting Wires** | Male-to-Female / Male-to-Male jumper wires | Set |
| **USB Cable** | Data cable for programming and serial communication | 1 |

---

## 🔌 Circuit Wiring Diagram

| ESP32 Pin | Relay Module Pin | Description |
| :--- | :--- | :--- |
| **GPIO 23** | IN | Digital control signal input |
| **5V / 3.3V** | VCC | Power supply |
| **GND** | GND | Common Ground |

### **AC High-Voltage Wiring Warning:**
> ⚠️ **DANGER OF ELECTROCUTION:** Working with 220V AC mains power is extremely hazardous. Ensure the ESP32 and relay are completely unplugged from power while wiring. Properly insulate all high-voltage connections before testing.

1. Connect one wire of the AC main supply directly to one terminal of the bulb holder.
2. Connect the second AC main supply wire to the **COM (Common)** terminal of the relay module.
3. Connect the **NO (Normally Open)** terminal of the relay module to the second terminal of the bulb holder.

---

## 🛠️ Step-by-Step Setup Guide

### **Step 1: Flash the ESP32 Firmware**
1. Open the **Arduino IDE**.
2. Install the ESP32 board package if you haven't already.
3. Copy the code from [esp32_relay_control.ino](esp32_relay_control.ino) and paste it into your IDE.
4. Select your correct ESP32 board and **COM Port**, then click **Upload**.

### **Step 2: Install Python Dependencies**
Open your terminal or command prompt and install the required Python computer vision and serial communication packages:
```bash
pip install opencv-python mediapipe pyserial
