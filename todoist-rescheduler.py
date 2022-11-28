#!/usr/bin/python3

#  Copyright (C) 2021 Sam Steele
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
from datetime import datetime
from todoist_api_python.api import TodoistAPI

TODOIST_ACCESS_TOKEN = '' #At the bottom of Settings > Integrations in the web/desktop app

if len(sys.argv) != 2:
	print("Usage: " + sys.argv[0] + " label")
	sys.exit(0)

def reschedule_label(label):
	items = api.get_tasks(label=label)
	for item in items:
		date = item.due.datetime
		if date is None:
			date = item.due.date
		if datetime.fromisoformat(date) < datetime.now():
			print("Overdue (" + label + "): " + date + " - " + item.content)
			api.update_task(task_id=item.id, due_string=item.due.string)

api = TodoistAPI(TODOIST_ACCESS_TOKEN)

reschedule_label(sys.argv[1])
