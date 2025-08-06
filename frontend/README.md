# CPE Frontend

This is the frontend application for the CPE (Common Platform Enumeration) Viewer.  
It allows users to view, search, filter, and paginate through CPE data retrieved from a RESTful backend API.

---

## Features

- Table view of CPE entries:
  - Title (with truncation and tooltip)
  - CPE 2.2 URI
  - CPE 2.3 URI
  - Deprecated dates (formatted as `MM DD YYYY`)
  - Reference links (up to 2 shown, expandable "X more" popover)
- Filter by:
  - Title
  - CPE 2.2 URI
  - CPE 2.3 URI
  - Deprecation date (prior to)
- Fully paginated (customizable results per page: 15–50)
- Frontend built with **React** and **MUI (Material UI)**

---

## Setup Instructions:

### 1. Download and open zipped files:

    -->bash
    cd cpe-api-project/frontend

### Install dependencies:

    --> bash
    npm install

### Configure API URL (if needed)

    Default: http://127.0.0.1:5000

### Run the app:

    --> bash
    npm start

    --> Visit: http://localhost:3000

## NOTE:
- Make sure the backend is running and accessible when using the frontend
- CORS must be enabled in the backend if you're accessing it from a different domain or port


