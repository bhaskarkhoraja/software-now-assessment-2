import pandas as pd
import os

def find_largest_temp_range_station():
    """
    Finds the station(s) with the largest temperature range across all available data.
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

    # Calculate max, min, and range for each station
    # We use .apply(pd.to_numeric, errors='coerce') to ensure data is numeric and handle NaNs
    all_data[month_columns] = all_data[month_columns].apply(
        pd.to_numeric, errors="coerce"
    )

    # Group by station and find the overall max and min for each station
    station_stats = all_data.groupby("STATION_NAME")[month_columns].agg(["max", "min"])

    # Flatten the multi-level column index
    station_stats.columns = [
        "_".join(col).strip() for col in station_stats.columns.values
    ]

    # Calculate the temperature range for each station
    station_stats["Temp_Max"] = station_stats[
        [col for col in station_stats.columns if "max" in col]
    ].max(axis=1)
    station_stats["Temp_Min"] = station_stats[
        [col for col in station_stats.columns if "min" in col]
    ].min(axis=1)
    station_stats["Temp_Range"] = station_stats["Temp_Max"] - station_stats["Temp_Min"]

    # Find the maximum temperature range
    max_range = station_stats["Temp_Range"].max()

    # Find all stations that have this maximum range
    stations_with_max_range = station_stats[
        station_stats["Temp_Range"] == max_range
    ].reset_index()

    # Save the results to a text file
    output_file = "largest_temp_range_station.txt"
    with open(output_file, "w") as f:
        print(
            f"The station(s) with the largest temperature range ({max_range:.1f}°C) are:"
        )
        for index, row in stations_with_max_range.iterrows():
            station_name = row["STATION_NAME"]
            temp_range = row["Temp_Range"]
            max_temp = row["Temp_Max"]
            min_temp = row["Temp_Min"]

            output_line = f"Station {station_name}: Range {temp_range:.1f}°C (Max: {max_temp:.1f}°C, Min: {min_temp:.1f}°C)"
            f.write(output_line + "\n")
            print(output_line)

    print(f"\nResults have been saved to '{output_file}'.")

if __name__ == "__main__":
    find_largest_temp_range_station()
