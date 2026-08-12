# 🎓 WebStudy: A Comprehensive E-Learning Platform Prototype

## Table of Contents
1. [Introduction](#introduction)
2. [Project Vision & Philosophy](#project-vision)
3. [Core Features Overview](#core-features)
4. [Technical Architecture](#technical-architecture)
5. [The Sandbox Execution Logic](#the-sandbox-execution-logic)
6. [Getting Started & Installation](#getting-started)
7. [API & Data Management](#api--data-management)
8. [Production Roadmap & Scalability](#roadmap)
9. [Conclusion](#conclusion)

---

<a name="introduction"></a>
## 1. Introduction
WebStudy is a modular, high-performance prototype of an e-learning platform specifically engineered for programming education. Unlike traditional platforms that force students to switch between a video player and an external IDE, WebStudy unifies these experiences into a singular, responsive "Split-Layout" interface. This design maximizes cognitive flow, allowing students to apply theoretical knowledge in a real-time JavaScript environment without ever leaving the instructional context.

<a name="project-vision"></a>
## 2. Project Vision & Philosophy
The philosophical core of WebStudy is "Interactivity through Simplicity." In an era dominated by heavy JavaScript frameworks (React, Vue, Angular), this project demonstrates that professional, reactive, and highly functional web applications can still be built using pure, optimized Vanilla JavaScript. By minimizing dependencies, we achieve faster load times, cleaner DOM interactions, and a lower barrier to entry for developers looking to understand the underlying mechanics of web browser execution.

<a name="core-features"></a>
## 3. Core Features Overview
*   **The Student Dashboard:** Acts as the central command center, providing a visual representation of academic progress. It aggregates data from multiple modules to calculate an overall course completion percentage.
*   **The Split-Layout Interface:** This is the heart of the platform. By organizing the screen into two distinct panes, we cater to the dual nature of programming study: passive learning (video/lecture) and active execution (coding).
*   **Integrated JavaScript Sandbox:** Built using the browser's native `new Function()` constructor, the execution environment provides a safe, sandboxed area where students can manipulate variables, test functions, and observe real-time output.
*   **Interactive Assessments:** The platform includes a dedicated Quiz engine and Exercise validation logic. These aren't just static questions; they are dynamic hooks that challenge the student's comprehension after specific instructional blocks.
*   **Persistence & Data Tracking:** Every action—from marking a lesson as finished to submitting a quiz—is stored in a relational database, ensuring a seamless experience across multiple sessions.

<a name="technical-architecture"></a>
## 4. Technical Architecture
WebStudy adheres to the **Model-View-Template (MVT)** architectural pattern, which is standard in the Django ecosystem.

### The Backend (Django + Python 3)
Django serves as the backbone, handling user authentication, session management, and the object-relational mapping (ORM) required to manage complex relationships between Courses, Modules, Lessons, and Exercises. By using SQLite as the database engine, we maintain simplicity during the prototype phase while ensuring data integrity.

### The Frontend (Vanilla JavaScript + CSS3)
The frontend does not rely on third-party libraries. All dynamic interactions—such as the "Run Code" command, the Quiz feedback mechanism, and the async status updates—are written in modular, event-driven JavaScript. This approach minimizes the total payload size, making the platform exceptionally fast even on slower mobile connections.

<a name="the-sandbox-execution-logic"></a>
## 5. The Sandbox Execution Logic
One of the most critical aspects of WebStudy is how it handles user-provided code.
*   **Scope Isolation:** User code is wrapped into a local variable scope, preventing conflicts with the main application's logic.
*   **Console Redirection:** By overriding `console.log` during the execution cycle, the application successfully intercepts standard browser output and renders it into the custom DOM-based console window provided in the interface.
*   **Security:** Because the execution occurs in the student’s browser (client-side), no malicious user-provided script can reach the Django server, database, or sensitive system files.

<a name="getting-started"></a>
## 6. Getting Started & Installation
This project is optimized for **GitHub Codespaces**. To initialize:

1.  **Clone & Open:** Open the repository in GitHub Codespaces.
2.  **Environment Setup:** Ensure you have Python 3 installed. Run `pip install django`.
3.  **Database Configuration:** Execute `python manage.py makemigrations core` followed by `python manage.py migrate`.
4.  **Admin Access:** Create your credentials with `python manage.py createsuperuser`.
5.  **Execution:** Use `python manage.py runserver` and connect via the provided port forwarding link.

<a name="api--data-management"></a>
## 7. API & Data Management
Django is utilized both as a templating engine and a lightweight API. The front-end communicates with the back-end using the `Fetch API`. When a student clicks "Complete Lesson," a POST request is sent to the `/api/complete/` endpoint. This request is handled asynchronously, updating the database and returning a JSON success status, allowing the UI to react instantly (e.g., changing the button state) without requiring a browser refresh.

<a name="roadmap"></a>
## 8. Production Roadmap & Scalability
While this prototype is functional, scaling it for millions of users requires specific enhancements:
*   **Professional Editor Integration:** Replacing the simple `<textarea>` with the **Monaco Editor** to provide professional-grade syntax highlighting, autocomplete, and error detection.
*   **Containerized Execution:** For back-end support of Python, Java, or C++, transitioning from local client-side execution to secure, isolated Docker containers (e.g., using Kubernetes or AWS Lambda).
*   **Real-time WebSocket Progress:** Implementing Django Channels to provide real-time updates and notifications across the entire platform.
*   **Course Content Delivery Network (CDN):** Migrating video assets to specialized media servers to ensure minimal latency for international users.

<a name="conclusion"></a>
## 9. Conclusion
WebStudy is more than just a coding exercise; it is an exploration of efficient web design. By stripping away unnecessary bloat and focusing on the core pedagogical experience, we have created a platform that is lightweight, scalable, and highly effective for programming instruction. Whether you are using this as a foundation for a commercial platform or an academic project, the architectural choices made here ensure a robust starting point for future growth.
