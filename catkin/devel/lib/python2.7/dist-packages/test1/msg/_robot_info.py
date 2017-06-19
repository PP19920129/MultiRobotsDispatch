# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from test1/robot_info.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class robot_info(genpy.Message):
  _md5sum = "f7468c010c81fc0248bb003b9877aa15"
  _type = "test1/robot_info"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint16 Robot_Serial
uint16 Control_State
uint16 Robot_State
uint16 Robot_Position
uint16 Task_Type
uint16 Route_Serial
"""
  __slots__ = ['Robot_Serial','Control_State','Robot_State','Robot_Position','Task_Type','Route_Serial']
  _slot_types = ['uint16','uint16','uint16','uint16','uint16','uint16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Robot_Serial,Control_State,Robot_State,Robot_Position,Task_Type,Route_Serial

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(robot_info, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.Robot_Serial is None:
        self.Robot_Serial = 0
      if self.Control_State is None:
        self.Control_State = 0
      if self.Robot_State is None:
        self.Robot_State = 0
      if self.Robot_Position is None:
        self.Robot_Position = 0
      if self.Task_Type is None:
        self.Task_Type = 0
      if self.Route_Serial is None:
        self.Route_Serial = 0
    else:
      self.Robot_Serial = 0
      self.Control_State = 0
      self.Robot_State = 0
      self.Robot_Position = 0
      self.Task_Type = 0
      self.Route_Serial = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6H().pack(_x.Robot_Serial, _x.Control_State, _x.Robot_State, _x.Robot_Position, _x.Task_Type, _x.Route_Serial))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.Robot_Serial, _x.Control_State, _x.Robot_State, _x.Robot_Position, _x.Task_Type, _x.Route_Serial,) = _get_struct_6H().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6H().pack(_x.Robot_Serial, _x.Control_State, _x.Robot_State, _x.Robot_Position, _x.Task_Type, _x.Route_Serial))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.Robot_Serial, _x.Control_State, _x.Robot_State, _x.Robot_Position, _x.Task_Type, _x.Route_Serial,) = _get_struct_6H().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6H = None
def _get_struct_6H():
    global _struct_6H
    if _struct_6H is None:
        _struct_6H = struct.Struct("<6H")
    return _struct_6H