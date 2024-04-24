def recommend_clothing(weather, temperature):
    if weather == "sunny":
        if temperature >= 25:
            return "Wear shorts and a t-shirt."
        elif 20 <= temperature < 25:
            return "Wear shorts and a light shirt."
        else:
            return "Wear shorts and a light sweater."
    elif weather == "rainy":
        return "Wear a raincoat and waterproof shoes."
    elif weather == "snowy":
        if temperature <= 0:
            return "Wear a heavy jacket, gloves, and a hat."
        else:
            return "Wear a warm jacket and snow boots."
    else:
        return "Sorry, I can't provide a recommendation for this weather condition."

def main():
    weather = input("Enter the current weather condition (sunny, rainy, snowy): ").lower()
    temperature = float(input("Enter the current temperature in Celsius: "))
    
    recommendation = recommend_clothing(weather, temperature)
    print("Recommendation:", recommendation)

if __name__ == "__main__":
    main()
