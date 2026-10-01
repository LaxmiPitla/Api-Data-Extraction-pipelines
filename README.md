# API Data Extraction Pipeline

## Overview

This project demonstrates the extraction of data from REST APIs using Python.

The pipeline retrieves data from the DummyJSON API, handles paginated responses and nested JSON structures, extracts relevant fields, and stores the processed data in CSV format for further data engineering workflows.

## Tech Stack

* Python
* REST APIs
* `requests`
* Pandas
* JSON
* CSV
* Git & GitHub

## API Source

**DummyJSON** — a free REST API used for learning and testing data extraction workflows.

Endpoints used in this project:

* Products
* Carts
* Users

## Project Structure

```text
api_data_extraction_pipeline/
│
├── dummyjson/
│   ├── products.py
│   ├── carts.py
│   └── users.py
│
├── data/
│   └── *.csv
│
├── requirements.txt
└── README.md
```

## Data Extraction Workflow

```text
REST API
   ↓
HTTP Request
   ↓
JSON Response
   ↓
Pagination
   ↓
Nested JSON Processing
   ↓
Data Extraction
   ↓
Data Validation
   ↓
Pandas DataFrame
   ↓
CSV
```

## Key Features

### 1. API Data Extraction

Python's `requests` library is used to send HTTP GET requests and retrieve JSON data from the API.

### 2. Pagination

The extraction logic uses API pagination parameters such as `limit` and `skip` to retrieve data across multiple API responses instead of relying only on the default response size.

### 3. Nested JSON Handling

The project handles nested structures such as products contained within carts.

For example:

```text
Cart
 └── Products
      ├── Product 1
      ├── Product 2
      └── Product 3
```

The extraction logic preserves the relationship between the cart and its products using identifiers such as `cart_id` and `product_id`.

### 4. Data Validation

Extracted data is validated by checking:

* Number of records
* Column names
* Missing values
* Duplicate records
* Data types

### 5. CSV Output

The extracted data is converted into Pandas DataFrames and stored as CSV files for downstream processing.

## Example

A cart-product record is extracted into a tabular structure such as:

| cart_id | user_id | product_id | title              |   price | quantity |
| ------: | ------: | ---------: | ------------------ | ------: | -------: |
|       1 |       1 |        162 | Blue Frock         |   29.99 |        4 |
|       1 |       1 |        113 | Generic Motorcycle | 3999.99 |        3 |

## How to Run

Clone the repository:

```bash
git clone <repository-url>
cd api_data_extraction_pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run an extraction script:

```bash
python dummyjson/products.py
```

The extracted data will be saved as CSV files in the designated data directory.

## Future Enhancements

* Load extracted data into Snowflake
* Implement incremental API extraction
* Add logging and error handling
* Automate the extraction workflow
* Add data transformation and quality checks
* Build a Bronze → Silver → Gold data pipeline

## Purpose

This project is part of my Data Engineering portfolio and focuses on practical API ingestion concepts including REST APIs, pagination, nested JSON processing, data validation, and preparing data for downstream data warehouse loading.
