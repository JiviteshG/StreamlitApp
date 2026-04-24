# Streamlit Chat App

A Streamlit-based web application demonstrating interactive chat interfaces and efficient data caching strategies.

## 🚀 Overview
This repository serves as a foundation for building Streamlit applications with a focus on performance optimization. It showcases how to implement real-time chat components while utilizing advanced caching mechanisms to handle expensive computations and state persistence.

## 🛠 Key Features
* **Interactive Chat UI:** Built using Streamlit’s native chat elements for a fluid user experience.
* **Performance Optimization:** Includes implementations of `@st.cache_data` and `@st.cache_resource` to minimize latency during re-runs.
* **Modular Caching Logic:** Dedicated modules (`cache.py`, `cache2.py`) to test and compare different data persistence strategies.

## 📂 Project Structure
* `main.py`: The primary entry point for the Streamlit application.
* `cache.py` & `cache2.py`: Independent scripts demonstrating specific caching benchmarks and resource management.
* `.gitignore`: Pre-configured to keep the repository clean of `__pycache__` and environment files.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/JiviteshG/StreamlitApp.git](https://github.com/JiviteshG/StreamlitApp.git)
   cd StreamlitApp
   ```

2. **Set up a Virtual Environment (Recommended):**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. **Install Dependencies:**

  ```Bash
  pip install streamlit
  ```

🏃 Running the App
To launch the main application, use the following command:

  ```Bash
  streamlit run main.py
  ```
🧪 Testing Caching Logic
To explore the performance experiments included in this repo, you can run the cache demonstration files individually:
  ```Bash
  # To test data caching
  streamlit run cache.py
  ```

# To test resource/object caching
  ```Bash
  streamlit run cache2.py
  ```
