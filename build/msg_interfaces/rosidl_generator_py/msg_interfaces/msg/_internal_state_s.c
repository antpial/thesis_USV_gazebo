// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from msg_interfaces:msg/InternalState.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "msg_interfaces/msg/detail/internal_state__struct.h"
#include "msg_interfaces/msg/detail/internal_state__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool msg_interfaces__msg__internal_state__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[49];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("msg_interfaces.msg._internal_state.InternalState", full_classname_dest, 48) == 0);
  }
  msg_interfaces__msg__InternalState * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // id
    PyObject * field = PyObject_GetAttrString(_pymsg, "id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->id = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // v
    PyObject * field = PyObject_GetAttrString(_pymsg, "v");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->v = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // d
    PyObject * field = PyObject_GetAttrString(_pymsg, "d");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->d = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // e
    PyObject * field = PyObject_GetAttrString(_pymsg, "e");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->e = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // de
    PyObject * field = PyObject_GetAttrString(_pymsg, "de");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->de = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // given_position_lat
    PyObject * field = PyObject_GetAttrString(_pymsg, "given_position_lat");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->given_position_lat = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // given_position_lon
    PyObject * field = PyObject_GetAttrString(_pymsg, "given_position_lon");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->given_position_lon = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // starting_position_lat
    PyObject * field = PyObject_GetAttrString(_pymsg, "starting_position_lat");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->starting_position_lat = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // starting_position_lon
    PyObject * field = PyObject_GetAttrString(_pymsg, "starting_position_lon");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->starting_position_lon = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // left_thrust
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_thrust");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->left_thrust = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // right_thrust
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_thrust");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->right_thrust = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // given_azimuth
    PyObject * field = PyObject_GetAttrString(_pymsg, "given_azimuth");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->given_azimuth = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // current_azimuth
    PyObject * field = PyObject_GetAttrString(_pymsg, "current_azimuth");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->current_azimuth = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // distance
    PyObject * field = PyObject_GetAttrString(_pymsg, "distance");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->distance = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // p_los
    PyObject * field = PyObject_GetAttrString(_pymsg, "p_los");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->p_los = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // i_los
    PyObject * field = PyObject_GetAttrString(_pymsg, "i_los");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->i_los = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // kp_los
    PyObject * field = PyObject_GetAttrString(_pymsg, "kp_los");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->kp_los = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ki_los
    PyObject * field = PyObject_GetAttrString(_pymsg, "ki_los");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ki_los = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw_vel
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw_vel");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw_vel = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * msg_interfaces__msg__internal_state__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of InternalState */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("msg_interfaces.msg._internal_state");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "InternalState");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  msg_interfaces__msg__InternalState * ros_message = (msg_interfaces__msg__InternalState *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // v
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->v);
    {
      int rc = PyObject_SetAttrString(_pymessage, "v", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // d
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->d);
    {
      int rc = PyObject_SetAttrString(_pymessage, "d", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // e
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->e);
    {
      int rc = PyObject_SetAttrString(_pymessage, "e", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // de
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->de);
    {
      int rc = PyObject_SetAttrString(_pymessage, "de", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // given_position_lat
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->given_position_lat);
    {
      int rc = PyObject_SetAttrString(_pymessage, "given_position_lat", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // given_position_lon
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->given_position_lon);
    {
      int rc = PyObject_SetAttrString(_pymessage, "given_position_lon", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // starting_position_lat
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->starting_position_lat);
    {
      int rc = PyObject_SetAttrString(_pymessage, "starting_position_lat", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // starting_position_lon
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->starting_position_lon);
    {
      int rc = PyObject_SetAttrString(_pymessage, "starting_position_lon", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_thrust
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->left_thrust);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_thrust", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_thrust
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->right_thrust);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_thrust", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // given_azimuth
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->given_azimuth);
    {
      int rc = PyObject_SetAttrString(_pymessage, "given_azimuth", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // current_azimuth
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->current_azimuth);
    {
      int rc = PyObject_SetAttrString(_pymessage, "current_azimuth", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // distance
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->distance);
    {
      int rc = PyObject_SetAttrString(_pymessage, "distance", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // p_los
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->p_los);
    {
      int rc = PyObject_SetAttrString(_pymessage, "p_los", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // i_los
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->i_los);
    {
      int rc = PyObject_SetAttrString(_pymessage, "i_los", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // kp_los
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->kp_los);
    {
      int rc = PyObject_SetAttrString(_pymessage, "kp_los", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ki_los
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ki_los);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ki_los", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw_vel
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw_vel);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw_vel", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
