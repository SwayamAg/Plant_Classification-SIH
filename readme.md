
# 🌿 Plant Species Classifier (Streamlit)

An interactive Streamlit app that identifies plant species from images using a TensorFlow/Keras CNN. The model classifies images into 24 categories. The deployed model is ~300MB (`plant_species_Model_kaggle.h5`).

## 🌱 Supported Plant Types

The model can identify the following 24 plant types (derived from `Data/`):
- **Amla**
- **Arali**
- **Ashoka**
- **Ashwagandha**
- **Avacado**
- **Bamboo**
- **Basale**
- **Castor**
- **Corn**
- **Curry_Leaf**
- **Doddapatre**
- **Ganike**
- **Guava**
- **Henna**
- **Mint**
- **Nooni**
- **Pappaya**
- **Rose**
- **Wood_sorel**
- **aloevera**
- **banana**
- **mango**
- **orange**
- **watermelon**


## ✨ Features
- **Streamlit interactive UI** for image upload and prediction
- **Real-time image classification** with confidence scores
- **Automatic model download** if not present
- **Easy local or cloud deployment**


## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- See `requirements.txt` for dependencies

### Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/SwayamAg/Plant-Identification
   cd Plant_Classifier_SIH
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Ensure the model file is present**
   - The app downloads `plant_species_Model_kaggle.h5` (~300MB) from Google Drive on first run
   - Or, place `plant_species_Model_kaggle.h5` in the project root manually

### Running the Streamlit App
```bash
streamlit run app.py
# or
streamlit run streamlit_app.py
```


## �️ Usage

1. Open the app in your browser (Streamlit will provide a local URL)
2. Upload a plant image (JPG/PNG)
3. View the predicted species and confidence score


## 🚀 Deployment

You can deploy this Streamlit app on platforms like Streamlit Community Cloud, Hugging Face Spaces, or any cloud VM that supports Python.

**To deploy on Streamlit Cloud:**
1. Push your code to GitHub
2. Go to https://streamlit.io/cloud and connect your repo
3. Set the main file to `app.py` or `streamlit_app.py`
4. The app will auto-install from `requirements.txt` and run


## 📁 Project Structure

```
Plant_Classifier_SIH/
├── app.py                  # Streamlit app (main)
├── streamlit_app.py        # (Optional) Streamlit app (alternate)
├── plant_species_Model_kaggle.h5  # Trained model
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
├── readme.md               # Project documentation
├── plant-cnn-model_kaggle.ipynb  # Notebook (training/experiments)
├── .kaggle/                # (Optional) Kaggle API config
```


## 🔧 Model Information

- **Architecture**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow/Keras
- **Input Size**: 224x224 pixels
- **Classes**: 24 plant types
- **Model Size**: ~300MB
- **Training**: Custom dataset with train/validation/test splits


## 🛠️ Development

### Adding New Plant Types

1. Add a new class folder under `Data/`
2. Retrain the model with the updated dataset
3. Deploy the updated model file (`plant_species_Model_kaggle.h5`)

### Model Training

The training process is documented in `Plant_Classification_train.ipynb`. To retrain:

1. Prepare your dataset in the `train/`, `val/`, and `test/` directories
2. Run the Jupyter notebook
3. Replace `plant_species_Model_kaggle.h5` with the new model


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request


## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.


## 🙏 Acknowledgments

- TensorFlow team for the deep learning framework

- The plant dataset contributors

## 📞 Support


For issues and questions:
- Create an issue in the repository
- Use the Streamlit Community forums for deployment help

---

## 👨‍💻 Made by Swayam

- **LinkedIn**: [Swayam Agarwal](https://www.linkedin.com/in/swayam-agarwal/)
- **GitHub**: [SwayamAg](https://github.com/SwayamAg)

---

**Note**: The app auto-downloads `plant_species_Model_kaggle.h5` on first run; you can also place the ~300MB model in the project root manually.
