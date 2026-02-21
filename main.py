Creating a smart energy consumption tracker involves several components, including data collection, data analysis, and actionable insights to reduce wastage and costs. Below is a Python program that simulates such a system. The goal here is to provide a simplified version that includes data simulation, analysis, and basic recommendations.

For a real-world implementation, you would need actual data from energy usage sensors or API integrations with smart meters.

```python
import random
import datetime
import statistics

class EcoEnergy:
    def __init__(self):
        # Simulated energy usage data: list of tuples (datetime, consumption in kWh)
        self.energy_data = []
        
    def simulate_data(self, days=30):
        """Simulate energy consumption data for the given number of days."""
        current_time = datetime.datetime.now()
        for day in range(days):
            for hour in range(24):
                time = current_time - datetime.timedelta(days=days-day, hours=hour)
                consumption = random.uniform(0.1, 5.0)  # kWh usage per hour, random example
                self.energy_data.append((time, consumption))
        self.energy_data.sort()  # Sort by time
    
    def analyze_data(self):
        """Analyze energy consumption data and return insights."""
        try:
            if not self.energy_data:
                raise ValueError("No energy data to analyze.")
            
            # Analyze daily consumptions
            daily_consumption = {}
            for entry in self.energy_data:
                date = entry[0].date()
                daily_consumption[date] = daily_consumption.get(date, 0) + entry[1]
            
            # Average daily consumption
            daily_values = list(daily_consumption.values())
            avg_daily_consumption = statistics.mean(daily_values)
            peak_consumption = max(daily_values)
            off_peak_consumption = min(daily_values)
            
            return {
                'average_daily_usage': avg_daily_consumption,
                'peak_usage': peak_consumption,
                'off_peak_usage': off_peak_consumption
            }
        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    
    def provide_recommendations(self, analysis_result):
        """Provide recommendations to optimize energy usage."""
        if not analysis_result:
            print("No analysis results to base recommendations on.")
            return
        
        avg = analysis_result['average_daily_usage']
        peak = analysis_result['peak_usage']
        off_peak = analysis_result['off_peak_usage']
        
        print("\nEnergy Consumption Recommendations:")
        print(f"Average daily usage: {avg:.2f} kWh")
        if avg > 3.0:
            print("- Consider reducing your average daily consumption. Look into energy-efficient appliances.")
        if peak - avg > 1.5:
            print("- Try to identify any spikes in your energy usage. Avoid using high-energy appliances during peak hours.")
        if off_peak < 1.0:
            print("- Good job on maintaining a low off-peak energy usage! Continue optimizing to save on energy bills.")

def main():
    eco_energy = EcoEnergy()
    eco_energy.simulate_data(days=30)  # Simulate data for the past 30 days
    analysis_result = eco_energy.analyze_data()  # Analyze the simulated data
    eco_energy.provide_recommendations(analysis_result)  # Provide recommendations to optimize usage

if __name__ == "__main__":
    main()
```

### Program Explanation
- **Data Simulation**: The `simulate_data` function generates random energy consumption data for each hour over a specified number of days.
- **Analysis**: The `analyze_data` function computes daily energy consumption, average daily usage, peak, and off-peak consumption.
- **Recommendations**: Based on the analysis, `provide_recommendations` suggests actions to reduce energy consumption.

### Error Handling
- The program checks for the presence of data before performing analysis.
- It captures and displays errors if anything goes wrong during data analysis.

This simple version of an eco-energy tracker primarily focuses on demonstrating concepts. For realistic implementations, data would usually be pulled from smart meters or home automation systems, and more sophisticated analysis would be performed using machine learning.