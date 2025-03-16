import cv2
import os
import ollama
import re
import csv
import numpy as np

type_list = [
    'Cross Intersection', 'T-Intersection', 'Y-Intersection', 'Roundabout', 'Sharp Left Curve',
    'Sharp Right Curve', 'Reverse Curve', 'Winding Road', 'Steep Ascent', 'Steep Descent',
    'Narrow Road Both Sides', 'Narrow Right Side', 'Narrow Left Side', 'Narrow Bridge',
    'Two-Way Traffic', 'Pedestrian Crossing', 'Children Crossing', 'Livestock Crossing',
    'Traffic Signals Ahead', 'Falling Rocks', 'Cross Wind', 'Slippery Surface',
    'Mountainous Road', 'Embankment Road', 'Village Ahead', 'Tunnel Ahead', 'Ferry Crossing',
    'Hump Bridge', 'Uneven Road', 'Ford', 'Guarded Railway Crossing', 'Unguarded Railway Crossing',
    'Non-Motorized Vehicles', 'Accident Prone Area', 'Reduce Speed', 'Diversion Both Sides',
    'Diversion Left', 'Diversion Right', 'Construction Zone', 'General Danger', 'Railroad Crossing Symbol',
    'No Entry', 'No Vehicles', 'Motor Vehicles Prohibited', 'Trucks Prohibited',
    'Three-Wheeled Vehicles Prohibited', 'Buses Prohibited', 'Passenger Cars Prohibited',
    'Trailers Prohibited', 'Tractors Prohibited', 'Farm Vehicles Prohibited',
    'Motorcycles Prohibited', 'Two Vehicle Types Prohibited', 'Non-Motorized Vehicles Prohibited',
    'Animal-Drawn Vehicles Prohibited', 'Freight Tricycles Prohibited', 'Passenger Tricycles Prohibited',
    'Handcarts Prohibited', 'No Bicycles Downhill', 'No Bicycles Uphill', 'Pedestrians Prohibited',
    'No Left Turn', 'No Right Turn', 'No Straight Through', 'No Left or Right Turns',
    'No Straight or Left Turns', 'No Straight or Right Turns', 'No U-Turn', 'No Overtaking',
    'Overtaking Allowed', 'No Stopping or Parking', 'No Long-term Parking', 'No Horn',
    'Width Limit', 'Height Limit', 'Weight Limit', 'Axle Weight Limit', 'Speed Limit',
    'End Speed Limit', 'Stop for Inspection', 'Stop', 'Yield', 'Oncoming Vehicles Yield',
    'Dangerous Goods Vehicles Prohibited', 'Go Straight', 'Turn Left', 'Turn Right',
    'Straight or Left Turn', 'Straight or Right Turn', 'Left or Right Turn',
    'Keep Right', 'Keep Left', 'Interchange Straight/Left', 'Interchange Straight/Right',
    'Roundabout Direction', 'Pedestrians Only', 'Sound Horn', 'Minimum Speed Limit',
    'One Way (Left/Right)', 'One Way (Straight)', 'Priority Road', 'Oncoming Vehicles Priority',
    'Zebra Crossing', 'Right Turn Lane', 'Straight Lane', 'Straight/Right Turn Lane',
    'Lane Directions', 'Bus Lane', 'Motor Vehicles Only', 'Motor Vehicle Lane',
    'Non-Motorized Vehicles Only', 'Non-Motorized Lane', 'U-Turn Allowed', 'Entrance Advance Guide',
    'Entrance', 'Route Start', 'Route End Advance Notice', 'Route End Warning', 'Route End',
    'Next Exit', 'Exit Number Advance', 'Exit Advance Guide', 'Exit', 'Directional Arrows',
    'Destination Distance', 'Toll Plaza Advance', 'Toll Plaza', 'Emergency Phone',
    'Phone Location', 'Gas Station', 'Emergency Parking Area', 'Service Area Advance',
    'Tourist Direction', 'Tourist Distance', 'Information Center', 'Hiking Trail',
    'Cable Car', 'Campground', 'Campfire Area', 'Playground', 'Horseback Riding',
    'Fishing Area', 'Golf Course', 'Diving Area', 'Swimming Area', 'Boating Area',
    'Winter Recreation Area', 'Skiing Area', 'Skating Area', 'Construction Barrier',
    'Traffic Cone', 'Rail Crossing Post', 'Road Work Ahead', 'Road Closed',
    'Right Lane Closed', 'Left Lane Closed', 'Center Lane Closed', 'Slow Moving Vehicles',
    'Move Left', 'Move Right', 'Divert Left', 'Divert Right', 'Straight Auxiliary',
    'Stop', 'Stop Auxiliary', 'Wide Left Turn', 'Right Turn', 'Sharp Left Turn',
    'Left Turn Preparation', 'Violation Stop Order', 'Reduce Speed', 'Give Way to Following Vehicles',
    'Stop Signal', 'Proceed Straight Signal', 'Left Turn Signal', 'Left Turn Preparation Signal',
    'Right Turn Signal', 'Lane Change Signal', 'Reduce Speed Signal', 'Pull Over Signal',
    'Traffic Accident Diagram'
]


def analyze_image(image_path):
    prompt_str = f"""Please analyze the image and answer the following questions：

    1. Is there a {type_list}traffic sign in the image?:
    2. If yes, Please structure your response as follows.
    3.The Name, Description, and ConfidenceLevel information must be included!：


    Name:[I need you to name the traffic signs.],
    Description: [Your detailed description.],
    ConfidenceLevel: [0-100]
    """

    # 调用视觉模型
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': prompt_str,
            'images': [image_path]
        }]
    )
    raw_text = response['message']['content']
    return raw_text


print(analyze_image(r"img/test.png"))

