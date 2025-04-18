# recommender.py
import pandas as pd

def recommend_crop(season, soil, rainfall, ph):
    try:
        df = pd.read_csv("data/crops.csv")

        # Filter the crops based on user inputs
        filtered = df[
            (df['Season'].str.lower() == season.lower()) &
            (df['Soil'].str.lower() == soil.lower()) &
            (df['Min_Rainfall'] <= rainfall) &
            (df['Max_Rainfall'] >= rainfall) &
            (df['Min_pH'] <= ph) &
            (df['Max_pH'] >= ph)
        ]

        # Return the list of matched crops
        return filtered['Crop'].tolist()

    except Exception as e:
        print(f"⚠️ Error in recommendation logic: {e}")
        return []
