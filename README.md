# TeamsTextMessenger
Automated message sender using Selenium Python
- Webdriver now only works for Google Chrome for now

## What does this do?
1. Auto login into Microsoft Teams with *credentials* provided. 
2. Navigate to chat panel of the application.
3. Search for receiver of message.
4. Send the following *message* to the receiver.

## How to set up the program
1. Create a `info.json` file.
2. Fill in info into json file created based on the format shown in code block below.
3. Run `py main.py`.
```json
{
  "credentials" :
  {
    "email" : "TP012345@mail.apu.edu.my",
    "password" : "123456"
  },
  
  "message_info":
  {
    "intake_code" : "ABC1234",
    "survey_type" : "online survey",
    "survey_topic": "What are the factors influencing students' academic performance",
    "course_type" : "Foundation",
    "course_name" : "ABC",
    "form_link" : "https://www.abc12345.com/"
  },

  "receivers" :
  {
    "start_tp": "061200",
    "end_tp": "061205"
  }
}
```

### Message structure
Hey, my group and I from `intake_code` `course_type` are currently conducting an `survey_type` for our `course_name` assignment\
We would appreciate the help of yours at spending a short 5 mins to fill up the survey about `survey_topic`.\
Much appreciated! Thank you in advance and have a great day! `form_link` "


