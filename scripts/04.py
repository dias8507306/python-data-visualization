"""
Uber Data Analysis - Working Version
This will work without CSV file and encoding issues
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('default')
sns.set_style("whitegrid")

print("=" * 50)
print("UBER DATA ANALYSIS STARTING...")
print("=" * 50)

# Create sample data
print("Creating sample data...")
np.random.seed(42)

# Generate 1000 sample rides
n_samples = 1000

# Create sample dataframe
data = {
    'Date': pd.date_range('2024-01-01', periods=n_samples).date,
    'Time': [f"{np.random.randint(0, 23):02d}:{np.random.randint(0, 59):02d}" for _ in range(n_samples)],
    'Vehicle_Type': np.random.choice(['UberX', 'UberBlack', 'UberXL', 'Pool'], n_samples, 
                                     p=[0.5, 0.2, 0.2, 0.1]),
    'Booking_Status': np.random.choice(['Completed', 'Cancelled by User', 'No Driver Found'], 
                                       n_samples, p=[0.85, 0.1, 0.05]),
    'Booking_Value': np.random.exponential(50, n_samples).round(2),
    'Ride_Distance': np.random.gamma(shape=2, scale=5, size=n_samples).round(1),
}

df = pd.DataFrame(data)
print(f"Sample data created with {len(df)} records")

# Add datetime column
df['DateTime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'])
df['Hour'] = df['DateTime'].dt.hour
df['DayOfWeek'] = df['DateTime'].dt.day_name()
df['Month'] = df['DateTime'].dt.month
df['Is_Successful'] = (df['Booking_Status'] == 'Completed').astype(int)

print("Data prepared successfully!")

# ====================== CREATE 12 GRAPHS ======================

print("\n" + "="*50)
print("CREATING 12 ANALYSIS GRAPHS")
print("="*50)

# 1. Missing Data Analysis
print("1. Missing Data Analysis...")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_to_show = missing_pct[missing_pct > 0]

plt.figure(figsize=(10, 5))
if len(missing_to_show) > 0:
    missing_to_show.plot(kind='bar', color='lightcoral')
else:
    plt.text(0.5, 0.5, 'No Missing Data!', ha='center', va='center', fontsize=14)
plt.title('Missing Data Percentage by Column')
plt.xlabel('Columns')
plt.ylabel('Missing Percentage (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("1_missing_data.png", dpi=300, bbox_inches='tight')
plt.show()

# 2. Booking Status Distribution
print("2. Booking Status Distribution...")
plt.figure(figsize=(10, 5))
status_counts = df['Booking_Status'].value_counts()
status_counts.plot(kind='bar', color=['green', 'red', 'orange'])
plt.title('Booking Status Distribution')
plt.xlabel('Status')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("2_booking_status.png", dpi=300, bbox_inches='tight')
plt.show()

# 3. Success Rate by Vehicle Type
print("3. Success Rate by Vehicle Type...")
vehicle_success = df.groupby('Vehicle_Type')['Is_Successful'].agg(['mean', 'count'])
vehicle_success['mean_pct'] = vehicle_success['mean'] * 100

plt.figure(figsize=(10, 5))
vehicle_success['mean_pct'].sort_values().plot(kind='bar', color='skyblue')
plt.title('Success Rate by Vehicle Type (%)')
plt.xlabel('Vehicle Type')
plt.ylabel('Success Rate (%)')
plt.tight_layout()
plt.savefig("3_vehicle_success.png", dpi=300, bbox_inches='tight')
plt.show()

# 4. Success Rate by Hour
print("4. Success Rate by Hour...")
hour_success = df.groupby('Hour')['Is_Successful'].mean() * 100

plt.figure(figsize=(12, 5))
hour_success.plot(kind='bar', color='lightgreen')
plt.title('Success Rate by Hour of Day')
plt.xlabel('Hour (0-23)')
plt.ylabel('Success Rate (%)')
plt.xticks(range(0, 24, 2))
plt.tight_layout()
plt.savefig("4_hour_success.png", dpi=300, bbox_inches='tight')
plt.show()

# 5. Success Rate by Day of Week
print("5. Success Rate by Day of Week...")
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['DayOfWeek'] = pd.Categorical(df['DayOfWeek'], categories=day_order, ordered=True)
day_success = df.groupby('DayOfWeek', observed=True)['Is_Successful'].mean() * 100

plt.figure(figsize=(10, 5))
day_success.plot(kind='bar', color='violet')
plt.title('Success Rate by Day of Week')
plt.xlabel('Day')
plt.ylabel('Success Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("5_day_success.png", dpi=300, bbox_inches='tight')
plt.show()

# 6. Revenue Distribution for Successful Rides
print("6. Revenue Distribution...")
successful = df[df['Is_Successful'] == 1]

plt.figure(figsize=(10, 5))
plt.hist(successful['Booking_Value'], bins=30, color='gold', edgecolor='black', alpha=0.7)
plt.title('Revenue Distribution (Successful Rides)')
plt.xlabel('Revenue')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("6_revenue_distribution.png", dpi=300, bbox_inches='tight')
plt.show()

# 7. Revenue vs Distance Scatter Plot
print("7. Revenue vs Distance...")
plt.figure(figsize=(10, 5))
plt.scatter(successful['Ride_Distance'], successful['Booking_Value'], 
            alpha=0.6, s=30, color='blue')
plt.title('Revenue vs Ride Distance')
plt.xlabel('Distance (km)')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig("7_revenue_vs_distance.png", dpi=300, bbox_inches='tight')
plt.show()

# 8. Revenue Share by Vehicle Type
print("8. Revenue Share by Vehicle Type...")
vehicle_revenue = successful.groupby('Vehicle_Type')['Booking_Value'].agg(['sum', 'mean'])
vehicle_revenue['share_pct'] = (vehicle_revenue['sum'] / vehicle_revenue['sum'].sum()) * 100

plt.figure(figsize=(10, 5))
vehicle_revenue['share_pct'].sort_values().plot(kind='barh', color='lightblue')
plt.title('Revenue Share by Vehicle Type (%)')
plt.xlabel('Revenue Share (%)')
plt.ylabel('Vehicle Type')
plt.tight_layout()
plt.savefig("8_revenue_share.png", dpi=300, bbox_inches='tight')
plt.show()

# 9. Daily Ride Volume
print("9. Daily Ride Volume...")
daily_rides = df.groupby('Date').size()

plt.figure(figsize=(12, 5))
daily_rides.plot(color='red', linewidth=1.5)
plt.title('Daily Ride Volume')
plt.xlabel('Date')
plt.ylabel('Number of Rides')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("9_daily_rides.png", dpi=300, bbox_inches='tight')
plt.show()

# 10. Heatmap: Hour × Day Success Rate
print("10. Heatmap: Hour vs Day...")
heatmap_data = pd.pivot_table(df, index='DayOfWeek', columns='Hour', 
                              values='Is_Successful', aggfunc='mean')

plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap='YlOrRd')
plt.title('Success Rate Heatmap: Day vs Hour')
plt.xlabel('Hour')
plt.ylabel('Day')
plt.tight_layout()
plt.savefig("10_heatmap.png", dpi=300, bbox_inches='tight')
plt.show()

# 11. Box Plot: Revenue by Vehicle Type
print("11. Revenue by Vehicle Type (Box Plot)...")
plt.figure(figsize=(10, 5))
sns.boxplot(data=successful, x='Vehicle_Type', y='Booking_Value')
plt.title('Revenue Distribution by Vehicle Type')
plt.xlabel('Vehicle Type')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("11_revenue_boxplot.png", dpi=300, bbox_inches='tight')
plt.show()

# 12. Monthly Trend
print("12. Monthly Trend...")
monthly_success = df.groupby('Month')['Is_Successful'].mean() * 100

plt.figure(figsize=(10, 5))
monthly_success.plot(kind='line', marker='o', linewidth=2, markersize=8, color='purple')
plt.title('Monthly Success Rate Trend')
plt.xlabel('Month')
plt.ylabel('Success Rate (%)')
plt.xticks(range(1, 13))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("12_monthly_trend.png", dpi=300, bbox_inches='tight')
plt.show()

# ====================== SUMMARY ======================
print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("="*60)

print(f"""
RESULTS SUMMARY:
----------------
Total Rides: {len(df):,}
Successful Rides: {successful.shape[0]:,} ({successful.shape[0]/len(df)*100:.1f}%)
Failed Rides: {len(df) - successful.shape[0]:,}

Revenue Statistics:
• Total Revenue: ${successful['Booking_Value'].sum():,.2f}
• Average Revenue per Ride: ${successful['Booking_Value'].mean():.2f}
• Average Distance: {successful['Ride_Distance'].mean():.1f} km

Best Performance:
• Best Vehicle: {vehicle_success['mean_pct'].idxmax()} ({vehicle_success['mean_pct'].max():.1f}%)
• Best Hour: {hour_success.idxmax()}:00 ({hour_success.max():.1f}%)
• Best Day: {day_success.idxmax()} ({day_success.max():.1f}%)

Files Created:
---------------
12 PNG files have been saved in your current directory:
1. 1_missing_data.png
2. 2_booking_status.png
3. 3_vehicle_success.png
4. 4_hour_success.png
5. 5_day_success.png
6. 6_revenue_distribution.png
7. 7_revenue_vs_distance.png
8. 8_revenue_share.png
9. 9_daily_rides.png
10. 10_heatmap.png
11. 11_revenue_boxplot.png
12. 12_monthly_trend.png

All done! Check your folder for the graph files.
""")