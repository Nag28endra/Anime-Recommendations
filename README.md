# 🎌 Anime Recommendations

> A smart recommendation system for anime enthusiasts, helping you discover your next favorite show.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Data](https://img.shields.io/badge/Data-CSV-orange.svg)](data/anime_data.csv)

## 📋 Overview

This project provides an intelligent anime recommendation engine that analyzes anime data and suggests personalized recommendations based on user preferences and viewing history. Perfect for anime fans looking to expand their watchlist!

## ✨ Features

- 📊 **Data Analysis** - Comprehensive anime dataset analysis and exploration
- 🎯 **Smart Recommendations** - Algorithm-based anime suggestions
- 📈 **Data Visualization** - Interactive notebooks for data exploration
- 🔄 **Easy Data Updates** - Automated data pull scripts
- 📦 **Modular Design** - Clean, maintainable codebase

## 🛠️ Prerequisites

- Python 3.8 or higher
- pip package manager

## 📥 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/Anime-Recommendations.git
   cd Anime-Recommendations
   ```

2. **Set up a virtual environment**
   ```bash
   # Using Python venv
   python -m venv anime
   
   # Activate the virtual environment
   # On Windows:
   anime\Scripts\activate
   # On macOS/Linux:
   source anime/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Run Data Pull Script
```bash
python src/pull-data.py
```
This will fetch the latest anime data and update the local dataset.

### Explore Data with Jupyter
```bash
jupyter notebook notebooks/
```
Then open either:
- **pull-data.ipynb** - Data collection and preprocessing
- **test-data.ipynb** - Data analysis and exploration

## 📁 Project Structure

```
Anime-Recommendations/
├── src/
│   └── pull-data.py           # Data collection script
├── notebooks/
│   ├── pull-data.ipynb        # Data pulling notebook
│   └── test-data.ipynb        # Data exploration notebook
├── data/
│   └── anime_data.csv         # Anime dataset
├── anime/                      # Virtual environment
├── requirements.txt           # Project dependencies
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## 💻 Technologies & Libraries

- **Data Processing**: Pandas, NumPy, Openpyxl
- **Web Requests**: Requests, aiohttp
- **Utilities**: Python-dotenv, python-dateutil
- **Notebooks**: Jupyter
- **Time Zones**: pytz, tzdata

## 📝 Data Format

The anime dataset (`data/anime_data.csv`) contains comprehensive information about various anime titles including:
- Title and alternative names
- Genres and themes
- Rating and popularity scores
- Episode count and status
- And more...

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub or reach out to the maintainers.

---

**Happy anime watching!** 🎬
