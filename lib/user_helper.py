import urllib
import urllib2
from utils import Utils


class UserAPI(object):
    uri = "https://jsonplaceholder.typicode.com/users"

    #  Get all users
    def request_user_list(self):
        return Utils.get_data_in_json(urllib2.urlopen(self.uri))

    # Find user by username
    def request_user_by_username(self, username):
        url = self.uri+"?username=%s" % username
        response = urllib2.urlopen(url)
        return Utils.get_data_in_json(response)

    # Create new user
    def request_create_user(self, user):
        request = urllib2.Request(self.uri)
        request.add_data(urllib.urlencode(user))
        return urllib2.urlopen(request)

    # Update user
    def request_update_user(self, user_id, data):
        request = urllib2.Request(self.uri + "/%s" % user_id)
        request.get_method = lambda: 'PATCH'
        request.add_data(urllib.urlencode(data))
        response = urllib2.urlopen(request)
        return response

    # Delete user
    def request_delete_user(self, user_id):
        request = urllib2.Request(self.uri+"/%s" %user_id)
        request.get_method = lambda: 'DELETE'
        response = urllib2.urlopen(request)
        return response

