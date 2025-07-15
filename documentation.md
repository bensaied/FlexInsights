# FlexInsights Documentation

## Tech Stack

- **Backend**: Flask (Python) for API routes and serving public review pages.
- **Frontend**: Dash (Python) for the interactive manager dashboard.
- **Database**: SQLite for storing reviews and approval status.
- **Styling**: Tailwind CSS for modern, consistent UI.
- **Data Processing**: Pandas for data normalization and analysis.
- **Visualization**: Plotly for trend graphs.

## Key Design and Logic Decisions

1. **Hostaway API Integration**:
   - Mocked using provided JSON data stored in `mock_data.json`.
   - Normalized reviews into SQLite database with fields for ID, type, status, rating, public review, categories (JSON string), submission date, guest name, listing name, and approval status.
   - `GET /api/reviews/hostaway` route returns structured JSON, parsing categories for frontend use.
2. **Manager Dashboard**:
   - Built with Dash for interactivity, featuring a filterable table and trend graph.
   - Filters for listing and category; sortable table columns.
   - Approval toggle in table updates database in real-time.
   - Trend graph shows average ratings per listing across categories, styled with blue, teal, and yellow.
3. **Review Display Page**:
   - Uses Flask’s Jinja2 templating to render public-facing review pages.
   - Displays only approved reviews for a specific listing.
   - Styled with Tailwind CSS for consistency with Flex Living’s modern aesthetic.
4. **Problem-Solving**:
   - Added mock data for multiple listings to demonstrate filtering.
   - Included trend visualization to spot performance issues.
   - Ensured UI is responsive and intuitive, prioritizing manager usability.

## API Behaviors

- **GET /api/reviews/hostaway**:
  - Returns normalized review data in JSON format.
  - Structure: `{ "status": "success", "result": [{ id, type, status, rating, publicReview, categories, submittedAt, guestName, listingName, approved }, ...] }`.
  - Categories are parsed from JSON string for frontend compatibility.
- **Database Operations**:
  - SQLite stores reviews with an `approved` flag (0 or 1).
  - Updates to approval status are persisted via Dash callbacks.

## Google Reviews Findings

- **Exploration**: Investigated Google Places API for review integration.
- **Feasibility**: Requires a valid API key and Place ID for each property. API supports fetching reviews with ratings, text, and dates.
- **Challenges**: Sandbox environment limits real API access; no Place IDs provided for Flex Living properties.
- **Conclusion**: Basic integration is feasible with proper credentials but not implemented due to sandbox constraints. Mock data approach used instead.

## Notes

- The manager dashboard is fully implemented in Dash, accessible at the root URL (`/`).
- The public review page uses Flask’s Jinja2 templating for consistency with Flex Living’s style.
- Future improvements could include pagination for large datasets and advanced trend analysis.
