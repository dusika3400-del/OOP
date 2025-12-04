#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class DocumentMemento__Memento_(object):
	__metaclass__ = ABCMeta
	@classmethod
	def __init__(self, aContent):
		"""@ParamType aContent String"""
		self.___content = None
		"""@AttributeType String"""
		self.___timestamp = None
		"""@AttributeType DateTime"""

	@classmethod
	def get_content(self):
		"""@ReturnType String"""
		pass

	@classmethod
	def get_timestamp(self):
		"""@ReturnType String"""
		pass

	@classmethod
	def get_info(self):
		"""@ReturnType String"""
		pass

