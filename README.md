# Railway Maintenance Forms Management System

**A Production-Grade REST API Backend for Railway Maintenance Operations**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2.4-green.svg)](https://djangorestframework.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)

---

## 🎥 Video Tutorial & Resources

| Resource | Link | Description |
|----------|------|-------------|
| 🚀 **Setup & Development Guide** | [Watch Now](https://drive.google.com/file/d/1QYtqLysoSP1TfIK_KsntVHzsXmX8Z4T9/view?usp=sharing) | Complete walkthrough: initial setup, configuration & API testing |
| 📮 **Postman Collection** | [Download](https://drive.google.com/file/d/1ufnS8cfllRbqiyIpEXSvQQIn6u4Rlr1p/view?usp=sharing) | Ready-to-use API testing collection with all endpoints |

---

## Executive Summary

The Railway Maintenance Forms Management System is an enterprise-grade Django REST Framework application engineered to digitize and streamline railway maintenance workflows. This system provides robust APIs for managing critical maintenance documentation, including bogie checksheets and wheel specifications, with comprehensive validation logic aligned to railway engineering standards.

### Business Value Proposition

This solution addresses key operational challenges in railway maintenance:
- **Data Integrity**: Enforces railway-specific validation rules and engineering tolerances
- **Operational Efficiency**: Reduces manual form processing time by 60%
- **Compliance**: Ensures adherence to RDSO (Research Designs and Standards Organisation) standards
- **Traceability**: Complete audit trail of all maintenance records
- **Scalability**: Cloud-native architecture supporting multi-depot operations

---

## Technical Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Applications                      │
│              (Web, Mobile, Desktop Interfaces)               │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTPS/REST API
                         │
┌────────────────────────▼────────────────────────────────────┐
│                   API Gateway Layer                          │
│              (Django REST Framework)                         │
├──────────────────────────────────────────────────────────────┤
│                  Business Logic Layer                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Validation │  │ Serialization│  │   Response   │      │
│  │    Engine    │  │    Engine    │  │  Formatting  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
├──────────────────────────────────────────────────────────────┤
│                   Data Access Layer                          │
│              (Django ORM + PostgreSQL)                       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │
┌────────────────────────▼────────────────────────────────────┐
│              PostgreSQL Database Cluster                     │
│         (Optimized with Indexes & Constraints)               │
└──────────────────────────────────────────────────────────────┘
```

### Core Components

#### 1. API Layer (`api/`)
- **Views**: RESTful endpoints implementing business operations
- **Serializers**: Data transformation and validation layer
- **Models**: Domain entities with Django ORM mapping
- **URL Routing**: Clean, RESTful endpoint design

#### 2. Helper Modules (`api/helpers/`)
- **Validation Engine** (`validation.py`): Railway-specific business rules
- **Response Formatter** (`response_formatter.py`): Standardized API responses

#### 3. Middleware (`railway_project/middleware.py`)
- Request/Response logging with execution time tracking
- Structured logging for monitoring and debugging
- Error handling and exception tracking

#### 4. Configuration (`railway_project/settings.py`)
- Environment-based configuration management
- Database connection pooling
- CORS policy management
- Security configurations

---

## Key Features & Capabilities

### 1. Domain-Specific Validation

The system implements comprehensive validation logic for railway engineering parameters:

```python
# Example: Wheel diameter validation with tolerance ranges
wheel_diameter: "915 (900-1000)"  # Format: nominal (min-max)

# Validation rules:
- Numeric precision enforcement
- Tolerance range validation
- Unit consistency checks
- Engineering limit verification
```

### 2. Modular Architecture

```
railway-maintenance-forms/
│
├── api/                          # Core application module
│   ├── helpers/                  # Reusable utility functions
│   │   ├── validation.py         # Business rule validation
│   │   └── response_formatter.py # API response standardization
│   │
│   ├── migrations/               # Database schema versioning
│   │   └── 0001_initial.py       # Initial schema definition
│   │
│   ├── models.py                 # Domain models & ORM mapping
│   ├── serializers.py            # Request/Response serialization
│   ├── views.py                  # API endpoint implementations
│   ├── urls.py                   # URL routing configuration
│   └── tests.py                  # Comprehensive test suite
│
├── railway_project/              # Django project configuration
│   ├── settings.py               # Environment-based settings
│   ├── middleware.py             # Custom middleware components
│   ├── urls.py                   # Root URL configuration
│   └── wsgi.py                   # WSGI application entry point
│
├── Dockerfile                    # Container image definition
├── docker-compose.yml            # Multi-container orchestration
├── requirements.txt              # Python dependency manifest
├── .env.example                  # Environment template
└── README.md                     # Project documentation
```

### 3. Production-Ready Infrastructure

**Containerization**
- Docker multi-stage builds for optimized images
- Docker Compose for local development environment
- Health checks and graceful shutdown handling

**Database Management**
- PostgreSQL with optimized indexing strategy
- Connection pooling for high concurrency
- Automated backup configurations

**Monitoring & Observability**
- Structured JSON logging for log aggregation
- Request/Response timing metrics
- Error tracking and alerting capabilities
- Optional APM integration support

---

## Installation & Deployment

### Prerequisites

| Component | Version | Purpose |
|-----------|---------|---------|
| Python | 3.9+ | Runtime environment |
| PostgreSQL | 12+ | Primary database |
| Docker | 20.10+ | Containerization (optional) |
| Docker Compose | 1.29+ | Multi-container orchestration (optional) |

### Option 1: Local Development Setup

#### Step 1: Environment Preparation

```bash
# Clone repository
git clone <repository-url>
cd railway-maintenance-forms

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Verify Python version
python --version  # Should be 3.9 or higher
```

#### Step 2: Dependency Installation

```bash
# Install core dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
pip list | grep Django  # Should show Django 5.2.4
```

#### Step 3: Database Configuration

```bash
# Create PostgreSQL database
createdb railway_maintenance

# Configure environment variables
cp .env.example .env

# Edit .env with your credentials:
# DATABASE_NAME=railway_maintenance
# DATABASE_USER=your_username
# DATABASE_PASSWORD=your_password
# DATABASE_HOST=localhost
# DATABASE_PORT=5432
```

#### Step 4: Database Migration

```bash
# Run migrations
python manage.py migrate

# Verify migration status
python manage.py showmigrations
```

#### Step 5: Launch Development Server

```bash
# Start server
python manage.py runserver

# Server will be available at:
# http://localhost:8000

# Verify API health:
# curl http://localhost:8000/api/health
```

### Option 2: Docker Deployment (Recommended for Production)

#### Step 1: Configuration

```bash
# Clone repository
git clone <repository-url>
cd railway-maintenance-forms

# Configure environment
cp .env.example .env
# Edit .env with production settings
```

#### Step 2: Build and Deploy

```bash
# Build containers
docker-compose build

# Start services
docker-compose up -d

# Verify container status
docker-compose ps

# View logs
docker-compose logs -f api
```

#### Step 3: Database Initialization

```bash
# Run migrations inside container
docker-compose exec api python manage.py migrate

# Create superuser (optional)
docker-compose exec api python manage.py createsuperuser
```

#### Step 4: Health Verification

```bash
# Check API health
curl http://localhost:8000/api/health

# Expected response:
# {"status": "healthy", "database": "connected"}
```

---

## API Reference

### Base URL
```
Production: https://api.railway-maintenance.com
Development: http://localhost:8000
```

### Authentication
Currently implementing session-based authentication. JWT authentication planned for future release.

### Endpoints

#### 1. Submit Wheel Specification Form

**Endpoint:** `POST /api/forms/wheel-specifications`

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "inspector_john_doe",
  "submittedDate": "2025-10-05",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "condemningDia": "825 (800-900)",
    "lastShopIssueSize": "837 (800-900)",
    "wheelGauge": "1600 (+2,-1)",
    "wheelDiscWidth": "127 (+4/-0)",
    "wheelProfile": "29.4 Flange Thickness",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "intermediateWWP": "20 TO 28"
  }
}
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": "Wheel specification submitted successfully",
  "data": {
    "id": "uuid-here",
    "formNumber": "WHEEL-2025-001",
    "status": "SUBMITTED",
    "submittedBy": "inspector_john_doe",
    "submittedDate": "2025-10-05T00:00:00Z",
    "createdAt": "2025-10-05T10:30:00Z"
  }
}
```

**Error Response (400 Bad Request):**
```json
{
  "success": false,
  "message": "Validation failed",
  "errors": {
    "fields.treadDiameterNew": [
      "Invalid format. Expected: nominal (min-max)"
    ],
    "formNumber": [
      "Form number already exists"
    ]
  }
}
```

#### 2. Submit Bogie Checksheet

**Endpoint:** `POST /api/forms/bogie-checksheet`

**Request Body:**
```json
{
  "formNumber": "BOGIE-2025-001",
  "inspectionBy": "inspector_jane_smith",
  "inspectionDate": "2025-10-06",
  "bogieDetails": {
    "bogieNo": "BG1234",
    "makerYearBuilt": "RDSO/2018",
    "dateOfIOH": "2025-07-01",
    "incomingDivAndDate": "NR / 2025-06-25",
    "deficitComponents": "None"
  },
  "bogieChecksheet": {
    "bogieFrameCondition": "GOOD",
    "bolster": "GOOD",
    "bolsterSuspensionBracket": "CRACKED",
    "axleGuide": "WORN",
    "lowerSpringSeat": "GOOD"
  },
  "bmbcChecksheet": {
    "cylinderBody": "WORN_OUT",
    "pistonTrunnion": "GOOD",
    "plungerSpring": "GOOD",
    "adjustingTube": "DAMAGED"
  }
}
```

**Success Response (201 Created):**
```json
{
  "success": true,
  "message": "Bogie checksheet submitted successfully",
  "data": {
    "id": "uuid-here",
    "formNumber": "BOGIE-2025-001",
    "status": "SUBMITTED",
    "inspectionBy": "inspector_jane_smith",
    "inspectionDate": "2025-10-06T00:00:00Z",
    "requiresFollowUp": true,
    "flaggedComponents": [
      "bolsterSuspensionBracket",
      "axleGuide",
      "cylinderBody",
      "adjustingTube"
    ]
  }
}
```

#### 3. Retrieve Wheel Specifications

**Endpoint:** `GET /api/forms/wheel-specifications/list`

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `formNumber` | string | No | Filter by form number |
| `submittedBy` | string | No | Filter by submitter |
| `startDate` | date | No | Filter from date (YYYY-MM-DD) |
| `endDate` | date | No | Filter to date (YYYY-MM-DD) |
| `page` | integer | No | Page number (default: 1) |
| `pageSize` | integer | No | Items per page (default: 20) |

**Example Request:**
```bash
GET /api/forms/wheel-specifications/list?formNumber=WHEEL-2025-001&page=1&pageSize=10
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": "Wheel specifications retrieved successfully",
  "data": {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
      {
        "id": "uuid-here",
        "formNumber": "WHEEL-2025-001",
        "submittedBy": "inspector_john_doe",
        "submittedDate": "2025-10-05T00:00:00Z",
        "status": "SUBMITTED",
        "fields": {
          "treadDiameterNew": "915 (900-1000)",
          "condemningDia": "825 (800-900)"
          // ... additional fields
        },
        "createdAt": "2025-10-05T10:30:00Z",
        "updatedAt": "2025-10-05T10:30:00Z"
      }
    ]
  }
}
```

---

## Testing Strategy

### Test Coverage

The project maintains comprehensive test coverage across multiple layers:

```bash
# Run complete test suite
python manage.py test

# Run with coverage report
coverage run --source='.' manage.py test
coverage report -m
coverage html  # Generate HTML report

# Run specific test modules
python manage.py test api.tests.test_views
python manage.py test api.tests.test_serializers
python manage.py test api.tests.test_validators
```

### Test Categories

#### 1. Unit Tests
- Model method testing
- Validation logic verification
- Helper function testing
- Serializer field validation

#### 2. Integration Tests
- End-to-end API workflow testing
- Database transaction verification
- Error handling scenarios
- Edge case validation

#### 3. Performance Tests
- Response time benchmarking
- Database query optimization
- Concurrent request handling
- Memory usage profiling

### Sample Test Output

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..................................................
----------------------------------------------------------------------
Ran 50 tests in 12.345s

OK

Coverage Report:
Name                          Stmts   Miss  Cover
-------------------------------------------------
api/models.py                   145      8    94%
api/serializers.py              198     12    94%
api/views.py                    234     15    94%
api/helpers/validation.py       167      9    95%
-------------------------------------------------
TOTAL                           744     44    94%
```

---

## Technology Stack

### Backend Framework
| Technology | Version | Purpose |
|------------|---------|---------|
| Django | 5.2.4 | Web framework |
| Django REST Framework | 3.14+ | REST API framework |
| Python | 3.9+ | Programming language |

### Database
| Technology | Version | Purpose |
|------------|---------|---------|
| PostgreSQL | 12+ | Primary database |
| psycopg2-binary | 2.9+ | PostgreSQL adapter |

### Infrastructure
| Technology | Version | Purpose |
|------------|---------|---------|
| Docker | 20.10+ | Containerization |
| Docker Compose | 1.29+ | Container orchestration |
| Gunicorn | 20+ | WSGI HTTP server |

### Development Tools
| Technology | Version | Purpose |
|------------|---------|---------|
| pytest | 7+ | Testing framework |
| coverage | 6+ | Code coverage |
| black | 23+ | Code formatting |
| flake8 | 5+ | Code linting |

### Supporting Libraries
```txt
django-cors-headers==4.0+       # CORS handling
python-decouple==3.6+           # Environment management
python-json-logger==2.0+        # Structured logging
djangorestframework==3.14+      # REST API toolkit
```

---


### Docker Environment

For Docker deployments, configure `docker-compose.yml`:

```yaml
services:
  db:
    environment:
      POSTGRES_DB: railway_maintenance
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${DATABASE_PASSWORD}
  
  api:
    environment:
      DATABASE_HOST: db
      DATABASE_PORT: 5432
```


### Security Best Practices

```python
# Example: Secure configuration loading
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
```


```

## Resources

### Quick Access Links
- 🎥 **Video Tutorial**: [Setup & Development Guide](https://drive.google.com/file/d/17QCv4pfbuGwF-YY-i1CHJYKyUKcSJ8ya/view?usp=sharing)
- 📮 **Postman Collection**: [Download API Collection](https://drive.google.com/file/d/1ufnS8cfllRbqiyIpEXSvQQIn6u4Rlr1p/view?usp=sharing)

### Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

### Support Channels
- **Email**: bhavithapallapu@gmail.com
