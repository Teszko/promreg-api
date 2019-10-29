""" Prometheus Registration Python Client
    Check https://intern.gitlab.tu-berlin.de/hpc/promreg-api for more information.
"""

import requests
import json


class PromRegApi:
    def __init__(self, hostname, token, protocol="http", port=12321, basepath="targets/", comment="added by promregapi"
                 , session=None):
        self.url = "{}://{}:{}/".format(protocol, hostname, port)
        self.token = token
        self.basepath = basepath
        self.comment = comment
        self._session = session or requests.Session()

    def _request(self, method, path, data=None):
        req_url = self.url + self.basepath + path
        headers = {'AuthToken': self.token}
        resp = self._session.request(method, req_url, headers=headers, data=json.dumps(data))

        if 400 <= resp.status_code:
            resp.raise_for_status()
        return resp

    def get(self, uri=""):
        """ get target if already registered with Prometheus
            Registration Returns all targets if called without
            parameter

        :param uri: hostname or ip and port of target.
        :return: target information or None if no target found
        """
        return self._request("GET", uri).json()

    def register(self, target, labels=None, comment=None):
        """ registers target with Prometheus Registration

        :param target: the hostname or ip and port of target
        :param labels: prometheus labels
        :param comment: comment describing this target
        :return: the return value of http call
        """
        if comment is None:
            comment = self.comment
        data = {'comment': comment, 'labels': labels}
        return self._request("POST", target, data)

    def delete(self, target):
        """ remove a target that's already registered with
            Prometheus Registration

        :param target: the hostname or ip and port of target
        :return: the return value of http call
        """
        return self._request("DELETE", target)

    def update(self, target, comment=None, labels=None):
        """ update comment and labels of target

        :param target: the hostname or ip and port of target
        :param comment: comment describing this target
        :param labels: prometheus labels
        :return: the return value of http call
        """
        if comment is None:
            comment = self.comment
        data = {'comment': comment, 'labels': labels}
        return self._request("PUT", target, data)
