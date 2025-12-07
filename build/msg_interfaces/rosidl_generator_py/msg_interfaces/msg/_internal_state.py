# generated from rosidl_generator_py/resource/_idl.py.em
# with input from msg_interfaces:msg/InternalState.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_InternalState(type):
    """Metaclass of message 'InternalState'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('msg_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'msg_interfaces.msg.InternalState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__internal_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__internal_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__internal_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__internal_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__internal_state

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class InternalState(metaclass=Metaclass_InternalState):
    """Message class 'InternalState'."""

    __slots__ = [
        '_header',
        '_id',
        '_v',
        '_d',
        '_e',
        '_de',
        '_given_position_lat',
        '_given_position_lon',
        '_starting_position_lat',
        '_starting_position_lon',
        '_left_thrust',
        '_right_thrust',
        '_given_azimuth',
        '_current_azimuth',
        '_distance',
        '_p_los',
        '_i_los',
        '_kp_los',
        '_ki_los',
        '_yaw_vel',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'id': 'int32',
        'v': 'float',
        'd': 'float',
        'e': 'float',
        'de': 'float',
        'given_position_lat': 'double',
        'given_position_lon': 'double',
        'starting_position_lat': 'double',
        'starting_position_lon': 'double',
        'left_thrust': 'float',
        'right_thrust': 'float',
        'given_azimuth': 'float',
        'current_azimuth': 'float',
        'distance': 'float',
        'p_los': 'float',
        'i_los': 'float',
        'kp_los': 'float',
        'ki_los': 'float',
        'yaw_vel': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.id = kwargs.get('id', int())
        self.v = kwargs.get('v', float())
        self.d = kwargs.get('d', float())
        self.e = kwargs.get('e', float())
        self.de = kwargs.get('de', float())
        self.given_position_lat = kwargs.get('given_position_lat', float())
        self.given_position_lon = kwargs.get('given_position_lon', float())
        self.starting_position_lat = kwargs.get('starting_position_lat', float())
        self.starting_position_lon = kwargs.get('starting_position_lon', float())
        self.left_thrust = kwargs.get('left_thrust', float())
        self.right_thrust = kwargs.get('right_thrust', float())
        self.given_azimuth = kwargs.get('given_azimuth', float())
        self.current_azimuth = kwargs.get('current_azimuth', float())
        self.distance = kwargs.get('distance', float())
        self.p_los = kwargs.get('p_los', float())
        self.i_los = kwargs.get('i_los', float())
        self.kp_los = kwargs.get('kp_los', float())
        self.ki_los = kwargs.get('ki_los', float())
        self.yaw_vel = kwargs.get('yaw_vel', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.id != other.id:
            return False
        if self.v != other.v:
            return False
        if self.d != other.d:
            return False
        if self.e != other.e:
            return False
        if self.de != other.de:
            return False
        if self.given_position_lat != other.given_position_lat:
            return False
        if self.given_position_lon != other.given_position_lon:
            return False
        if self.starting_position_lat != other.starting_position_lat:
            return False
        if self.starting_position_lon != other.starting_position_lon:
            return False
        if self.left_thrust != other.left_thrust:
            return False
        if self.right_thrust != other.right_thrust:
            return False
        if self.given_azimuth != other.given_azimuth:
            return False
        if self.current_azimuth != other.current_azimuth:
            return False
        if self.distance != other.distance:
            return False
        if self.p_los != other.p_los:
            return False
        if self.i_los != other.i_los:
            return False
        if self.kp_los != other.kp_los:
            return False
        if self.ki_los != other.ki_los:
            return False
        if self.yaw_vel != other.yaw_vel:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if self._check_fields:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property  # noqa: A003
    def id(self):  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value):  # noqa: A003
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'id' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'id' field must be an integer in [-2147483648, 2147483647]"
        self._id = value

    @builtins.property
    def v(self):
        """Message field 'v'."""
        return self._v

    @v.setter
    def v(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'v' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'v' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._v = value

    @builtins.property
    def d(self):
        """Message field 'd'."""
        return self._d

    @d.setter
    def d(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'd' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'd' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._d = value

    @builtins.property
    def e(self):
        """Message field 'e'."""
        return self._e

    @e.setter
    def e(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'e' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'e' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._e = value

    @builtins.property
    def de(self):
        """Message field 'de'."""
        return self._de

    @de.setter
    def de(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'de' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'de' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._de = value

    @builtins.property
    def given_position_lat(self):
        """Message field 'given_position_lat'."""
        return self._given_position_lat

    @given_position_lat.setter
    def given_position_lat(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'given_position_lat' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'given_position_lat' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._given_position_lat = value

    @builtins.property
    def given_position_lon(self):
        """Message field 'given_position_lon'."""
        return self._given_position_lon

    @given_position_lon.setter
    def given_position_lon(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'given_position_lon' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'given_position_lon' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._given_position_lon = value

    @builtins.property
    def starting_position_lat(self):
        """Message field 'starting_position_lat'."""
        return self._starting_position_lat

    @starting_position_lat.setter
    def starting_position_lat(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'starting_position_lat' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'starting_position_lat' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._starting_position_lat = value

    @builtins.property
    def starting_position_lon(self):
        """Message field 'starting_position_lon'."""
        return self._starting_position_lon

    @starting_position_lon.setter
    def starting_position_lon(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'starting_position_lon' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'starting_position_lon' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._starting_position_lon = value

    @builtins.property
    def left_thrust(self):
        """Message field 'left_thrust'."""
        return self._left_thrust

    @left_thrust.setter
    def left_thrust(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'left_thrust' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'left_thrust' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._left_thrust = value

    @builtins.property
    def right_thrust(self):
        """Message field 'right_thrust'."""
        return self._right_thrust

    @right_thrust.setter
    def right_thrust(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'right_thrust' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'right_thrust' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._right_thrust = value

    @builtins.property
    def given_azimuth(self):
        """Message field 'given_azimuth'."""
        return self._given_azimuth

    @given_azimuth.setter
    def given_azimuth(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'given_azimuth' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'given_azimuth' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._given_azimuth = value

    @builtins.property
    def current_azimuth(self):
        """Message field 'current_azimuth'."""
        return self._current_azimuth

    @current_azimuth.setter
    def current_azimuth(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'current_azimuth' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'current_azimuth' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._current_azimuth = value

    @builtins.property
    def distance(self):
        """Message field 'distance'."""
        return self._distance

    @distance.setter
    def distance(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'distance' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'distance' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._distance = value

    @builtins.property
    def p_los(self):
        """Message field 'p_los'."""
        return self._p_los

    @p_los.setter
    def p_los(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'p_los' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'p_los' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._p_los = value

    @builtins.property
    def i_los(self):
        """Message field 'i_los'."""
        return self._i_los

    @i_los.setter
    def i_los(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'i_los' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'i_los' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._i_los = value

    @builtins.property
    def kp_los(self):
        """Message field 'kp_los'."""
        return self._kp_los

    @kp_los.setter
    def kp_los(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'kp_los' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'kp_los' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._kp_los = value

    @builtins.property
    def ki_los(self):
        """Message field 'ki_los'."""
        return self._ki_los

    @ki_los.setter
    def ki_los(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'ki_los' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'ki_los' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._ki_los = value

    @builtins.property
    def yaw_vel(self):
        """Message field 'yaw_vel'."""
        return self._yaw_vel

    @yaw_vel.setter
    def yaw_vel(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'yaw_vel' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'yaw_vel' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._yaw_vel = value
