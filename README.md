# Todoist-Rescheduler
Automatically reschedule overdue tasks in Todoist

## Configuration
Open `todoist-rescheduler.py` and set your API token at the top of the file

## Usage
Check your Python version and make sure version 3.7 or newer is installed on your system:
```
$ python3 --version
```

Install required python3 modules:
```
$ pip3 install todoist-python
```

Run the script at the end of the day to automatically reschedule any overdue tasks with the label `daily`, `weekly`, `monthly`, and `yearly` to the next day/week/month/year.

# License

Copyright (C) 2021 Sam Steele. Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
