Crop and Fertilizer Recommendation System
A Django-based web app that helps users predict the best crops and fertilizers using machine learning (Random Forest) based on uploaded CSV data.
The application includes user authentication (login/registeration),prediction functionalities, and a products section


## Features
- **User Authentication:** Register and log in securely.
- **Crop prediction:** Recommends the most suitable crop for given input conditions using a trained ML model.
- **Fertilizer Prediction:** Suggests optimal fertilizers using predictive algorithms.
- **Product Management:** View, add, and manage products (seeds, fertilizers, etc.).
- **Machine Learning Integration:** Utilizes a Random Forest classifier trained on agricultural CSV data.

## Getting Started 

### 1. Clone the repository 
    git clone 
### 2. Create a Virtual Environment

    python -m venv venv
    source venv/bin/activate # On Windows : venv\Scriots\activate

### 3. Install Dependencies
    pip install  -r requirements.txt

### 4. Run Migrations
    python manage.py migrate

### 5. Run the Server
    python manage.py runserver

##Usage 

- Register or login via the main page
- Navigate to the **Predict** section for crop/fertilizer recommendations.
- View and manage available products.
- Access ML predictions that use a pre-trained Random Forest model and CSV data.

## Machine Learning Details

- **Algorithms:** Random Forest Classifier
- **Training Data:** CSV files with historical crop and fertilizer data
- **Workflow:** Input data (like soil, temperature, rainfall) -> Model -> Prediction output

## Directory Structure

├── <project_root>
│   ├── manage.py
│   ├── requirements.txt
│   ├── <app_name>/
│   ├── ML_model/
│   │   └── crop_model.pkl
│   │   └── fertilizer_model.pkl
│   └── templates/
│       └── ...


## Screenshots

_Add login, registration, and prediction feature screenshots here._

## Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork this repo
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -m "Add some feature"`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Open a pull request

---

Feel free to copy and paste this into your README.md file. Let me know if you want me to help with any other sections!


  
