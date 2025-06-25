from runAiBot import connect_to_google_sheet, get_applied_job_ids
import unittest
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread

def test_google_sheet_connection():
    try:
        applied_sheet = connect_to_google_sheet('Applied')
        failed_sheet = connect_to_google_sheet('Failed')

        if applied_sheet:
            print("Successfully connected to 'Applied' sheet.")
        else:
            print("Failed to connect to 'Applied' sheet.")

        if failed_sheet:
            print("Successfully connected to 'Failed' sheet.")
        else:
            print("Failed to connect to 'Failed' sheet.")

    except Exception as e:
        print(f"Error during testing Google Sheets connection: {e}")

class TestGoogleSheets(unittest.TestCase):

    def test_connect_to_google_sheet(self):
        """Test connection to Google Sheets."""
        sheet_name = 'Applied'  # Replace with the actual sheet name
        sheet = connect_to_google_sheet(sheet_name)
        self.assertIsNotNone(sheet, "Failed to connect to Google Sheets")

    def test_get_applied_job_ids(self):
        """Test fetching applied job IDs from Google Sheets."""
        job_ids = get_applied_job_ids()
        self.assertIsInstance(job_ids, set, "Job IDs should be returned as a set")

    def test_google_sheets_update(self):
        # Google Sheets setup
        SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        CREDENTIALS_FILE = 'google-creds.json'

        # Connect to Google Sheets
        try:
            credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)
            client = gspread.authorize(credentials)
            sheet = client.open('Applied').sheet1

            # Test data
            job_id = '12345'
            title = 'Software Engineer'
            company = 'Tech Corp'
            work_location = 'Remote'
            work_style = 'Hybrid'
            description = 'Develop software solutions.'
            experience_required = '3 years'
            skills = ['Python', 'Django']
            hr_name = 'John Doe'
            hr_link = 'https://linkedin.com/in/johndoe'
            resume = 'default_resume.pdf'
            reposted = False
            date_listed = datetime.now().strftime('%Y-%m-%d')
            date_applied = datetime.now().strftime('%Y-%m-%d')
            job_link = 'https://linkedin.com/jobs/view/12345'
            application_link = 'Easy Applied'
            questions_list = {'What is your experience?': '3 years'}
            connect_request = 'Pending'

            # Append test data to Google Sheet
            row = [job_id, title, company, work_location, work_style, description, experience_required, skills, hr_name, hr_link, resume, reposted, date_listed, date_applied, job_link, application_link, questions_list, connect_request]
            sheet.append_row(row)

            print("Test data successfully written to Google Sheet.")
        except Exception as e:
            print(f"Failed to connect to Google Sheets or write data: {e}")

if __name__ == "__main__":
    test_google_sheet_connection()
    unittest.main()
