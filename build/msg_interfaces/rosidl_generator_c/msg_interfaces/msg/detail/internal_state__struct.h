// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from msg_interfaces:msg/InternalState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "msg_interfaces/msg/internal_state.h"


#ifndef MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__STRUCT_H_
#define MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/InternalState in the package msg_interfaces.
typedef struct msg_interfaces__msg__InternalState
{
  std_msgs__msg__Header header;
  int32_t id;
  /// --- Sterowanie ---
  /// przepustnica
  float v;
  /// kierownica (ster)
  float d;
  /// --- Błędy sterowania ---
  /// blad kursu (heading error)
  float e;
  /// cross track error (odleglosc od linii)
  float de;
  /// --- Nawigacja GPS (Musi byc float64!) ---
  /// cel lodzi lat
  double given_position_lat;
  /// cel lodzi lon
  double given_position_lon;
  /// start lodzi lat
  double starting_position_lat;
  /// start lodzi lon
  double starting_position_lon;
  /// --- Wyjścia silników ---
  /// ciag na lewym silniku
  float left_thrust;
  /// ciag na prawym silniku
  float right_thrust;
  /// --- Stan ---
  /// azymut do ktorego zmierza lodka
  float given_azimuth;
  /// chwilowy azymut lodzi
  float current_azimuth;
  /// dystans do punku docelowego
  float distance;
  /// --- Diagnostyka PID/LOS ---
  /// wartość wyjściowa członu P
  float p_los;
  /// wartosc wyjsciowa czlonu I
  float i_los;
  /// nastawa Kp
  float kp_los;
  /// nastawa Ki
  float ki_los;
} msg_interfaces__msg__InternalState;

// Struct for a sequence of msg_interfaces__msg__InternalState.
typedef struct msg_interfaces__msg__InternalState__Sequence
{
  msg_interfaces__msg__InternalState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_interfaces__msg__InternalState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__STRUCT_H_
