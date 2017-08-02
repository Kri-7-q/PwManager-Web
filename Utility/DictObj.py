from flask import Markup

class DictObj(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    # Get the HTML-Attribute for AngularJS Application.
    def angularApp(self):
        if 'ngApp' in self:
            return Markup(' ng-app="{}"'.format(self['ngApp']))
        else:
            return None

    # Get the HTML-Attribute for AngularJS Controller.
    def angularCtrl(self):
        if 'ngCtrl' in self:
            return Markup(' ng-controller="{}"'.format(self['ngCtrl']))
        else:
            return None