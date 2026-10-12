# Codeman API — specialist execution playbook

## Preconditions

Use for creating or repairing service endpoints, schemas, handlers, client SDKs, authentication boundaries, and distributed API integrations.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Catalog the exposed surface

1. Identify API types, endpoint/method or RPC names, middleware order, authentication, scopes, rate limits, request and response contracts.
2. Inspect actual implementation, schemas, clients, generated bindings, API gateways, CORS settings, and historical versions.
3. Trace at least one complete request through auth, validation, business logic, persistence, and response encoding.
## Phase 2: Specify contract and failure semantics

1. Define parameter constraints, status/error codes, pagination, sorting, partial results, cancellation, timeouts, retry semantics, and idempotency.
2. Specify WebSocket reconnect/backpressure and GraphQL authorization per field, or gRPC deadline/status mapping where relevant.
3. Classify compatibility impacts and preserve legacy client behavior without silently dropping routes.
## Phase 3: Implement production behavior

1. Wire routes/RPC registrations, middleware, serializers, database access, permission enforcement, logging, tracing, and error handling.
2. Use structured validated inputs and parameterized persistence; reject ambiguous payloads and apply bounded resource use.
3. Update generated API documentation and client packages consistently when source-of-truth schemas change.
## Phase 4: Test actual contracts

1. Exercise authenticated and unauthorized calls, valid/invalid payloads, status codes, concurrency, timeouts, pagination, and upstream failure.
2. Verify old-client/new-server and new-client/old-server compatibility using genuine protocol requests when possible.
3. Check CORS/CSRF behavior, secrets handling, rate limits, and streaming disconnect handling applicable to the specific API.
## Phase 5: Deliver integrated API artifacts

1. Provide complete handlers, schemas, client integrations, configuration, and tests; include deployment registrations.
2. Publish executed requests/results and unresolved client or infrastructure dependencies.
3. Avoid claiming endpoints are live when only static schemas or local mocks exist.

## Required project deliverables

1. **API and consumer inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Versioned wire contracts and error semantics** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Complete route/service/client integration** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Authenticated and negative contract tests** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Deployment and gateway requirements** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Writing a handler without router registration.
- Returning secret internals in errors.
- Changing status codes without client review.
- Unit testing serializers without exercising HTTP/RPC transport.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
