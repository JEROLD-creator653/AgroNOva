import streamlit as st
import random

st.set_page_config(page_title="Nimbus Alert", layout="wide")

# Sidebar toggle for background
bg_choice = st.sidebar.radio("🌄 Choose Background", ["Rain Animation", "Farm Video"])

# Background CSS + HTML
if bg_choice == "Rain Animation":
    st.markdown("""
        <style>
        body {
          background: linear-gradient(135deg,#667eea 0%,#764ba2 100%);
          overflow: hidden;
        }
        .rain-container {
          position: fixed;
          top: 0;
          left: 0;
          width: 100vw;
          height: 100vh;
          overflow: hidden;
          z-index: -1;
        }
        .raindrop {
          position: absolute;
          width: 2px;
          height: 15px;
          background: rgba(255,255,255,0.6);
          animation: fall linear infinite;
        }
        @keyframes fall {
          0% { transform: translateY(-10vh); }
          100% { transform: translateY(110vh); }
        }
        </style>
        <div class="rain-container">
    """, unsafe_allow_html=True)

    rain_html = ""
    for i in range(80):
        left = random.randint(0, 100)
        duration = round(random.uniform(1, 3), 2)
        delay = round(random.uniform(0, 2), 2)
        rain_html += f"""
        <div class="raindrop" style="left:{left}vw; animation-duration:{duration}s; animation-delay:{delay}s;"></div>
        """

    st.markdown(rain_html + "</div>", unsafe_allow_html=True)

else:  # Farm Video Background
    st.markdown("""
        <style>
        .video-background {
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          object-fit: cover;
          z-index: -1;
        }
        </style>
        <video autoplay muted loop class="video-background">
          <source src="https://videos.pexels.com/video-files/853889/853889-hd_1920_1080_30fps.mp4" type="video/mp4">
        </video>
    """, unsafe_allow_html=True)

# Header
st.markdown("<div style='text-align:center;color:white;margin:20px;'><h1>☁ Nimbus Alert</h1><p>Smart Rain Detection & Notification System for Farmers</p></div>", unsafe_allow_html=True)

# Live Weather Dashboard
st.subheader("🌦 Live Weather Dashboard")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Humidity", f"{random.randint(65,75)}%")
col2.metric("Temperature", f"{round(22+random.random()*6,1)}°C")
col3.metric("Pressure", f"{1010+random.randint(0,10)} hPa")
col4.metric("Rainfall", f"{round(random.random()*5,1)} mm")

# Hardware Components
st.subheader("⚙ Hardware Components")
components = {
    "Arduino Uno R3": "Microcontroller board based on ATmega328P, used to collect sensor data.",
    "ESP32 WiFi Module": "Provides WiFi connectivity to send data to the cloud server.",
    "DHT22": "Measures temperature and humidity with good accuracy.",
    "BMP280": "Pressure and altitude sensor used for weather prediction.",
    "Rain Drop Sensor": "Detects rainfall intensity.",
    "Solar Panel + Battery": "Provides renewable power to the system.",
    "GSM Module (SIM800L)": "Used for SMS and call notifications in remote areas."
}
if st.button("View Specifications"):
    for name, desc in components.items():
        st.markdown(f"{name}**  \n{desc}\n")

# Alerts
st.subheader("🚨 Alert System")
st.warning("RAIN DETECTED – Light rain starting in Field A")
st.error("HEAVY RAIN WARNING – Predicted in next 30 minutes")
st.success("SYSTEM UPDATE – Sensors calibrated successfully")

colA, colB = st.columns(2)
if colA.button("Configure Alerts"):
    st.info("⚙ Alert configuration panel would open here.")
if colB.button("Test Notifications"):
    st.success("✅ Test notification sent successfully!")

# Mobile App
st.subheader("📱 Mobile App Features")
st.write("📊 Real-time monitoring")
st.write("🔔 Push notifications")
st.write("📈 Historical data")
st.write("🗺 Multi-field support")
st.write("⚙ Customizable thresholds")
st.write("📞 SMS/Call backup")
if st.button("Download App"):
    st.info("📥 App download link would be here.")

# System Architecture
st.subheader("🏗 System Architecture")
st.write("🌦 Sensors → 🖥 Microcontroller → ☁ Cloud Server → 📱 User Devices")
st.write("- Real-time weather monitoring\n- Machine learning rain prediction\n- Multi-channel notifications\n- Solar-powered units\n- Cloud storage & analytics\n- Mobile & web dashboard access")