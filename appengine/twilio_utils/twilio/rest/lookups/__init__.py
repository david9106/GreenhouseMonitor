# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.domain import Domain
from twilio.rest.lookups.v1 import V1


class Lookups(Domain):

    def __init__(self, twilio):
        """
        Initialize the Lookups Domain
        
        :returns: Domain for Lookups
        :rtype: Lookups
        """
        super(Lookups, self).__init__(twilio)
        
        self.base_url = 'https://lookups.twilio.com'
        
        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of lookups
        :rtype: V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def phone_numbers(self):
        """
        :rtype: PhoneNumberList
        """
        return self.v1.phone_numbers

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Lookups>'
