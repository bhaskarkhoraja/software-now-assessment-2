import pandas as pd
import os

def analyze_temperature_data():
    """
    Analyzes temperature data from multiple weather stations across several years,
    calculating the average temperature for each Australian season.
    """
    all_data = pd.DataFrame()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(script_dir, "temperatures")

    if not os.path.exists(data_folder):
        print(f"Error: The '{data_folder}' folder was not found.")
        return

    # Process all CSV files in the 'temperatures' folder
    for file_name in os.listdir(data_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(data_folder, file_name)
            try:
                # Read each CSV file, ignoring the metadata columns for calculations
                df = pd.read_csv(file_path, index_col=False)
                # Ensure month columns are treated as numeric
                for month in [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December",
                ]:
                    df[month] = pd.to_numeric(df[month], errors="coerce")

                all_data = pd.concat([all_data, df], ignore_index=True)
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

    if all_data.empty:
        print("No valid data found to process.")
        return

    # Define Australian seasons based on months
    seasons = {
        "Summer": ["December", "January", "February"],
        "Autumn": ["March", "April", "May"],
        "Winter": ["June", "July", "August"],
        "Spring": ["September", "October", "November"],
    }

    # Calculate the average temperature for each season
    seasonal_averages = {}
    for season, months in seasons.items():
        # Select the relevant month columns, drop NaN values, then calculate the mean
        seasonal_temps = all_data[months].stack().mean()
        # Round the result to one decimal place for cleaner output
        seasonal_averages[season] = round(seasonal_temps, 1)

    # Save the seasonal averages to a text file
    output_file = os.path.join(script_dir, "average_temp.txt")
    with open(output_file, "w") as f:
        for season, avg_temp in seasonal_averages.items():
            line = f"{season}: {avg_temp}°C\n"
            f.write(line)
            print(line.strip())  # Also print to console for immediate feedback

    print(f"\nSeasonal average temperatures have been saved to '{output_file}'.")

if __name__ == "__main__":
    analyze_temperature_data()
