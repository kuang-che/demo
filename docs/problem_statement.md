# Problem Statement

## Background
In team-oriented software development and research projects, tracking progress across multiple workstreams is a common friction point. Teams require lightweight, fast, and visual mechanisms to see the current status of tasks, identify bottlenecks, and assign responsibility. 

Existing project management software can be overly complex, slow, and expensive, requiring extensive configuration. A simple, full-stack collaborative task dashboard provides a baseline tool for visual task management that can be self-hosted locally and extended easily.

## Problem Description
Develop a lightweight, local-first web application that allows team members to:
1. **Visualize tasks** according to three stages: *To Do*, *In Progress*, and *Done*.
2. **Interact with tasks** dynamically (creating new items, modifying their status, and deleting them once resolved).
3. **Persist state** in a relational database locally to prevent loss of information.
4. **Communicate via clear API boundaries** so that different frontend formats (web, CLI, or mobile) can access the same back-end status in the future.
