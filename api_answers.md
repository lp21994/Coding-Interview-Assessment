Scenario questions 
C1. How would you prove that our Xero API connection is working before checking invoices? 
We can send a `GET` request to the `/connections` endpoint. A successful `200 OK` response returning a valid list of connected tenants (orgs) proves that the OAuth 2.0 authentication is successful and the API connection is active.
C2. If /connections works but GET /Invoices fails, what would you check? 
 Check if the Access Token has the `accounting.journals.read` or `accounting.invoices.read` scope. Ensure the `Xero-Tenant-Id` header is correctly passed and matches a valid tenant ID obtained from the `/connections` endpoint.Check the error code (e.g., `403 Forbidden` means insufficient permissions; `401 Unauthorized` means expired token).
C3. What endpoint would you call to check invoices? 
GET https://api.xero.com/api.xro/2.0/Invoices`
C4. How would you check one specific invoice? 
Append the specific `InvoiceID` (GUID) to the endpoint path:
`GET https://api.xero.com/api.xro/2.0/Invoices/{InvoiceID}`
C5. If the invoice API returns 429, how should the backend handle it?
 Read Retry-After Header: Check the `Retry-After` HTTP header to know how many seconds to wait.
Implement Exponential Backoff:Use a backoff algorithm with jitter to retry the request after a delay.
Rate Limiting Queues: Queue subsequent requests instead of flooding the API to respect Xero's rate limits (Concurrent, Minute, and Daily limits).