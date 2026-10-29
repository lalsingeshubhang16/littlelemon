LITTLE LEMON API — PEER REVIEW ENDPOINTS
Base URL: http://127.0.0.1:8000
GET /api/menu-items/ — list menu (public)
GET /api/menu-items/<id>/ — retrieve menu item (public)
POST /api/menu-items/ — create (staff token required)
PUT/PATCH /api/menu-items/<id>/ — update (staff token required)
DELETE /api/menu-items/<id>/ — delete (staff token required)
GET /api/bookings/ — list own bookings (token required; staff sees all)
GET /api/bookings/?date=YYYY-MM-DD — filter bookings by date
POST /api/bookings/ — create booking (token required)
GET/PUT/PATCH/DELETE /api/bookings/<id>/ — manage own booking (or staff)
POST /api/registration/ — register; JSON username, email, password
POST /api/token/login/ — obtain token; JSON username, password
POST /api/token/logout/ — logout (token required)
Protected header: Authorization: Token <token_key>
Booking JSON: {"first_name":"Asha","reservation_date":"2026-12-15","reservation_slot":"19:00"}
Menu JSON: {"title":"Lemon Pasta","price":"12.50","inventory":20}
Insomnia: use the listed HTTP methods/URLs; send JSON for POST/PUT/PATCH.
