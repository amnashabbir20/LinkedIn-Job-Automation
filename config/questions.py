'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "C:\\Users\\ashfa\\OneDrive\\Desktop\\Resume (Baber Aabk).pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "8"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = ""                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/baber-aabk-812610370/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "U.S. Citizen/Permanent Resident"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 135000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 135000           # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 14                  # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Full Stack Developer with bachelors in Computer Science and 8+ years of experience" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
I'm a Senior Software Engineer with Bachelors in CS and 8+ years of experience in developing and maintaining Full Stack Web applications. 
Specialized in Mern and Python.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I am writing to express my interest in this position at your company. With over 8 years of experience as a Senior Python and MERN Stack Developer, I have built scalable web applications in healthcare, fintech, and AI. My expertise includes Python, JavaScript (ES6+), TypeScript, Django, Flask, React, Node.js, Express.js, Next.js, and cloud technologies such as AWS and Docker.

Throughout my career, I have led backend architecture, optimized databases for high performance, and collaborated with AI/ML teams to deliver innovative solutions. I am passionate about aligning technology with business needs and driving product innovation.

I am confident that my technical skills and dedication to excellence will make a valuable contribution to your company. Thank you for considering my application. I look forward to the opportunity to contribute to your team.

Best regards,
Baber Aabk
"""
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all = """
Name: Baber Aabk
Email: babaraabk@gmail.com
LinkedIn: https://www.linkedin.com/in/baber-aabk-812610370/
Location: United States

Professional Summary:
Senior Python and MERN Stack Developer with 8+ years of experience in building scalable web applications in healthcare, fintech, and AI. Proficient in Python, JavaScript (ES6+), and TypeScript, with a strong focus on cloud technologies, microservices, and Agile practices. Experienced in aligning tech solutions with business needs and driving product innovation.

Core Competencies:
- Languages: Python, JavaScript (ES6+), TypeScript
- Frameworks: Django, Flask, React, Node.js, Express.js, Next.js
- Databases: PostgreSQL, MongoDB, MySQL
- Cloud & DevOps: AWS, Firebase, Docker, Kubernetes, Prometheus, Grafana
- Tools: Git, Jenkins, CircleCI, Jira, Trello
- Other Skills: REST APIs, GraphQL, CI/CD, Microservices, Agile Development, Testing (PyTest, Jest)

Certifications:
- AWS Certified Cloud Practitioner
- FreeCodeCamp Certifications
- Advanced Python (Udemy)

Desired Salary: $135,000 per annum

Professional Experience:
1. Senior Python Developer, SeeWithin (2022–2024)
   - Developed HIPAA-compliant backend for AI-driven healthcare automation.
   - Optimized PostgreSQL databases for high availability and performance.
   - Worked closely with AI/ML teams to enhance features with React.
   - Integrated AWS, Docker, and Prometheus for optimized deployment and monitoring.
2. Senior MERN Stack Developer, Nike (2021–2022)
   - Led backend architecture using Node.js and integrated real-time data pipelines for reporting.
   - Migrated to microservices, improving scalability and system reliability.
3. Senior Python Developer, GoIdentify (2019–2021)
   - Built an AI-powered financial query bot with NLP.
   - Created Streamlit dashboards for real-time data visualization.
   - Integrated Prometheus for continuous performance monitoring.
4. Senior MERN Stack Developer, UX Pilot (2018–2019)
   - Led migration from React to Next.js for better performance and SEO.
   - Developed scalable backend APIs using Node.js and Firebase.
5. Python Developer, BaseOperation (2015–2018)
   - Built AI-powered dashboards and real-time collaboration tools.
   - Developed reusable data processing workflows, enhancing efficiency.

Education:
Bachelor of Computer Science, Johnson County Community College – Overland Park, Kansas, USA (Graduated: 2014)

Technical Tools:
- Version Control: Git, GitHub
- CI/CD: Jenkins, CircleCI
- Project Management: Jira, Trello
- Testing: PyTest, Jest
"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "Not Applicable" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "8"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = True # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''
############################################################################################################