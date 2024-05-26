import random, requests

def download_streetview_images(latitude, longitude, num_images, first, radius):
    base_url = "https://maps.googleapis.com/maps/api/streetview"
    api_key = "API_KEY"
    size = "600x480"
    max_error = 30

    for i in range(num_images):
        # Calculate random location within +/- 3 km
        random_latitude = latitude + random.uniform(-radius, radius)
        random_longitude = longitude + random.uniform(-radius, radius)

        # Calculate random heading
        heading = random.uniform(0, 360)

        # Create the request URL
        location = f"{random_latitude},{random_longitude}"
        url = f"{base_url}?size={size}&location={location}&heading={heading}&radius={max_error}&key={api_key}"

        # Send request and save image
        response = requests.get(url)
        if response.status_code == 200:
            if first == -1:
                file_name = f"{random_latitude:.6f}_{random_longitude:.6f}.jpg"
            else:
                file_name = f"{i + first}_{random_latitude:.6f}_{random_longitude:.6f}.jpg"
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Saved image {i + 1} at {random_latitude:.6f}, {random_longitude:.6f}")
        else:
            print(f"Failed to retrieve image {i + 1}")


if __name__ == '__main__':
    download_streetview_images(-6.9091349, 107.6085346, 1000, -1, 0.06)
