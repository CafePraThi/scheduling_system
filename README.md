## Scheduling System

### Description
A system designed to manage and schedule appointments efficiently, ensuring that sellers are not double-booked.

### Objective
To provide a scheduling solution that includes appointment creation, conflict validation, and a calendar view.

## Installation Instructions


### Installation Steps

1. Clone the repository:
    ```bash
    git clone [<repository-url>](https://github.com/CafePraThi/scheduling_system)
    ```

2. Navigate to the bench directory:
    ```bash
    cd $PATH_TO_YOUR_BENCH
    ```

3. Get the app:
    ```bash
    bench get-app [<URL_OF_THIS_REPO>](https://github.com/CafePraThi/scheduling_system) --branch develop
    ```

4. Install the app:
    ```bash
    bench install-app scheduling_system
    ```

5. Install the app on site:
    ```bash
    bench --site your-site install-app scheduling_system
    ```

## Configuration Details

### Activate Developer Mode
To edit/create DocTypes, activate developer mode:
```bash
bench set-config developer_mode 1
```

## Database Schema

### DocTypes

#### Appointment DocType:
- **Client Name**: Data
- **Start date**: Datetime
- **End date**: Datetime (Read-only, set programmatically based on the start date and duration)
- **Duration**: Time
- **Description**: Small Text
- **Seller**: Link (Links to a User)
- **Status**: Select (Options: Scheduled, Finished, Canceled)

## Key Features

- **Appointment Creation**: Users can create appointments with specified details.
- **Conflict Validation**: Ensures that a seller cannot have overlapping appointments.
- **Calendar View**: Configured as the default view for appointments.

## Usage Instructions

### Creating an Appointment
1. Log in to the system.
2. Navigate to the Appointments List.
3. Click on "Add Appointment."
4. Fill in the required fields and save.

### Calendar View
1. Navigate to the Appointments List.
2. The calendar view is set as the default view, displaying all appointments.

## Code Documentation

### Code Structure
- `apps/scheduling_system`: Main app directory.
- `doctype/appointment`: Contains the Appointment DocType.
  - `appointment.py`: Backend logic for Appointment Doctype .
  - `appointment.js`: Client-side logic for Appointment Doctype.
  - `appointment_calendar.js`: JavaScript for calendar view.
  - - `appointment_api.py`: Provides API endpoints for Appointment Doctype.

### Key Modules

#### appointment.py
Handles backend logic for appointment management, including validation and utility functions.

#### appointment.js
Configures and apply calendar as primary view

#### appointment_calendar.js
Configures and manages the calendar view for appointments.

#### appointment_api.py
Provides API endpoints and server-side logic for managing appointments via HTTP requests.

## API Documentation

### Postman API Link

Here is the [[API Documentation Link](https://documenter.getpostman.com/view/26683227/2sA3kPojDf)]. In this documentation, you will find detailed information on the available endpoints, including how to:

- Retrieve all appointments
- Retrieve a single appointment
- Create a new appointment
- Update an existing appointment
- Delete an appointment

## Final Considerations

### Potential System Enhancements

- **Duration Field - Time**: Improve the user experience by refining the duration field format.
- **Repeating Meetings for Multiple Consecutive Days**: Enable scheduling of recurring meetings over several consecutive days.
- **Client Retrieval from System**: Integrate the system to automatically fetch client.
- **Integration with Google Calendar, Microsoft Teams, or Other Calendars**: Facilitate automatic synchronization of appointments with external calendar platforms.
- **Restrict Appointment Creation**: Allow appointment creation only with the initial status "Scheduled".
- **Access Profiles**:
  - Users can only view their own appointments.
  - Managers have access to appointments for all users.
- **Email Notifications and Appointment Reminders**: Implement automatic email notifications for appointment reminders.
- **Estimate Hours of Meetings Held per Month**: Develop functionality to estimate and display the number of hours of meetings held each month.
- **Enhanced Management Reports**: Improve management reports to provide detailed insights into system usage and performance.
- **Endpoints**:
  - **Enhanced API Permissions**: Block Guess API.
  - **Pagination**: Implement pagination in endpoints to enhance performance and navigation of results.

### Challenges Encountered in the Project

Due to the limited time available, I managed to achieve some of the project goals. However, with more dedicated time for documentation and exploration, I believe I could have gained a deeper understanding of the system. This was my first experience with the library, and initially, there was limited content available online. Despite this, I found the documentation to be robust and encountered a vibrant community and active forums. With more time invested in learning alongside the documentation, I am confident I could have achieved a more profound insight into the system.


## Pre-commit Configuration

Pre-commit is configured to use the following tools for checking and formatting your code:
- ruff
- eslint
- prettier
- pyupgrade

## License
This project is licensed under the MIT License.

Feel free to paste this markdown text into your GitHub repository's README file.
