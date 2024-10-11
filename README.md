# PDF Template Generator

This project generates a PDF document from a CSV file containing topics. Each topic is displayed on a separate page, with a header, footers, and lines for organization.
Features

    Read topics and page numbers from a CSV file.
    Generate a PDF with each topic on a separate page.
    Customizable formatting for the header, footer, and content lines.

Prerequisites

Before running the application, ensure you have the following installed:

    Python 3.x
    fpdf library
    pandas library

Installation

You can install the necessary Python libraries using pip:

bash

pip install fpdf pandas

Files
1. pdf_generator.py

This file contains the main functionality for generating a PDF from a CSV file.
Key Functions:

    Reads data from a CSV file (topics.csv).
    Creates a PDF document with the following structure:
        Header: Displays the topic name in bold.
        Lines: Horizontal lines throughout the page for visual separation.
        Footer: Displays the topic name at the bottom of each page.

2. topics.csv

This is a sample CSV file that contains the topics and the number of pages for each topic. The expected format is as follows:

Topic,Pages
Topic 1,3
Topic 2,2
Topic 3,5

Usage

    Create a CSV file named topics.csv in the same directory with the format mentioned above.
    Run the PDF generator script:

    bash

    python pdf_generator.py

    The output PDF will be saved as output.pdf in the same directory.

Example Output

    The generated output.pdf will have each topic on a separate page with a header and footer, along with lines to enhance readability.
