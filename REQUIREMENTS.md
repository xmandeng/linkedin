
# Business Requirement Document (BRD)

## 1. Introduction
**Objective**: Develop a Minimum Viable Product (MVP) that scrapes compliance job listings from LinkedIn, compiles the results, and presents them in an HTML report to be reviewed by a human. The system is intended to be a proof-of-concept with the potential for expansion based on user feedback.

## 2. Business Requirements

### Job Scraping Functionality
- The system shall scrape job listings specifically related to compliance from LinkedIn.
- The system shall allow for the retrieval of a list of 30-50 job listings per search session.
- The system shall present the scraped job listings in a structured format (e.g., title, company name, job description, and link to the original listing).

### User Interaction
- The system shall provide the compiled job listings to a human reviewer for evaluation.
- The system shall facilitate easy review and feedback by allowing the reviewer to mark job listings as relevant or irrelevant.
- The system shall not proceed to automated posting; the workflow ends with the generation of the report and handoff to the human reviewer.

### Report Generation
- The system shall generate an HTML report of the compiled job listings.
- The HTML report shall be structured for easy review, with job titles, company names, brief descriptions, and links displayed clearly.

### Internal Web Server
- The system shall include a small web server to host the generated HTML reports internally.
- The web server shall be accessible only to authorized users within the organization.

### Security
- The system shall ensure that all data scraped and stored is handled according to standard data privacy guidelines.
- The web server shall be configured to restrict access to authorized personnel only.

## 3. Technical Requirements

### Technology Stack
- The MVP shall be developed using a web scraping tool compatible with LinkedIn's data structure (e.g., Python with Beautiful Soup or Scrapy).
- The HTML report generation shall be handled using a lightweight HTML templating system.
- The internal web server shall be set up using a simple framework such as Flask or Django (if using Python).

### System Performance
- The system shall be capable of scraping up to 50 job listings within a time frame of 5-10 minutes per search.
- The system shall generate the HTML report and host it on the internal web server within 1-2 minutes after scraping.

### Scalability
- The system architecture shall allow for easy expansion to include additional job platforms after the MVP stage.
- The codebase shall be modular, making it straightforward to add new filters (e.g., salary, geography) based on user feedback.

### Logging and Monitoring
- The system shall log all scraping activities and report generation processes for auditing purposes.
- The system shall include basic monitoring to ensure the web server is operational and accessible.

## 4. KPIs (Key Performance Indicators)

| KPI Name               | Description                                                   | Calculation Method                                                 |
|------------------------|---------------------------------------------------------------|--------------------------------------------------------------------|
| Scraping Success Rate   | The percentage of successful job scrapes compared to the total attempts | (Number of successful scrapes / Total scrapes) * 100                |
| Report Generation Time  | The average time taken to generate the HTML report after scraping | Total report generation time / Number of reports generated          |
| User Review Time        | The average time taken by the human reviewer to assess the report | Total review time / Number of reports reviewed                      |
| System Uptime           | The percentage of time the web server is operational          | (Uptime hours / Total hours in a period) * 100                      |

## 5. Acceptance Criteria

### Job Scraping
- The system must successfully scrape at least 90% of relevant job listings during each search session.
- The system must correctly format and present all relevant job details in the HTML report.

### HTML Report
- The generated HTML report must be fully functional and accessible via the internal web server.
- The report must be clear, easy to navigate, and contain all necessary job information.

### Web Server
- The internal web server must be operational at least 99% of the time during the MVP testing period.
- Access to the web server must be restricted to authorized users only.

### Security
- The system must adhere to all relevant data privacy guidelines, ensuring no unauthorized data leakage or access.
