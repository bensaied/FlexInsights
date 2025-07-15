# FlexInsights Setup Instructions

## Overview

FlexInsights is a Reviews Dashboard for Flex Living, designed to help managers assess property performance based on guest reviews. It includes a manager dashboard for filtering and sorting reviews, spotting trends, and selecting reviews for public display, as well as a public review display page.

---

## Prerequisites

- **Python 3.8+**
- **pip** package manager

---

## Installation

1.  **Clone the repository**:

    ```bash
    git clone <repository_url>
    cd FlexInsights
    ```

2.  **Create a virtual environment and activate it**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:

    ```bash
    pip install flask dash pandas plotly
    # Note: sqlite3 is part of Python's standard library, no need to install via pip
    ```

4.  **Ensure `mock_data.json` is in the project root.** This file contains the mock review data used by the application.

5.  **Run the application**:
    ```bash
    python app.py
    ```

---

## Usage

- **Manager Dashboard**: Access the interactive dashboard at `http://localhost:5000/`.
- **Public Reviews Page**: View selected public reviews for a specific listing at `http://localhost:5000/reviews/<listing_name>`. Replace `<listing_name>` with an actual listing name from your mock data (e.g., `http://localhost:5000/reviews/2B%20N1%20A%20-%2029%20Shoreditch%20Heights`).

---

## API & Data

- **Mock Hostaway Reviews API**: The application implements a mock API endpoint at `http://localhost:5000/api/reviews/hostaway`. This endpoint serves the normalized review data from `mock_data.json` via a local SQLite database.
- **Authentication**: To access the mock Hostaway API endpoint (`/api/reviews/hostaway`), requests **must** include specific authentication headers.
- **Testing the Mock API**: You can test this endpoint using `curl` (or Postman, Insomnia, etc.), ensuring you include the necessary `X-Hostaway-Account-ID` and `X-Hostaway-API-Key` headers in your request. Requests without correct credentials will receive a `401 Unauthorized` response.
- **Local Database**: The application uses a local SQLite database (`reviews.db`) to store and persist review data, including the approval status set in the dashboard.
- **Google Reviews**: Integration with Google Reviews was explored. _[Include your findings here, e.g., "Basic integration was implemented via Google Places API to fetch XYZ, or "Integration was not feasible due to ABC, as detailed in the documentation."]_

---

## Design Notes

- **Manager Dashboard**: Built with **Dash** for an interactive and dynamic user interface. It allows filtering by listing and review category, and displays performance trends through a Plotly graph. Managers can mark reviews for public display directly within the table.
- **Review Display Page**: Replicates the Flex Living property details layout and conditionally displays reviews marked as 'approved' by the manager.
- **Styling**: Utilizes **Tailwind CSS** for a clean, modern, and responsive design, included via a CDN.
