# GeoSearchApp

![GeoSearchApp Screenshot](https://github.com/user-attachments/assets/e92d51d5-10c7-4b98-b288-3129b1d71ba8)

Feel free to visit the live Web App at [https://locatenow.org](https://locatenow.org)

---

## Web App Summary: Interactive Address & Places Map

**GeoSearchApp** provides an interactive map interface that allows users to search for addresses, drop pins manually, view nearby places, and get detailed information about locations. Below are the core functionalities:

### Core Functionalities

#### 1. **Interactive Map Display**
- The app integrates a **Google Map** that is interactive and responsive. Users can zoom, pan, and click to drop pins on the map.

#### 2. **Address Search with Autocomplete**
- Users can search for locations by typing an address into the input field with **Google Maps Places Autocomplete**. 
- As users type, relevant address suggestions appear. Selecting a suggestion centers the map on the location and drops a pin.

#### 3. **Manual Pin Drop**
- Users can click anywhere on the map to manually drop a pin.
- The app geocodes the clicked location, fetches its address, and displays the address both in the input field and in an **info window** on the map.

#### 4. **Nearby Places Search**
- After a pin is dropped (either manually or via address search), the app can search for **nearby places** based on the selected location.
- Users can filter places by **category** (e.g., Restaurants, Gyms, Movie Theaters, Shopping Malls) and **radius** (e.g., 5KM, 10KM, etc.).
- Nearby places are displayed as markers on the map.

#### 5. **Info Window with Location Details**
- When a pin is dropped, an **info window** displays location details, including:
  - The address
  - Name of the place
  - Rating and reviews
  - **Street View** image, if available

#### 6. **Locate Me Button**
- A **"Locate Me" button** uses the browser’s geolocation feature to center the map on the user's current location and drop a pin there, allowing users to easily find their position on the map.

#### 7. **Responsive Design**
- The app is designed to be **responsive**, adjusting its layout for different screen sizes (e.g., mobile devices). 
- The map and controls (search bar, dropdowns, locate button) automatically adjust for smaller screen sizes to ensure an optimal user experience.

#### 8. **User Interaction and Accessibility**
- Users can interact with the map by clicking to drop pins, searching for places, and navigating between locations.
- The app includes **accessibility features** such as focus and hover effects on controls to enhance usability for all users.

---

These core functionalities work together to provide a seamless experience for users to search, explore, and get detailed information about locations in a visually appealing and easy-to-use interface.

---

## Quick Use Guide: Interactive Address & Places Map

This guide will help you get started with using the **Interactive Address & Places Map** web app. The app allows users to search for addresses, drop pins, explore nearby places, and view location details.

### 1. **Searching for an Address**
- **Step 1**: Type an address into the search bar at the top of the page.
- **Step 2**: As you type, **autocomplete suggestions** will appear. Select the correct address from the list.
- **Step 3**: The map will automatically center on the selected location, and a pin will be dropped at that address.
- **Step 4**: The **info window** will open, showing the address and location details (e.g., name, rating, reviews).

### 2. **Dropping a Pin Manually**
- **Step 1**: Click anywhere on the map.
- **Step 2**: A pin will be dropped at that location.
- **Step 3**: The app will fetch and display the **address** of the clicked location in the search bar.
- **Step 4**: The **info window** will show the location's details, including the address and any available Street View images.

### 3. **Locate Me**
- **Step 1**: Click the **Locate Me** button.
- **Step 2**: The map will center on your current location (if geolocation is enabled).
- **Step 3**: A pin will be dropped at your location, and the **info window** will display your current address.

### 4. **Searching for Nearby Places**
- **Step 1**: After dropping a pin (either manually or through the search), you can search for **nearby places** based on the selected location.
- **Step 2**: Select a **category** (e.g., Restaurant, Gym) and a **radius** (e.g., 5KM).
- **Step 3**: The app will display nearby places as markers on the map.
- **Step 4**: Clicking on any marker will open an **info window** with additional details about the place.

### 5. **Interacting with the Info Window**
- **Step 1**: After a pin is dropped, the **info window** will display location details.
- **Step 2**: If available, **Street View** images will also be displayed in the info window.
- **Step 3**: You can click on the pin to reopen the info window anytime.

### 6. **Responsive Design**
- The app is fully **responsive**, meaning it will adapt its layout for mobile and tablet screens.
- On smaller screens, controls (such as the search bar, dropdowns, and buttons) will adjust to fit comfortably.

---

### Troubleshooting

- **Issue**: Location not appearing in the search bar.
  - **Solution**: Make sure the address is properly recognized by Google Maps. Try adjusting the search term for better accuracy.

---

### Notes:
- The **Locate Me** button requires your browser's geolocation to function correctly.
- Street View imagery may not be available for all locations. In such cases, the app will display a fallback message.

With these steps, you should be able to fully interact with the app and explore the map features easily.
