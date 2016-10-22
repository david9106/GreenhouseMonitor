# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

from twilio import twiml
from twilio.rest import Client

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        # replace with your credentials from: https://www.twilio.com/user/account
        account_sid = "AC0b80488af39dcd381ac952934507ef69"
        auth_token = "617ce805fc5a06c6aabc9e3aaf3549bf"

        client = Client(account_sid, auth_token)
        # replace "to" and "from_" with real numbers
        rv = client.messages.create(to="+526645380095",
                                    from_="+16179970349 ",
                                    body="Hello Monkey!")
        self.response.write(str(rv))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)