#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DocumentMemento__Memento_

class TextDocument__Originator_(DocumentMemento__Memento_):
	def _init_(self):
		pass

	def add_text(self, aText):
		"""@ParamType aText String"""
		pass

	def delete_text(self, aLength):
		"""@ParamType aLength int"""
		pass

	def replace_text(self, aOld_text, aNew_text):
		"""@ParamType aOld_text String
		@ParamType aNew_text String"""
		pass

	def get_content(self):
		"""@ReturnType String"""
		pass

	def display(self):
		pass

	def save(self):
		"""@ReturnType DocumentMemento"""
		pass

	def restore(self, aMemento):
		"""@ParamType aMemento DocumentMemento"""
		pass

	def __init__(self):
		self.___content = None
		"""@AttributeType String"""

