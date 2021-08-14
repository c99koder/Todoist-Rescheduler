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
from datetime import datetime, date, timedelta
from todoist.api import TodoistAPI

TODOIST_ACCESS_TOKEN = '' #At the bottom of Settings > Integrations in the web/desktop app

if len(sys.argv) != 2:
	print("Usage: " + sys.argv[0] + " label")
	sys.exit(0)

def find_label_id(label):
	for l in api.state['labels']:
		if l['name'] == label:
			return l['id']
	return None

def find_items_by_label_id(label_id):
	items = []
	for i in api.state['items']:
		for l in i['labels']:
			if l == label_id:
				items.append(i)

	return items

def reschedule_label(label):
	items = find_items_by_label_id(find_label_id(label))
	for item in items:
		due = item['due']
		date = datetime.fromisoformat(due['date'])
		if date < datetime.now():
			print("Overdue (" + label + "): " + str(date) + " - " + item['content'])
			item.update(due={'string': due['string']})

api = TodoistAPI(TODOIST_ACCESS_TOKEN)
api.sync()

reschedule_label(sys.argv[1])

api.commit()