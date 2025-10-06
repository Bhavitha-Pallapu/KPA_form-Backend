# Railway Maintenance Forms

> A Django-powered REST API backend for managing railway maintenance forms with comprehensive validation, PostgreSQL integration, and optional monitoring.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2.4-green.svg)](https://djangorestframework.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://docker.com)
[![Monitoring](https://img.shields.io/badge/Monitoring-Enabled-lightgrey.svg)]()
[!-- AWS badge removed --]

---
## 🎥 Video Tutorials

| Tutorial | Link | Description |
|----------|------|-------------|
| 🚀 **Setup & Development** | [Watch Now](https://drive.google.com/file/d/17QCv4pfbuGwF-YY-i1CHJYKyUKcSJ8ya/view?usp=sharing) | Initial setup, configuration & API testing |
| 🐳 **Docker Deployment** | [Watch Now](https://drive.google.com/file/d/1pbGgeTAep39GuDYdNK1tmojN1PWTQ1Fv/view?usp=drive_link) | Containerization and logging |
| 📊 **Monitoring Overview** | [Watch Now](https://drive.google.com/file/d/1pbGgeTAep39GuDYdNK1tmojN1PWTQ1Fv/view?usp=drive_link) | Real-time monitoring & log analytics setup |
---

## Overview

The **Railway Maintenance Forms** backend is a robust Django REST Framework service designed specifically for railway maintenance operations. It provides structured APIs to handle and validate critical maintenance forms including bogie checksheets and wheel specifications, ensuring data integrity and compliance with railway standards.

## Key Differentiators

### Beyond Basic CRUD
- **Railway Domain Expertise**: Understanding of engineering tolerances and maintenance workflows
- **Production-Ready Architecture**: Full monitoring, logging, and deployment pipeline
- **Comprehensive Testing**: API testing suite with edge cases
- **Documentation Quality**: Clear setup instructions and video walkthroughs

### Technical Depth
- **Custom Middleware**: Request/response logging and timing
- **Advanced Querying**: Optimized database queries with proper indexing
- **Error Recovery**: Graceful handling of database connection issues
- **Monitoring Integration**: Real-time application health tracking

### Key Highlights

- **Comprehensive Validation** - Custom validation logic for all railway-specific form fields
- **Modular Architecture** - Clean separation of concerns with Django apps
- **PostgreSQL Integration** - Reliable data storage with advanced querying capabilities  
- **Containerized Deployment** - Docker-ready with production configurations
- **Advanced Monitoring** - Integrated application monitoring and structured logging for production insights
- **Cloud-Native** - Optimized for cloud deployments (provider agnostic)
- **API Documentation** - Complete Postman collection with examples


---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+**
- **PostgreSQL 12+**
- **Docker & Docker Compose** (for containerized setup)
- **pip** (Python package manager)

### 🛠️ Local Development Setup

#### Option 1: Traditional Setup

```bash
# 1. Clone and navigate to the project
git clone <repository-url>
cd railway-maintenance-forms

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your database credentials

# 5. Run database migrations
python manage.py migrate

# 6. Start the development server
python manage.py runserver
```

docker-compose up --build
#### Option 2: Docker Setup (Recommended)

```bash
# 1. Clone the repository
git clone <repository-url>
cd railway-maintenance-forms

# 2. Configure environment variables
cp .env.example .env
# Edit .env with your production settings

# 3. Build and start containers
docker-compose up --build

# 4. Access the API
# http://localhost:8000
```

---

## 📊 Technology Stack

<table>
<tr>
<td>

**Backend Framework**
- Django 5.2.4
- Django REST Framework
- Python 3.9+

</td>
<td>

**Database**
- PostgreSQL 12+
- Django ORM
- Custom migrations

</td>
</tr>
<tr>
<td>

**Monitoring & Logging**
- Application Performance Monitoring (APM) - optional via your provider
- Structured JSON logging
- Request/Response middleware
- Error tracking & alerts

</td>
<td>

**Infrastructure**
- Docker & Docker Compose
- Gunicorn WSGI server
- Environment-based config

</td>
</tr>
<tr>
<td colspan="2">

**Deployment**
- Cloud instances / managed DB (provider-agnostic)
- Production-ready monitoring
- Automated log aggregation

</td>
</tr>
</table>

---

## 🏗️ Project Architecture


```
railway-maintenance-forms/
├── api/                       # Core Django app (renamed from forms_api)
│   ├──  helpers/                    # Utility functions
│   │   ├── validation.py            # Form validation logic
│   │   └── response_formatter.py    # API response formatting
│   ├──  migrations/                 # Database schema changes
│   ├──  models.py                   # Data models
│   ├──  serializers.py              # API serializers
│   ├──  urls.py                     # URL routing
│   ├──  views.py                    # API view classes
│   └──  tests.py                    # Unit tests
├── railway_project/                 # Django project settings
│   ├── logging_config.py            # Comprehensive logging setup
│   ├── middleware.py                # Request/Response logging
│   └── settings.py                  # Django configuration
# Runtime log files are not stored in the repository; any local
# logs generated during development or in containers have been
# removed from source control to avoid committing runtime artifacts.
├── Dockerfile                       # Container configuration
├── docker-compose.yml               # Multi-container setup (monitoring optional)
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```


---

## 🔌 API Endpoints

| Endpoint | Method | Description | Status |
|----------|--------|-------------|--------|
| `/api/forms/bogie-checksheet` | `POST` | Submit bogie checksheet with validation | ✅ Active |
| `/api/forms/wheel-specifications` | `POST` | Submit wheel specification data | ✅ Active |
| `/api/forms/wheel-specifications/list` | `GET` | Retrieve wheel specifications with filters | ✅ Active |

## 📘 API Usage Examples

### 1️⃣ Submit Wheel Specification

**Endpoint:** `POST /api/forms/wheel-specifications`

```json
{
  "fields": {
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "condemningDia": "825 (800-900)",
    "intermediateWWP": "20 TO 28",
    "lastShopIssueSize": "837 (800-900)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "treadDiameterNew": "915 (900-1000)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelDiscWidth": "127 (+4/-0)",
    "wheelGauge": "1600 (+2,-1)",
    "wheelProfile": "29.4 Flange Thickness"
  },
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "status": "Saved",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03"
  }
}
```

### 2️⃣ Submit Bogie Checksheet

**Endpoint:** `POST /api/forms/bogie-checksheet`

```json
{
  "bogieDetails": {
    "bogieNo": "BG1234",
    "dateOfIOH": "2025-07-01",
    "deficitComponents": "None",
    "incomingDivAndDate": "NR / 2025-06-25",
    "makerYearBuilt": "RDSO/2018"
  },
  "bogieChecksheet": {
    "axleGuide": "Worn",
    "bogieFrameCondition": "Good",
    "bolster": "Good",
    "bolsterSuspensionBracket": "Cracked",
    "lowerSpringSeat": "Good"
  },
  "bmbcChecksheet": {
    "adjustingTube": "DAMAGED",
    "cylinderBody": "WORN OUT",
    "pistonTrunnion": "GOOD",
    "plungerSpring": "GOOD"
  },
  "formNumber": "BOGIE-2025-001",
  "inspectionBy": "user_id_456",
  "inspectionDate": "2025-07-03"
}
```

### 3️⃣ Retrieve Wheel Specifications

**Endpoint:** `GET /api/forms/wheel-specifications/list?formNumber=WHEEL-2025-001`

```json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
        "bearingSeatDiameter": "130.043 TO 130.068"
        // ... additional fields
      }
    }
  ]
}
```


---
**Monitoring & Logging**

The project includes structured JSON logging and request/response middleware. Integration with a monitoring provider (APM/log aggregation) is optional — add your preferred provider and configuration if needed.

### Log Categories

| Log Type | File | Description |
|----------|------|-------------|
| **General** | `django.log` | Django framework logs |
| **Requests** | `requests.log` | HTTP request/response logs |
| **API** | `api.log` | Application-specific logs |
| **Database** | `database.log` | Database query logs |
| **Errors** | `errors.log` | Error and exception logs |

---


## 🌩️ AWS Deployment

### Infrastructure Setup

```bash
# 1. Launch EC2 instance
aws ec2 run-instances \
  --image-id ami-0abcdef1234567890 \
  --count 1 \
  --instance-type t3.medium \
  --key-name your-key-pair \
  --security-groups web-server-sg

# 2. Create RDS PostgreSQL instance
aws rds create-db-instance \
  --db-instance-identifier railway-forms-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password your-secure-password \
  --allocated-storage 20
```

### Deployment Steps

1. **Configure Security Groups**
   - Allow HTTP/HTTPS traffic (ports 80, 443)
   - Allow SSH access (port 22)
   - Configure RDS security group for PostgreSQL (port 5432)
  - Allow monitoring agent communication if you run an external agent (e.g., ports 8125, 8126)

2. **Environment Setup**
   ```bash
   # SSH into EC2 instance
   ssh -i your-key.pem ec2-user@your-ec2-ip
   
   # Install Docker
   sudo yum update -y
   sudo yum install -y docker
   sudo systemctl start docker
   
  # Deploy application
   git clone <your-repo>
  cd railway-maintenance-forms
   docker-compose up -d
   ```

3. **Production Environment Variables**
   ```bash
   # .env configuration for production
   DEBUG=False
   SECRET_KEY=your-production-secret-key
   ALLOWED_HOSTS=your-domain.com,your-ec2-ip
   
   # Database Configuration
   DB_HOST=your-rds-endpoint.amazonaws.com
  DB_NAME=railway_forms_db
   DB_USER=admin
   DB_PASSWORD=your-secure-password
   DB_PORT=5432
   
  # Monitoring configuration (optional)
  # Add your monitoring provider API keys here if you're using one.
   ```

---

## 🧪 Testing

### Run Test Suite

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test forms_api

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

### Test Categories

- **✅ Unit Tests** - Individual function validation
- **🔗 Integration Tests** - API endpoint testing  
- **📊 Data Validation Tests** - Form field validation
- **🔒 Authentication Tests** - Security validation
- **🖥️ Monitoring Tests** - Logging and metrics validation

---

## 📚 Resources & Documentation

| Resource | Link | Description |
|----------|------|-------------|
| 📮 **Postman Collection** | [Download](https://drive.google.com/file/d/1-A6R_Paf6DYv2s4L8zza_fCkPygGduqf/view) | Complete API testing collection |
| 📊 **Monitoring Dashboard** | [View Dashboard](#) | Production monitoring dashboard (provider-specific)

---

## ⚠️ Important Notes

### System Requirements
- ✅ PostgreSQL database is required and must be properly configured
- ✅ Environment variables must be set for database connectivity (and monitoring if used)
- ✅ Docker containers require sufficient system resources
- ✅ AWS deployment requires proper IAM permissions
- ✅ Monitoring/observability provider optional - configure if you need APM or remote log collection

### Data Validation
- ✅ All form fields undergo comprehensive validation
- ✅ Date formats must follow ISO 8601 standard (YYYY-MM-DD)
- ✅ Form numbers must be unique and follow specified patterns
- ✅ Railway-specific measurements must include proper units and tolerances

### API Response Format
All API responses follow this consistent structure:
```json
{
  "success": boolean,
  "message": "string",
  "data": object | array
}
```

### Monitoring & Alerts
- ✅ All API requests are logged locally via structured logging
- ✅ Database query performance can be tracked via your chosen provider
- ✅ Error rates and response times can be monitored by connecting an APM or monitoring service

---

## 📦 Dependencies

### Core Dependencies
```txt
Django==5.2.4
djangorestframework
django-cors-headers
python-decouple
psycopg2-binary
gunicorn
python-json-logger
```

### Development Dependencies
```txt
pytest
pytest-django
coverage
black  # Code formatting
flake8  # Code linting
```

---

## 📞 Support & Contributing

### Getting Help
- 📧 **Email**: saikrishnadandu9@gmail.com
-- 📊 **Monitoring**: Check your monitoring provider dashboard for system health

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include logging for important operations
- Write tests for new features

---


## 🚀 Roadmap

### Current Sprint
- ✅ Basic form submission APIs
- ✅ PostgreSQL integration
- ✅ Docker containerization
- ✅ Monitoring integration available (provider-agnostic)
- ✅ AWS deployment guide


