# Detailed API Rules: Frontend (Bob)

This document describes the frontend communication standards for interacting with the backend API.

## 1. Network Connection Setup
- **Base URL**: The API connects to `http://127.0.0.1:5000/api`. Do not hardcode endpoint addresses in individual methods; always build URLs using `API_BASE_URL`.
- **Request Headers**: When dispatching `POST` or `PUT` payloads, always include `'Content-Type': 'application/json'` in the request header.

## 2. Dynamic DOM Insertion & Security
- **Escape Inputs**: To prevent Cross-Site Scripting (XSS), user-submitted fields (`title`, `description`) must be filtered through `escapeHTML()` before being inserted into innerHTML templates:
  ```javascript
  function escapeHTML(str) {
      return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  ```

## 3. UI State Coordination
- **Reactive state updates**: Maintain a local array `state.tasks`. Perform fetch operations to synchronize local arrays, then immediately invoke `renderTasks()` to redraw cards and status numbers.
- **Failover / Offline warning**: If a connection fails, alert the user using a toast or alert indicator specifying that the backend server on port 5000 might be offline.
