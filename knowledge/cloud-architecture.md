# Cloud Architecture Principles

These principles guide the design of scalable, resilient cloud systems.

## 1. Design for Failure
- **Expectation**: Resources will fail. Network packets will drop. Latency will spike.
- **Mitigation**:
  - **Redundancy**: Deploy across multiple Availability Zones (AZs).
  - **Decoupling**: Use queues (Pub/Sub, SQS) to buffer between services.
  - **Self-Healing**: Use Auto Scaling Groups and managed instance groups.

## 2. Infrastructure as Code (IaC)
- **Immutable**: Once a server is deployed, do not patch it. Replace it.
- **Declarative**: Define *what* you want (Terraform), not *how* to get there.
- **Versioned**: Infrastructure code belongs in Git.

## 3. The 12-Factor App (Cloud Native)
1.  **Codebase**: One codebase tracked in revision control, many deploys.
2.  **Dependencies**: Explicitly declare and isolate dependencies.
3.  **Config**: Store config in the environment, not in the code.
4.  **Backing Services**: Treat backing services as attached resources.
5.  **Build, Release, Run**: Strictly separate build and run stages.
6.  **Processes**: Execute the app as one or more stateless processes.
7.  **Port Binding**: Export services via port binding.
8.  **Concurrency**: Scale out via the process model.
9.  **Disposability**: Maximize robustness with fast startup and graceful shutdown.
10. **Dev/Prod Parity**: Keep development, staging, and production as similar as possible.
11. **Logs**: Treat logs as event streams.
12. **Admin Processes**: Run admin/management tasks as one-off processes.

## 4. Security Layers
- **Identity**: The new perimeter. Strong IAM is paramount.
- **Compute**: Minimal OS images, no root access.
- **Network**: Private IPs only, load balancers as entry points, WAF enabled.
- **Data**: Encryption at rest (KMS) and in transit (TLS).
