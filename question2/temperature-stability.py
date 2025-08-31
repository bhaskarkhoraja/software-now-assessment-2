import pandas as pd
import os

def analyze_temperature_stability():
    """
    Analyzes temperature data to find the most stable and most variable stations
    based on the standard deviation of their temperature readings.
    """
    all_data = pd.DataFrame()
    data_folder = "temperatures"

    if not os.path.exists(data_folder):
        print(f"Error: The '{data_folder}' folder was not found.")
        return

    # Process all CSV files in the 'temperatures' folder
    for file_name in os.listdir(data_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(data_folder, file_name)
            try:
                # Read each CSV file
                df = pd.read_csv(file_path, index_col=False)
                all_data = pd.concat([all_data, df], ignore_index=True)
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

    if all_data.empty:
        print("No valid data found to process.")
        return

    # Columns containing temperature data
    month_columns = [
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
    ]

    # Convert month columns to numeric, coercing errors to NaN
    all_data[month_columns] = all_data[month_columns].apply(
        pd.to_numeric, errors="coerce"
    )

    # Calculate the standard deviation for each station across all months and years
    # 📝 Corrected section: stack the monthly temperature columns first to create a single series
    # of temperatures for each station, then group by the station name to calculate the standard deviation.
    # The original code attempted to call .stack() on a groupby object, which is incorrect.
    stacked_temperatures = all_data.set_index("STATION_NAME")[month_columns].stack()
    station_stdev = stacked_temperatures.groupby(level="STATION_NAME").std().to_frame("StdDev")


    # Find the station with the smallest standard deviation (most stable)
    most_stable_std = station_stdev["StdDev"].min()
    most_stable_stations = station_stdev[
        station_stdev["StdDev"] == most_stable_std
    ].reset_index()

    # Find the station with the largest standard deviation (most variable)
    most_variable_std = station_stdev["StdDev"].max()
    most_variable_stations = station_stdev[
        station_stdev["StdDev"] == most_variable_std
    ].reset_index()

    # Save the results to a text file
    output_file = "temperature_stability_stations.txt"
    with open(output_file, "w") as f:
        f.write("Most Stable:\n")
        print("Most Stable:")
        for index, row in most_stable_stations.iterrows():
            station_name = row["STATION_NAME"]
            std_dev = row["StdDev"]
            output_line = f"Station {station_name}: StdDev {std_dev:.1f}°C"
            f.write(output_line + "\n")
            print(output_line)

        f.write("\nMost Variable:\n")
        print("\nMost Variable:")
        for index, row in most_variable_stations.iterrows():
            station_name = row["STATION_NAME"]
            std_dev = row["StdDev"]
            output_line = f"Station {station_name}: StdDev {std_dev:.1f}°C"
            f.write(output_line + "\n")
            print(output_line)

    print(f"\nTemperature stability analysis has been saved to '{output_file}'.")


if __name__ == "__main__":
    analyze_temperature_stability()
