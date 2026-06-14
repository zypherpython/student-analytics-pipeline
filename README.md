# 🎓 Student Analytics Pipeline with SQL Practice

> *Master Data Processing & SQL through Building a Real Extract-Transform-Load Pipeline*

---

## 📊 Project Overview

Welcome to the **Student Analytics Pipeline** project! This is a comprehensive learning initiative focused on building a robust data pipeline combining **Extract → Transform → Load (ETL)** with **PostgreSQL database practice**.

This project combines data processing with **real-world SQL operations**, using **psycopg** to manage connections and practice database operations through Python.

### 🎯 Project Status: ✅ PHASE 1 COMPLETE

✅ **Extract Phase (COMPLETED)**
- Successfully implemented robust CSV data extraction
- Enhanced error handling and data validation
- UTF-8 encoding support and detailed logging
- Scalable record ingestion from 100+ student records

✅ **Transform Phase (COMPLETED)** 
- Robust data cleaning and normalization pipeline
- Duplicate record detection and removal
- Data validation with grade range checks (0-100)
- Missing value handling for critical fields
- Student name normalization to title case
- Comprehensive reporting on data quality improvements

✅ **SQL Load Phase (COMPLETED)**
- PostgreSQL database integration using **psycopg2**
- Complete ETL pipeline with database persistence
- Data insertion with error handling
- Transaction management and connection handling
- Full end-to-end pipeline execution

🔮 **Future Enhancements (PLANNED)**
- Advanced SQL queries and analytics
- Data visualization dashboards
- Unit tests and CI/CD pipeline
- Performance optimization and indexing
- Additional datasets and use cases

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL Database (local or remote)
- **psycopg2** - PostgreSQL adapter for Python
- Required Python packages (see `requirements.txt`)

### Installation

```bash
# Clone the repository
git clone https://github.com/zypherpython/student-analytics-pipeline.git
cd student-analytics-pipeline

# Install dependencies
pip install -r requirements.txt

# Make sure PostgreSQL is running on your system
```

### Quick Start - Complete Pipeline

```python
from load import extract, transform, load, main

# Run the complete ETL pipeline
main()
```

Or step-by-step:

```python
from load import extract, transform, load

# Step 1: Extract data from CSV
data = extract('data/messy_students_100.csv')
print(f"Extracted {len(data)} records")

# Step 2: Transform and clean data
clean_data = transform(data)
print(f"Cleaned {len(clean_data)} records")

# Step 3: Load to PostgreSQL database
load(clean_data)
```

### Database Setup

Before running the pipeline, create the PostgreSQL database and table:

```sql
-- Create database
CREATE DATABASE STUDENT_ANALYSIS;

-- Create students table
CREATE TABLE students (
    ID INT PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL,
    AGE INT NOT NULL,
    COURSE VARCHAR(50),
    GRADE INT NOT NULL CHECK (GRADE >= 0 AND GRADE <= 100)
);
```

---

## 📁 Project Structure

```
student-analytics-pipeline/
├── load.py                          # Complete ETL pipeline (extract, transform, load)
├── data/
│   └── messy_students_100.csv       # Sample dataset with 100 messy student records
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
└── .gitignore                       # Git ignore rules
```

---

## 🔧 Features & Capabilities

### Extract Phase ✨
- **CSV Data Ingestion**: Robust extraction from CSV files
- **UTF-8 Encoding**: Proper character encoding support
- **Error Handling**: Graceful handling of missing files
- **DictReader**: Convenient field-based access to records

### Transform Phase ⚙️
- **Duplicate Detection**: Identifies and removes duplicate records
- **Data Validation**: Ensures grade values are within 0-100 range
- **Missing Value Handling**: Removes records with missing critical fields (age)
- **Data Normalization**: Converts student names to title case
- **Quality Reporting**: Detailed metrics on records removed

### Load Phase 🗄️ (with psycopg)
- **PostgreSQL Integration**: Direct database connection via psycopg2
- **Batch Data Loading**: Efficient insertion of cleaned records
- **Error Handling**: Graceful error management and reporting
- **Transaction Management**: Proper commit/rollback handling
- **Connection Management**: Clean connection lifecycle

---

## 💻 Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Data Input** | CSV | Messy source data format |
| **Processing** | Python 3.8+ | Data transformation and orchestration |
| **Database** | PostgreSQL | Persistent data storage |
| **DB Driver** | psycopg2 | Python ↔ PostgreSQL communication |

---

## 📊 Sample Dataset

The project includes **`messy_students_100.csv`** with 100 student records containing:
- **Duplicates**: Same student appearing multiple times
- **Invalid Grades**: Grades > 100 (e.g., 150)
- **Missing Values**: Empty AGE or COURSE fields
- **Case Inconsistencies**: Names in different cases (JOHN, john, John)

This demonstrates real-world data quality challenges! ✨

---

## 📚 Learning Journey

This project is a **comprehensive learning initiative** exploring:
- **Data Extraction**: Reading and parsing CSV files efficiently
- **Data Transformation**: Cleaning, validating, and normalizing data
- **Data Loading**: Inserting data into relational databases
- **Python-SQL Integration**: Using psycopg to bridge Python and PostgreSQL
- **Database Design**: Creating and managing database schemas
- **Error Handling**: Robust handling of edge cases and failures
- **ETL Best Practices**: Industry-standard pipeline patterns

> **Project Philosophy**: Learn data engineering by building something real! From messy CSV to clean database - that's the journey.

---

## 🚀 What's Next?

### Future Enhancements
We're planning to add more exciting features:

1. **Advanced Analytics**
   - SQL queries for grade analysis
   - Course-wise performance metrics
   - Student ranking and statistics

2. **Data Visualization**
   - Dashboard with matplotlib/plotly
   - Grade distribution charts
   - Course performance graphs

3. **Quality Improvements**
   - Unit tests for each phase
   - Integration tests
   - Performance benchmarking

4. **Scalability**
   - Batch processing for larger datasets
   - Database indexing and optimization
   - Connection pooling

5. **Additional Datasets**
   - Multiple source systems
   - Different data formats (JSON, Excel)
   - Real-time data ingestion

---

## 🤝 Contributing & Feedback

👉 **We're building this together!** If you have:
- 💡 Suggestions for improvements
- 🐛 Bug reports
- 📖 Documentation improvements
- 🎯 Feature ideas
- 🧪 Test cases or edge cases to handle

...please feel free to:
1. Open an issue
2. Submit a pull request
3. Reach out with feedback

---

## Acknowledgments

| Contributor | Role |
|-------------|------|
| zypherpython | Project Lead & Developer |
| Copilot | Documentation & Code Structure |

---

## 📝 License

This project is open source and available under the MIT License - see the LICENSE file for details.

---

<div align="center">
  <strong>🎓 Learn Data Engineering Through Practice! 🚀</strong>
  <br/>
  <i>Extract once, Transform always, Load to the database</i>
  <br/>
  <br/>
  <strong>Stay tuned for more exciting features & improvements!</strong>
</div>
