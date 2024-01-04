#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

import cata5CChapeau_driver	 as mdm

fileName='/tmp/toto.xml'
jdd = mdm.CreateFromDocument(open(fileName).read())
print (jdd)
