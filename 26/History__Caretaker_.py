#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DocumentMemento__Memento_

class History__Caretaker_(DocumentMemento__Memento_):
	def __init__(self, aDocument, aMax_history_size = 10):
		"""@ParamType aDocument TextDocument
		@ParamType aMax_history_size int"""
		self.___document = None
		"""@AttributeType TextDocument"""
		self.___mementos = None
		"""@AttributeType List"""
		self.___max_history_size = None
		"""@AttributeType int"""
		self.___current_index = None
		"""@AttributeType int"""

	def backup(self):
		pass

	def undo(self):
		"""@ReturnType boolean"""
		pass

	def redo(self):
		"""@ReturnType boolean"""
		pass

	def show_history(self):
		pass

