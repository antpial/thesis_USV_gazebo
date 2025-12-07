// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from msg_interfaces:msg/InternalState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "msg_interfaces/msg/internal_state.hpp"


#ifndef MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__TRAITS_HPP_
#define MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "msg_interfaces/msg/detail/internal_state__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace msg_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const InternalState & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: id
  {
    out << "id: ";
    rosidl_generator_traits::value_to_yaml(msg.id, out);
    out << ", ";
  }

  // member: v
  {
    out << "v: ";
    rosidl_generator_traits::value_to_yaml(msg.v, out);
    out << ", ";
  }

  // member: d
  {
    out << "d: ";
    rosidl_generator_traits::value_to_yaml(msg.d, out);
    out << ", ";
  }

  // member: e
  {
    out << "e: ";
    rosidl_generator_traits::value_to_yaml(msg.e, out);
    out << ", ";
  }

  // member: de
  {
    out << "de: ";
    rosidl_generator_traits::value_to_yaml(msg.de, out);
    out << ", ";
  }

  // member: given_position_lat
  {
    out << "given_position_lat: ";
    rosidl_generator_traits::value_to_yaml(msg.given_position_lat, out);
    out << ", ";
  }

  // member: given_position_lon
  {
    out << "given_position_lon: ";
    rosidl_generator_traits::value_to_yaml(msg.given_position_lon, out);
    out << ", ";
  }

  // member: starting_position_lat
  {
    out << "starting_position_lat: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_position_lat, out);
    out << ", ";
  }

  // member: starting_position_lon
  {
    out << "starting_position_lon: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_position_lon, out);
    out << ", ";
  }

  // member: left_thrust
  {
    out << "left_thrust: ";
    rosidl_generator_traits::value_to_yaml(msg.left_thrust, out);
    out << ", ";
  }

  // member: right_thrust
  {
    out << "right_thrust: ";
    rosidl_generator_traits::value_to_yaml(msg.right_thrust, out);
    out << ", ";
  }

  // member: given_azimuth
  {
    out << "given_azimuth: ";
    rosidl_generator_traits::value_to_yaml(msg.given_azimuth, out);
    out << ", ";
  }

  // member: current_azimuth
  {
    out << "current_azimuth: ";
    rosidl_generator_traits::value_to_yaml(msg.current_azimuth, out);
    out << ", ";
  }

  // member: distance
  {
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
    out << ", ";
  }

  // member: p_los
  {
    out << "p_los: ";
    rosidl_generator_traits::value_to_yaml(msg.p_los, out);
    out << ", ";
  }

  // member: i_los
  {
    out << "i_los: ";
    rosidl_generator_traits::value_to_yaml(msg.i_los, out);
    out << ", ";
  }

  // member: kp_los
  {
    out << "kp_los: ";
    rosidl_generator_traits::value_to_yaml(msg.kp_los, out);
    out << ", ";
  }

  // member: ki_los
  {
    out << "ki_los: ";
    rosidl_generator_traits::value_to_yaml(msg.ki_los, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const InternalState & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "id: ";
    rosidl_generator_traits::value_to_yaml(msg.id, out);
    out << "\n";
  }

  // member: v
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "v: ";
    rosidl_generator_traits::value_to_yaml(msg.v, out);
    out << "\n";
  }

  // member: d
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "d: ";
    rosidl_generator_traits::value_to_yaml(msg.d, out);
    out << "\n";
  }

  // member: e
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "e: ";
    rosidl_generator_traits::value_to_yaml(msg.e, out);
    out << "\n";
  }

  // member: de
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "de: ";
    rosidl_generator_traits::value_to_yaml(msg.de, out);
    out << "\n";
  }

  // member: given_position_lat
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "given_position_lat: ";
    rosidl_generator_traits::value_to_yaml(msg.given_position_lat, out);
    out << "\n";
  }

  // member: given_position_lon
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "given_position_lon: ";
    rosidl_generator_traits::value_to_yaml(msg.given_position_lon, out);
    out << "\n";
  }

  // member: starting_position_lat
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "starting_position_lat: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_position_lat, out);
    out << "\n";
  }

  // member: starting_position_lon
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "starting_position_lon: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_position_lon, out);
    out << "\n";
  }

  // member: left_thrust
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "left_thrust: ";
    rosidl_generator_traits::value_to_yaml(msg.left_thrust, out);
    out << "\n";
  }

  // member: right_thrust
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "right_thrust: ";
    rosidl_generator_traits::value_to_yaml(msg.right_thrust, out);
    out << "\n";
  }

  // member: given_azimuth
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "given_azimuth: ";
    rosidl_generator_traits::value_to_yaml(msg.given_azimuth, out);
    out << "\n";
  }

  // member: current_azimuth
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_azimuth: ";
    rosidl_generator_traits::value_to_yaml(msg.current_azimuth, out);
    out << "\n";
  }

  // member: distance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
    out << "\n";
  }

  // member: p_los
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "p_los: ";
    rosidl_generator_traits::value_to_yaml(msg.p_los, out);
    out << "\n";
  }

  // member: i_los
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "i_los: ";
    rosidl_generator_traits::value_to_yaml(msg.i_los, out);
    out << "\n";
  }

  // member: kp_los
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "kp_los: ";
    rosidl_generator_traits::value_to_yaml(msg.kp_los, out);
    out << "\n";
  }

  // member: ki_los
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ki_los: ";
    rosidl_generator_traits::value_to_yaml(msg.ki_los, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const InternalState & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace msg_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use msg_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const msg_interfaces::msg::InternalState & msg,
  std::ostream & out, size_t indentation = 0)
{
  msg_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use msg_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const msg_interfaces::msg::InternalState & msg)
{
  return msg_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<msg_interfaces::msg::InternalState>()
{
  return "msg_interfaces::msg::InternalState";
}

template<>
inline const char * name<msg_interfaces::msg::InternalState>()
{
  return "msg_interfaces/msg/InternalState";
}

template<>
struct has_fixed_size<msg_interfaces::msg::InternalState>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<msg_interfaces::msg::InternalState>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<msg_interfaces::msg::InternalState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__TRAITS_HPP_
