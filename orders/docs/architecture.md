# Munjiz Backend Architecture Document

## 1. Project Overview

Munjiz is a delivery operations system designed to manage on-demand delivery services starting in New Assiut City.

The system is currently focused on building a strong operational backbone before scaling into a full marketplace model.

---

## 2. Current System State (Phase 1 - Core Foundation)

The backend is built using:

- Python
- Django
- PostgreSQL
- Git version control

The system is structured as a modular Django project.

---

## 3. Core Entities

### Order

Represents a customer delivery request.

Main fields:
- customer_name
- customer_phone
- pickup_address
- delivery_address
- total_amount
- delivery_fee
- status
- rider (ForeignKey)
- created_at

Business Logic:
- If a rider is assigned and status is "pending", it automatically becomes "assigned".

---

### Rider

Represents a delivery agent.

Main fields:
- name
- phone
- status (online / offline / busy)
- created_at

---

## 4. Current Workflow

Order Lifecycle (initial version):

- pending
- assigned
- delivered
- cancelled

Automatic rule:
Assigning a rider updates order status to "assigned".

---

## 5. Dispatch Model (Current)

Manual dispatch via admin panel.

Future target:
Semi-automated dispatch logic.

---

## 6. Version Control

Project is managed via Git and hosted on GitHub.

Repository:
munjiz-backend

---

## 7. Next Engineering Milestone

- Expand Order lifecycle with detailed timestamps.
- Implement Zone system for pricing and delivery segmentation.
- Strengthen dispatch logic.