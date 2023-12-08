# i -*- coding: utf-8 -*-
# Copyright (C) 2007-2024   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
"""
  La classe CONNECTOR sert a enregistrer les observateurs d'objets et a delivrer
  les messages emis a ces objets.

  Le principe general est le suivant : un objet (subscriber) s'enregistre aupres du
  connecteur global (theconnector) pour observer un objet emetteur de messages (publisher)
  sur un canal donne (channel). Il demande a etre notifie par appel d'une fonction (listener).
  La sequence est donc :

     - enregistrement du subscriber pour le publisher : theconnector.Connect(publisher,channel,listener,args)
     - emission du message par le publisher : theconnector.Emit(publisher,channel,cargs)

  args et cargs sont des tuples contenant les arguments de la fonction listener qui sera appelee
  comme suit::

     listener(cargs+args)
"""
import traceback
from copy import copy
import weakref


class ConnectorError(Exception):
    pass


class CONNECTOR:
    def __init__(self):
        self.connections = {}

    def Connect(self, object, channel, function, args):
        # print ("Connect",object, channel, function, args)
        idx = id(object)
        # if self.connections.has_key(idx):
        if idx in self.connections:
            channels = self.connections[idx]
        else:
            channels = self.connections[idx] = {}

        # if channels.has_key(channel):
        if channel in channels:
            receivers = channels[channel]
        else:
            receivers = channels[channel] = []

        for funct, fargs in receivers[:]:
            if funct() is None:
                receivers.remove((funct, fargs))
            elif (function, args) == (funct(), fargs):
                receivers.remove((funct, fargs))

        receivers.append((ref(function), args))

    def Disconnect(self, object, channel, function, args):
        try:
            receivers = self.connections[id(object)][channel]
        except KeyError:
            raise ConnectorError(
                "no receivers for channel %s of %s" % (channel, object)
            )

        for funct, fargs in receivers[:]:
            if funct() is None:
                receivers.remove((funct, fargs))

        for funct, fargs in receivers:
            if (function, args) == (funct(), fargs):
                receivers.remove((funct, fargs))
                if not receivers:
                    # the list of receivers is empty now, remove the channel
                    channels = self.connections[id(object)]
                    del channels[channel]
                    if not channels:
                        # the object has no more channels
                        del self.connections[id(object)]
                return

        raise ConnectorError(
            "receiver %s%s is not connected to channel %s of %s"
            % (function, args, channel, object)
        )

    def Emit(self, object, channel, *args):
        # print "Emit",object, channel, args
        try:
            receivers = self.connections[id(object)][channel]
        except KeyError:
            return
        # print "Emit",object, channel, receivers
        # Attention : copie pour eviter les pbs lies aux deconnexion reconnexion
        # pendant l'execution des emit
        for rfunc, fargs in copy(receivers):
            try:
                func = rfunc()
                if func:
                    # print (func,args,fargs)
                    # rint args + fargs
                    # apply(func, args + fargs)
                    if args + fargs == ():
                        func()
                    else:
                        func(args + fargs)
                else:
                    # Le receveur a disparu
                    if (rfunc, fargs) in receivers:
                        receivers.remove((rfunc, fargs))
            except:
                traceback.print_exc()


def ref(target, callback=None):
    # if hasattr(target,"im_self"):
    #   return BoundMethodWeakref(target)
    if hasattr(target, "__self__"):
        return BoundMethodWeakref(target)
    else:
        return weakref.ref(target, callback)


class BoundMethodWeakref(object):
    def __init__(self, callable):
        # self.Self=weakref.ref(callable.im_self)
        # self.Func=weakref.ref(callable.im_func)
        self.Self = weakref.ref(callable.__self__)
        self.Func = weakref.ref(callable.__func__)

    def __call__(self):
        target = self.Self()
        if not target:
            return None
        func = self.Func()
        if func:
            return func.__get__(self.Self())


_the_connector = CONNECTOR()
Connect = _the_connector.Connect
Emit = _the_connector.Emit
Disconnect = _the_connector.Disconnect

if __name__ == "__main__":

    class A:
        pass

    class B:
        def add(self, a):
            print(("--------------------------------add ", self, a))

        def __del__(self):
            print(("__del__", self))

    def f(a):
        print((f, a))

    a = A()
    b = B()
    c = B()

    Connect(a, "add", b.add, ())
    Connect(a, "add", b.add, ())
    Connect(a, "add", c.add, ())
    Connect(a, "add", f, ())

    Emit(a, "add", 1)

    print("del b")
    del b

    Emit(a, "add", 1)
    print("del f")
    del f

    Emit(a, "add", 1)
    Disconnect(a, "add", c.add, ())
    Emit(a, "add", 1)
