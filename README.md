# FlexInsights

A Reviews Dashboard for Flex Living.

![Flex Living Logo](https://i.ibb.co/7NgQf8LS/flex-living-logo1.jpg)

## 🧰 Tech Stack

**Client:** Dash,

**Server:** Flask

**Database:** SQLite



## 🚀 Use Cases

FlexInsights supports practical applications for property managers to understand and leverage guest feedback:

- **Per-Property Performance Assessment:** Easily see how individual properties are performing based on guest ratings and comments.
- **Trend Identification:** Spot recurring issues or positive trends across different properties or over time.
- **Review Curation:** Select and approve specific guest reviews to be showcased on the public Flex Living website.
- **Data Normalization:** Automated parsing and normalization of review data for consistent analysis.



## 🔥 Features

FlexInsights provides a comprehensive set of features for review management:

1.  **Hostaway Reviews Integration (Mocked):** Simulates integration with the Hostaway Reviews API using provided mock JSON data.
2.  **Manager Dashboard:** A user-friendly, interactive dashboard allowing managers to:
    - Filter and sort by rating, category, channel, or time.
    - Identify key performance trends through visualizations.
    - Toggle reviews for public display.
3.  **Review Display Page:** Replicates the Flex Living website property details layout, displaying only approved guest reviews.
4.  **Google Reviews Exploration:** Investigates the feasibility of integrating Google Reviews (e.g., via Places API). _[Include your specific findings here, e.g., "Determined basic fetching is possible with API key and Place ID, but not fully implemented due to sandbox constraints."]_
5.  **Data Normalization:** Processes raw review data, extracting and organizing key information like categories, ratings, and listing details.
6.  **Persistent Storage:** Utilizes a local SQLite database to store and persist review data, including manager-approved statuses.
7.  **Authentication for Mock API:** The `/api/reviews/hostaway` endpoint requires specific `X-Hostaway-Account-ID` and `X-Hostaway-API-Key` headers for access.



## 💻 Installation

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
    ```

4.  **Ensure `mock_data.json` is in the project root.** This file is crucial for the application to function.

5.  **Run the application**:
    ```bash
    python app.py
    ```



## ▶️ Usage

- **Manager Dashboard**: Access the interactive dashboard at `http://localhost:5000/`.
- **Public Reviews Page**: View selected public reviews for a specific listing at `http://localhost:5000/reviews/<listing_name>`.
  - _Example_: `http://localhost:5000/reviews/2B%20N1%20A%20-%2029%20Shoreditch%20Heights`



## 🧪 API & Data Details

- **Mock Hostaway Reviews API Endpoint**: `http://localhost:5000/api/reviews/hostaway`
  - **Authentication**: This endpoint requires specific `X-Hostaway-Account-ID` and `X-Hostaway-API-Key` headers in your request. Requests without these credentials will result in a `401 Unauthorized` error.
  - **Testing with `curl`**:
    ```bash
    curl -X GET \
      http://localhost:5000/api/reviews/hostaway \
      -H "X-Hostaway-Account-ID: YOUR_ACCOUNT_ID" \
      -H "X-Hostaway-API-Key: YOUR_API_KEY" \
      -H "Content-Type: application/json"
    ```
- **Local Database**: Uses `reviews.db` to store and manage review data, including the approval status.



## 📝 Authors

- Github: [@bensaied](https://www.github.com/bensaied) 

## 💝 Support

If you find this project helpful, please consider leaving a ⭐️!  
If you are interested or have questions, contact us at **ben.saied@proton.me**

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bensaied/) 
