#cpe-api-project  

Overview  

CPE Data Collection and RESTful API  

This project is designed to parse the public Common Platform Enumeration (CPE) dictionary XML feed, extract essential CPE information, store the structured data in a SQLite database, and expose it through a Flask-based RESTful API. The goal is to provide searchable access to structured CPE data for use in cybersecurity tools, vulnerability assessment workflows, or research applications.

The repository includes:  
CPE Parser and Loader: Parses the official NIST CPE XML file and extracts key attributes including CPE 2.2 URI, CPE 2.3 URI, titles, deprecated status, and references. Parsed data is loaded into a relational SQLite database.

Database Schema: A normalized schema supporting efficient lookups and optional relationships between CPEs, references, and titles.

Flask-based REST API: A modular and extensible RESTful API built using Flask, supporting query parameters such as CPE URI or title keywords. Responses are returned in JSON and support pagination for large datasets.

Frontend Interface (Partially Implemented): A React-based frontend was started to enable searching CPE entries through a simple interface. The frontend is not fully complete and does not fully meet all the project requirements; however, it successfully returns results for many valid search inputs and demonstrates functional integration with the backend API.

Features:  
XML parsing and preprocessing with deduplication and integrity checks

SQLite-backed persistent storage

RESTful endpoints with filters for:

cpe_22_uri

cpe_23_uri

title keyword matching

Pagination via page and limit query parameters

JSON responses suitable for frontend integration or programmatic access

Lightweight React-based UI prototype

Limitations:  
The frontend UI is incomplete and does not support all filtering or pagination features as originally planned. Some search queries may return expected results, while others may fail silently or not reflect accurate feedback due to limited input validation and missing error handling.

The project currently uses SQLite, which is ideal for small-scale development and testing but may not be suitable for production-scale data ingestion from the full CPE dictionary.

Search filtering may be basic and does not currently support complex query chaining (e.g., combining filters with AND/OR logic).

Purpose:  
This project was created to demonstrate the full pipeline of ingesting structured cybersecurity data, transforming it into a usable relational format, and exposing it through a web API that supports interaction via both code and a UI. It is a flexible foundation that could be extended with:

Full CRUD operations  

Caching and performance improvements  

Integration with CVE databases for vulnerability mapping  

Dockerized deployment or cloud integration


