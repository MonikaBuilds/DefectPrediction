# Defect Prediction System 

**Developer:** [Monika Bhati](https://github.com/MonikaBuilds)
**GitHub:** [MonikaBuilds](https://github.com/MonikaBuilds)

## Project Overview

The Defect Prediction system is a **Machine Learning-powered Flask web application** designed to predict defect-prone software modules. It analyzes standard code metrics to classify modules as either *defect-prone* or *not defect-prone*.

This project provides an interactive and user-friendly interface for both manual input and efficient batch processing using CSV files.

---

##  Key Features

* **Prediction Model:** Predicts defect-proneness based on key code metrics:
    * **Lines of Code (LOC)**
    * **Cyclomatic Complexity**
    * **Halstead Volume**
* **Web Interface:** Interactive frontend built with **HTML, CSS, and Flask**.
* **Batch Prediction:** Supports uploading **CSV files** (e.g., `kc1.csv`) for making predictions on multiple modules at once.
* **Code Quality Ready:** Project structure includes configuration for **SonarQube** analysis.

---

## 🛠️ Technologies Used

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend/Core** | Python 3 | Core programming language |
| **Web Framework** | Flask | Building the web application and routing |
| **Machine Learning** | scikit-learn | Model training and prediction |
| **Frontend** | HTML, CSS | Interactive user interface |
| **Database (Optional)**| MySQL | Potential for user data or logging (future work) |
| **Code Quality** | SonarScanner | Static code analysis |

---

##  Installation

Follow these steps to get the project running locally.

### 1. Clone the Repository

```bash
git clone [https://github.com/MonikaBuilds/DefectPrediction.git](https://github.com/MonikaBuilds/DefectPrediction.git)
```
```bash
cd DefectPrediction
```

### 2. Create and Activate Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.
# Create the virtual environment
```bash
python -m venv .venv
```

Activate the environment:

On Windows:
```bash
.venv\Scripts\activate
```

On macOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app/app.py
```

(Note: If the entry point is different, replace app/app.py with the correct file, e.g., flask run if configured)

The application will typically be accessible at http://127.0.0.1:5000/.

### Usage
Manual Input
Navigate to the web application in your browser.

Enter the values for Lines of Code (LOC), Cyclomatic Complexity, and Halstead Volume into the input form.

Click the "Predict Defect" button.

View the prediction result displayed on the page.

Batch Prediction (CSV Input)
Prepare your data in a CSV file (e.g., kc1.csv) with columns corresponding to the required code metrics.

Look for the CSV upload section on the web interface.

Upload your file and initiate the batch prediction.

The results will be displayed or available for download.

### Future Enhancements
Real-Time Scanning: Implement real-time code scanning capabilities.

CI/CD Integration: Integrate the system with CI/CD pipelines for automatic quality gate checks.

Interactive Dashboards: Develop dashboards for visualizing prediction statistics and trends.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

<img width="1204" height="733" alt="image" src="https://github.com/user-attachments/assets/57a5fc6d-3e81-4ba8-8709-909a456257c6" />
<img width="1026" height="689" alt="image" src="https://github.com/user-attachments/assets/736e1702-0b3d-45c5-994e-57a08e6382b0" />


