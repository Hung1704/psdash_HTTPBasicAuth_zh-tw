import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import sys 





# 獲取命令列參數
if len(sys.argv) != 2:
    print("Usage: python plot.py <Duration>")
    print("python3 plot.py '30days'")
    sys.exit(1)

start_duration = pd.Timedelta(sys.argv[1])

# 計算範圍的時間戳記
current_time = datetime.now()
start_time = current_time - start_duration

# Create an empty DataFrame to store all data
all_data = pd.DataFrame()
# Specify the directory where .csv files are located
data_directory = 'data/'  # Replace with your actual directory path
# Iterate through all .csv files in the directory
for filename in os.listdir(data_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(data_directory, filename)
        
        # Extract date and time information from the filename
        file_time_str = filename.split(".csv")[0]
        file_time = datetime.strptime(file_time_str, "%Y-%m-%d--%H-%M-%S")
        # Check if the file_time is within the specified time range
        if start_time <= file_time:
            # Read the .csv file
            data = pd.read_csv(file_path)
            
            # Add the date and time information from the filename to the DataFrame
            data["Time"] = file_time
            
            # Concatenate the data to the all_data DataFrame
            all_data = pd.concat([all_data, data], ignore_index=True)

# Sort the DataFrame by time
all_data.sort_values(by="Time", inplace=True)

# Perform statistics on user activity
grouped_data = all_data.groupby(["Time", "Course/Lab"]).size().unstack(fill_value=0)




# import mplcyberpunk
# import matplotlib.pyplot as plt
# # 使用赛博朋克风样式
# plt.style.use('cyberpunk')

# PLOT_COLORS=["#00BB00","#AE00AE","#408080","#EA0000","#2828FF","#FFD306","#F75000","#A23400","#3C3C3C"]
# Set plot style
plt.style.use("seaborn-paper")



# Prepare data for stackplot
time_points = grouped_data.index
stacked_data = [grouped_data[course_lab] for course_lab in grouped_data.columns]

# Calculate the total number of users across all servers for each time point
total_users = grouped_data.sum(axis=1)

# Plot the line chart
plt.figure(figsize=(11, 6))


# Plot individual course/lab lines
for course_lab in grouped_data.columns:
    plt.plot_date(grouped_data.index, grouped_data[course_lab], '-', label=course_lab, linewidth=3)
    #plt.plot_date(grouped_data.index, grouped_data[course_lab], '-', label=course_lab, marker='o')

#plt.plot_date(grouped_data.index, total_users, '-', label="Total Users", color="gray", marker='o')
plt.plot_date(grouped_data.index, total_users, '-', label="Total Users", color="forestgreen", linewidth=3)

# 將主要y軸和次要y軸上的圖例結合
# lines, labels = plt.get_legend_handles_labels()
# lines2, labels2 = plt2.get_legend_handles_labels()
# plt2.legend(lines + lines2, labels + labels2, loc="upper left")

plt.xlabel("Time", fontsize=16, fontweight="bold")
plt.ylabel("Number of Users", fontsize=16, fontweight="bold")
# plt.title("User Activity Over "+sys.argv[1], fontsize=24, fontweight="bold")
plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1), fontsize=12)
plt.grid(True, linestyle='--', linewidth=1,alpha=0.3)
plt.xticks(rotation=45)

# # Create a secondary y-axis for "Total Users"
# plt2 = plt.twinx()

# # Plot the gray line for the total number of users on the secondary y-axis
# plt2.plot_date(grouped_data.index, total_users, '-', label="Total Users", color="gray", marker='o')
# plt2.set_ylabel("Total Users")  # 設置次要y軸的標籤
# plt2.grid(False)  # 關閉次要y軸的網格


plt.tight_layout()
plt.savefig('users-web.png', dpi=300, bbox_inches='tight')
# mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.5, gradient_start='zero')

import mpld3
# Save the Matplotlib figure as an interactive HTML using mpld3
html_fig = mpld3.fig_to_html(plt.gcf())
# Save the HTML to a file
with open("users-web.html", "w") as html_file:
    html_file.write(html_fig)
# plt.show()
