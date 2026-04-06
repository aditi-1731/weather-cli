# 🌦️ Weather CLI

CLI-based Python tool to fetch real-time weather data using OpenWeather API with secure API key handling.

## 🚀 Features

* 🔍 Get weather by city name
* 🌡️ Temperature in Celsius
* ☁️ Weather condition
* 💧 Humidity
* 🌬️ Wind speed
* 🔐 Secure API key using `.env`

## 🛠️ Built With

* Python
* requests
* python-dotenv
* CLI (sys.argv)

## ⚙️ Installation

```bash
git clone https://github.com/aditi-1731/weather-cli.git
cd weather-cli
pip install -r requirements.txt
```

## 🔑 Setup API Key

Create a `.env` file in the project root:

```
API_KEY=your_api_key_here
```

## ▶️ Usage

```bash
python weather.py <city>
```

### Example

```bash
python weather.py Delhi
```

## 📌 Sample Output

Weather in Delhi:
----------------------------------------
🌡️ Temperature : 30°C  
☁️ Condition   : clear sky  
💧 Humidity    : 60%  
🌬️ Wind Speed  : 3.5 m/s  

## 📌 Notes

* Uses OpenWeather API
* Requires internet connection
* API key may take a few minutes to activate

## 🔮 Future Improvements

* Add unit selection (Celsius/Fahrenheit)
* Save results to file
* Add multiple city support
* Convert into GUI/Web app

## 👩‍💻 Author

**Aditi Tripathi**
