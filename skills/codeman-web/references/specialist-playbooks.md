# Codeman Web — specialist playbooks

Use this reference when the request involves full-stack web application development. Select the applicable subsection(s) based on the actual repository and request; do not execute every workflow reflexively. Record evidence from actual files, output, and tool results. Keep all operations within the Codeman operating contract.

**Routing clues:** React, Next.js, FastAPI, Flask, Node.js.

## React

1. Inspect component tree, routing, state stores, prop interfaces, hooks, forms, feature flags, design system, and existing tests.
2. Preserve every existing component capability, event path, keyboard interaction, loading/error/empty state, and accessibility semantics.
3. Check effect dependencies, cleanup, stale closures, memoization assumptions, and uncontrolled versus controlled inputs.
4. Wire backend/API changes through real typed client calls or existing data layers; do not use fake data to satisfy a feature request.
5. Validate UI behavior, accessibility, and regression tests across relevant viewports and states.

## Next.js

1. Identify Next.js and React versions, App Router versus Pages Router, server/client component boundaries, caching, middleware, actions, and deployment configuration.
2. Preserve route paths, dynamic params, SEO metadata, authentication/session boundaries, streaming, prefetch, and API contracts.
3. Keep server secrets server-side; validate data access in server actions/route handlers and prevent cross-user cache leaks.
4. Account for SSR/hydration differences, runtime targets (Node/Edge), redirects, errors, and static/dynamic rendering rules.
5. Run repository build, typecheck, and route-level integration tests; review any changes to deployment output.

## FastAPI

1. Inspect application factory, routers, dependencies, Pydantic version/models, lifespan handlers, middleware, and persistence layers.
2. Preserve endpoint paths, status codes, response schemas, validation behavior, authentication/authorization and OpenAPI contracts.
3. Use correct async/sync IO semantics; handle transactions, cancellation, connection pooling, errors, and dependency overrides properly.
4. Validate untrusted inputs and avoid exposing internal exceptions or secrets.
5. Exercise endpoint success/error/auth paths using existing pytest/httpx fixtures where available.

## Flask

1. Inspect app factory, blueprints, configuration loading, extensions, WSGI deployment, templates, sessions, and migrations.
2. Preserve routes, methods, view return types, Flask application/request context, CSRF defenses, authentication and error handlers.
3. Keep extension lifecycle and database session/transaction scope correct; do not modify global app state in unsafe ways.
4. Validate template escaping, uploads, path handling, cookie/security flags, and content types.
5. Run relevant Flask and database integration tests across required configurations.

## Node.js

1. Identify Node version, module mode, framework, process model, package manager/lockfile, queues, websockets, and environment configuration.
2. Preserve async error propagation, request lifecycle, stream backpressure, listeners, shutdown hooks, and exported APIs.
3. Validate authentication, request body limits, rate constraints, input parsing, security headers, and outbound network timeouts.
4. Manage resource cleanup for sockets, files, child processes, and background tasks; do not block the event loop with avoidable synchronous work.
5. Run existing tests, lint, typechecking if configured, and start/build smoke checks where feasible.

## Full-stack integration

1. Trace each feature UI → state → client → API → authorization → persistence → response → UI.
2. Preserve schema compatibility, validation, pagination, error states, redirects, authentication, cookies, CORS, and observability.
3. For app-opening workflows, inspect the project for the shared montage requirement and retrieve the authentic asset from a configured source only through authorized non-metered GitHub reads.
4. Deliver complete components/routes/models/configurations/tests rather than detached snippets.

