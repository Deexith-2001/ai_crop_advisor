# main.py
from recommender import recommend_crop

def main():
    print("🌾 Welcome to AI Crop Advisor 🌾\n")

    try:
        season = input("Enter season (Kharif/Rabi/Zaid): ").strip()
        soil = input("Enter soil type (Loamy/Clay/Sandy): ").strip()
        rainfall = float(input("Enter average rainfall (in mm): "))
        ph = float(input("Enter soil pH level (e.g., 6.5): "))

        result = recommend_crop(season, soil, rainfall, ph)

        if result:
            print("\n✅ Recommended Crops for Your Conditions:")
            for crop in result:
                print(f"• {crop}")
        else:
            print("\n❌ No suitable crops found for these conditions.")
    except ValueError:
        print("\n⚠️ Invalid input! Please enter numbers for rainfall and pH.")

if __name__ == "__main__":
    main()
