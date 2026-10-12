# Task: wire a health endpoint end-to-end

Add a new GET `/health` endpoint returning `{ "status": "ok", "service": "skillman-demo" }`. Connect route dispatch, handler registration, and the service function; do not bypass the router. Preserve `/version`, `/items` and `404` behavior exactly. Do not delete or simplify unrelated code.
