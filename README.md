
# OpenCare-Core 🏥

Open-source healthcare management system for medical facilities in Uganda and beyond.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

## 📋 System Overview

OpenCare-Core manages patient records, appointments, doctor schedules, and medical histories.

### Core Features

- ✅ Patient Registration & Management
- ✅ Appointment Scheduling System
- ✅ Electronic Medical Records (EMR)
- ✅ Prescription Management
- ✅ Doctor Schedule Management
- ✅ Billing and Insurance Integration

## 🏥 Healthcare Workflow

### Patient Journey

```
Patient Arrives → Reception Registers → Doctor Consults → Pharmacy Dispenses → Payment Processed
```

### Step-by-Step Process

1. **Patient Registration** - Collect and validate patient information
2. **Consultation** - Doctor views history, examines, diagnoses
3. **Prescription** - Electronic prescribing to pharmacy
4. **Billing** - Automatic bill generation and payment

## 📂 Module Structure

| Module | Description | Technology |
|--------|-------------|------------|
| patient-management | CRUD operations for patients | Python/Django |
| appointment-system | Scheduling and calendar | JavaScript |
| medical-records | EMR storage and retrieval | PostgreSQL |
| billing | Invoicing and payments | REST API |

## 🗄️ Database Schema

```sql
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/patients` | Register new patient |
| GET | `/api/patients/{id}` | Get patient details |
| PUT | `/api/patients/{id}` | Update patient |
| POST | `/api/appointments` | Book appointment |

## 🚀 Quick Setup

```bash
git clone https://github.com/kayinza/OpenCare-Core.git
cd OpenCare-Core
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) file

---
**Made with ❤️ for healthcare in Uganda**
