# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import deserialize
from twilio import values
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page


class NotificationList(ListResource):

    def __init__(self, version, service_sid):
        """
        Initialize the NotificationList
        
        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        
        :returns: NotificationList
        :rtype: NotificationList
        """
        super(NotificationList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'service_sid': service_sid,
        }
        self._uri = '/Services/{service_sid}/Notifications'.format(**self._solution)

    def create(self, identity=values.unset, tag=values.unset, body=values.unset,
               priority=values.unset, ttl=values.unset, title=values.unset,
               sound=values.unset, action=values.unset, data=values.unset,
               apn=values.unset, gcm=values.unset, sms=values.unset,
               facebook_messenger=values.unset):
        """
        Create a new NotificationInstance
        
        :param unicode identity: The identity
        :param unicode tag: The tag
        :param unicode body: The body
        :param notification.priority priority: The priority
        :param unicode ttl: The ttl
        :param unicode title: The title
        :param unicode sound: The sound
        :param unicode action: The action
        :param unicode data: The data
        :param unicode apn: The apn
        :param unicode gcm: The gcm
        :param unicode sms: The sms
        :param dict facebook_messenger: The facebook_messenger
        
        :returns: Newly created NotificationInstance
        :rtype: NotificationInstance
        """
        data = values.of({
            'Identity': identity,
            'Tag': tag,
            'Body': body,
            'Priority': priority,
            'Ttl': ttl,
            'Title': title,
            'Sound': sound,
            'Action': action,
            'Data': data,
            'Apn': apn,
            'Gcm': gcm,
            'Sms': sms,
            'FacebookMessenger': facebook_messenger,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return NotificationInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notifications.V1.NotificationList>'


class NotificationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the NotificationPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid
        
        :returns: NotificationPage
        :rtype: NotificationPage
        """
        super(NotificationPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NotificationInstance
        
        :param dict payload: Payload response from the API
        
        :returns: NotificationInstance
        :rtype: NotificationInstance
        """
        return NotificationInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notifications.V1.NotificationPage>'


class NotificationInstance(InstanceResource):

    def __init__(self, version, payload, service_sid):
        """
        Initialize the NotificationInstance
        
        :returns: NotificationInstance
        :rtype: NotificationInstance
        """
        super(NotificationInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'identities': payload['identities'],
            'tags': payload['tags'],
            'priority': payload['priority'],
            'ttl': deserialize.integer(payload['ttl']),
            'title': payload['title'],
            'body': payload['body'],
            'sound': payload['sound'],
            'action': payload['action'],
            'data': payload['data'],
            'apn': payload['apn'],
            'gcm': payload['gcm'],
            'sms': payload['sms'],
            'facebook_messenger': payload['facebook_messenger'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
        }

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def identities(self):
        """
        :returns: The identities
        :rtype: unicode
        """
        return self._properties['identities']

    @property
    def tags(self):
        """
        :returns: The tags
        :rtype: unicode
        """
        return self._properties['tags']

    @property
    def priority(self):
        """
        :returns: The priority
        :rtype: notification.priority
        """
        return self._properties['priority']

    @property
    def ttl(self):
        """
        :returns: The ttl
        :rtype: unicode
        """
        return self._properties['ttl']

    @property
    def title(self):
        """
        :returns: The title
        :rtype: unicode
        """
        return self._properties['title']

    @property
    def body(self):
        """
        :returns: The body
        :rtype: unicode
        """
        return self._properties['body']

    @property
    def sound(self):
        """
        :returns: The sound
        :rtype: unicode
        """
        return self._properties['sound']

    @property
    def action(self):
        """
        :returns: The action
        :rtype: unicode
        """
        return self._properties['action']

    @property
    def data(self):
        """
        :returns: The data
        :rtype: dict
        """
        return self._properties['data']

    @property
    def apn(self):
        """
        :returns: The apn
        :rtype: dict
        """
        return self._properties['apn']

    @property
    def gcm(self):
        """
        :returns: The gcm
        :rtype: dict
        """
        return self._properties['gcm']

    @property
    def sms(self):
        """
        :returns: The sms
        :rtype: dict
        """
        return self._properties['sms']

    @property
    def facebook_messenger(self):
        """
        :returns: The facebook_messenger
        :rtype: dict
        """
        return self._properties['facebook_messenger']

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notifications.V1.NotificationInstance>'
