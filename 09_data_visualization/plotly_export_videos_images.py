
######################################## Export videos, gifs using Plotly and Kaleido ########################################
# This script demonstrates how to create animated plots using Plotly and export them as GIFs or MP4 videos.
# It uses the diamonds dataset from seaborn, creates scatter plots for different cuts of diamonds,
# and saves each frame as an image. Finally, it compiles these images into a GIF and an MP4 video using moviepy.

import plotly.express as px
import seaborn as sns
import os
from moviepy.editor import ImageSequenceClip

# Load the diamonds dataset
df = sns.load_dataset('diamonds')

# Check for missing values
if df.isnull().any().any():
    raise ValueError("The dataset contains missing values. Please handle them before plotting.")

# Create a directory to save frames
frames_dir = "./09_data_visualization/frames"
os.makedirs(frames_dir, exist_ok=True)

# Extract unique values for the 'cut' column to iterate over
unique_cuts = df['cut'].unique()

# Save each frame as an image
for i, cut in enumerate(unique_cuts):
    # Filter the data for the current cut
    filtered_df = df[df['cut'] == cut]
    
    # Ensure filtered data is valid
    if filtered_df.empty:
        continue

    # Create the scatter plot for the current cut
    frame_fig = px.scatter(
        filtered_df, x='carat', y='price',
        color='color',
        title=f'Diamond\'s Dataset - Carat vs Price for {cut} Cut',
        size='depth',
        hover_data=['clarity'],
        labels={'carat': 'Carat Weight', 'price': 'Diamond Price ($)'}
    )
    
    # Save the frame image using Kaleido
    frame_filename = os.path.join(frames_dir, f"frame_{i:03d}.png")
    frame_fig.write_image(frame_filename)

# Create a GIF or MP4 using moviepy
image_files = [os.path.join(frames_dir, f) for f in sorted(os.listdir(frames_dir)) if f.endswith('.png')]

clip = ImageSequenceClip(image_files, fps=2)  # Adjust fps as needed
clip.write_gif("./09_data_visualization/03_plotly/animated_plot.gif", fps=2)    # Save as GIF
# clip.write_videofile("./09_data_visualization/03_plotly/animated_plot.mp4", fps=1)  # Save as MP4
# # save HD video
# clip.write_videofile("./09_data_visualization/03_plotly/animated_plot_HD.mp4", fps=1, codec="libx264", preset="ultrafast", bitrate="3000k")

######################################## Export html, png, pdf and svg using Plotly and Kaleido ########################################
# import plotly.express as px
# import seaborn as sns

# # Load the diamonds dataset
# df = sns.load_dataset('diamonds')


# # sunburst chart
# fig = px.sunburst(df, path=['cut', 'clarity', 'color'], 
#                   values='price', 
#                   title='Sunburst Chart of Diamonds by Cut and Clarity',
#                 #   color='price',
#                 #   color_continuous_scale='Viridis',
#                   )
# # save html file
# fig.write_html('./09_data_visualization/03_plotly/sunburst_chart.html')

# # save png with high DPI
# import plotly.io as pio
# fig.write_image('./09_data_visualization/03_plotly/sunburst_chart.png', scale=2)

# # save plot as pdf file
# fig.write_image('./09_data_visualization/03_plotly/sunburst_chart.pdf')

# # save plot as svg file
# fig.write_image('./09_data_visualization/03_plotly/sunburst_chart.svg')

######################################## Export html, png, pdf and svg using Plotly and Kaleido ########################################
# import wbdata
# import pandas as pd
# import plotly.express as px
# import os
# from moviepy.editor import ImageSequenceClip

# # Define the indicator for population (SP.POP.TOTL) and GDP per capita (NY.GDP.PCAP.CD)
# indicator = {
#     'SP.POP.TOTL': 'total_population',
#     'NY.GDP.PCAP.CD': 'gdp_per_capita',
# }

# # Define countries
# # countries = ['IN', 'PK', 'BD', 'LK', 'AF']

# # Fetch data
# data = wbdata.get_dataframe(indicator, 
#                             # country=countries,
#                             )
# data.reset_index(inplace=True)
# data.rename(columns={'country': 'Country', 'date': 'Year'}, inplace=True)
# data['Year'] = pd.to_numeric(data['Year'])

# # Handle missing values
# # Replace missing gdp_per_capita and total_population with 0
# data['gdp_per_capita'] = data['gdp_per_capita'].fillna(0)
# data['total_population'] = data['total_population'].fillna(0)

# # Filter data for valid years
# df = data[(data['Year'] <= 2023) & (data['Year'] >= 1960)]
# df.sort_values(by='Year', inplace=True)

# # Check for missing or invalid data after filtering
# if df.isnull().values.any():
#     print("Data still contains missing values. Please check.")
#     print(df[df.isnull().any(axis=1)])  # Print rows with missing values

# # Directory to save frames
# frames_dir = "./09_data_visualization/frames_map"
# os.makedirs(frames_dir, exist_ok=True)

# # Save each frame as an image
# unique_years = df['Year'].unique()
# for i, year in enumerate(unique_years):
#     # Filter data for the current year
#     filtered_df = df[df['Year'] == year]
    
#     # Create the choropleth map for the current year
#     frame_fig = px.choropleth(
#         filtered_df,
#         locations="Country",
#         locationmode='country names',
#         color="gdp_per_capita",
#         hover_name="Country",
#         color_continuous_scale=px.colors.sequential.Viridis,
#         title=f"GDP Per Capita (Current US$) - {year}",
#         labels={'gdp_per_capita': 'GDP Per Capita'}
#     )
    
#     # Save the frame image using Kaleido
#     frame_filename = os.path.join(frames_dir, f"frame_{i:03d}.png")
#     frame_fig.write_image(frame_filename, engine="kaleido")

# # Create a GIF or MP4 using moviepy
# image_files = [os.path.join(frames_dir, f) for f in sorted(os.listdir(frames_dir)) if f.endswith('.png')]
# clip = ImageSequenceClip(image_files, fps=2)  # Adjust FPS for animation speed

# # Save as GIF
# clip.write_gif("./09_data_visualization/04_maps_animation/animated_map.gif", fps=2)

# # # Save as MP4
# # clip.write_videofile("./09_data_visualization/04_maps_animation/animated_map.mp4", fps=2)

# # # Save HD video
# # clip.write_videofile("./09_data_visualization/04_maps_animation/animated_map_HD.mp4", fps=2, codec="libx264", preset="ultrafast", bitrate="3000k")
