// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from msg_interfaces:msg/InternalState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "msg_interfaces/msg/internal_state.hpp"


#ifndef MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__BUILDER_HPP_
#define MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "msg_interfaces/msg/detail/internal_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace msg_interfaces
{

namespace msg
{

namespace builder
{

class Init_InternalState_ki_los
{
public:
  explicit Init_InternalState_ki_los(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  ::msg_interfaces::msg::InternalState ki_los(::msg_interfaces::msg::InternalState::_ki_los_type arg)
  {
    msg_.ki_los = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_kp_los
{
public:
  explicit Init_InternalState_kp_los(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_ki_los kp_los(::msg_interfaces::msg::InternalState::_kp_los_type arg)
  {
    msg_.kp_los = std::move(arg);
    return Init_InternalState_ki_los(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_i_los
{
public:
  explicit Init_InternalState_i_los(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_kp_los i_los(::msg_interfaces::msg::InternalState::_i_los_type arg)
  {
    msg_.i_los = std::move(arg);
    return Init_InternalState_kp_los(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_p_los
{
public:
  explicit Init_InternalState_p_los(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_i_los p_los(::msg_interfaces::msg::InternalState::_p_los_type arg)
  {
    msg_.p_los = std::move(arg);
    return Init_InternalState_i_los(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_distance
{
public:
  explicit Init_InternalState_distance(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_p_los distance(::msg_interfaces::msg::InternalState::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_InternalState_p_los(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_current_azimuth
{
public:
  explicit Init_InternalState_current_azimuth(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_distance current_azimuth(::msg_interfaces::msg::InternalState::_current_azimuth_type arg)
  {
    msg_.current_azimuth = std::move(arg);
    return Init_InternalState_distance(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_given_azimuth
{
public:
  explicit Init_InternalState_given_azimuth(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_current_azimuth given_azimuth(::msg_interfaces::msg::InternalState::_given_azimuth_type arg)
  {
    msg_.given_azimuth = std::move(arg);
    return Init_InternalState_current_azimuth(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_right_thrust
{
public:
  explicit Init_InternalState_right_thrust(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_given_azimuth right_thrust(::msg_interfaces::msg::InternalState::_right_thrust_type arg)
  {
    msg_.right_thrust = std::move(arg);
    return Init_InternalState_given_azimuth(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_left_thrust
{
public:
  explicit Init_InternalState_left_thrust(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_right_thrust left_thrust(::msg_interfaces::msg::InternalState::_left_thrust_type arg)
  {
    msg_.left_thrust = std::move(arg);
    return Init_InternalState_right_thrust(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_starting_position_lon
{
public:
  explicit Init_InternalState_starting_position_lon(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_left_thrust starting_position_lon(::msg_interfaces::msg::InternalState::_starting_position_lon_type arg)
  {
    msg_.starting_position_lon = std::move(arg);
    return Init_InternalState_left_thrust(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_starting_position_lat
{
public:
  explicit Init_InternalState_starting_position_lat(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_starting_position_lon starting_position_lat(::msg_interfaces::msg::InternalState::_starting_position_lat_type arg)
  {
    msg_.starting_position_lat = std::move(arg);
    return Init_InternalState_starting_position_lon(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_given_position_lon
{
public:
  explicit Init_InternalState_given_position_lon(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_starting_position_lat given_position_lon(::msg_interfaces::msg::InternalState::_given_position_lon_type arg)
  {
    msg_.given_position_lon = std::move(arg);
    return Init_InternalState_starting_position_lat(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_given_position_lat
{
public:
  explicit Init_InternalState_given_position_lat(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_given_position_lon given_position_lat(::msg_interfaces::msg::InternalState::_given_position_lat_type arg)
  {
    msg_.given_position_lat = std::move(arg);
    return Init_InternalState_given_position_lon(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_de
{
public:
  explicit Init_InternalState_de(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_given_position_lat de(::msg_interfaces::msg::InternalState::_de_type arg)
  {
    msg_.de = std::move(arg);
    return Init_InternalState_given_position_lat(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_e
{
public:
  explicit Init_InternalState_e(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_de e(::msg_interfaces::msg::InternalState::_e_type arg)
  {
    msg_.e = std::move(arg);
    return Init_InternalState_de(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_d
{
public:
  explicit Init_InternalState_d(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_e d(::msg_interfaces::msg::InternalState::_d_type arg)
  {
    msg_.d = std::move(arg);
    return Init_InternalState_e(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_v
{
public:
  explicit Init_InternalState_v(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_d v(::msg_interfaces::msg::InternalState::_v_type arg)
  {
    msg_.v = std::move(arg);
    return Init_InternalState_d(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_id
{
public:
  explicit Init_InternalState_id(::msg_interfaces::msg::InternalState & msg)
  : msg_(msg)
  {}
  Init_InternalState_v id(::msg_interfaces::msg::InternalState::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_InternalState_v(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

class Init_InternalState_header
{
public:
  Init_InternalState_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InternalState_id header(::msg_interfaces::msg::InternalState::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_InternalState_id(msg_);
  }

private:
  ::msg_interfaces::msg::InternalState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_interfaces::msg::InternalState>()
{
  return msg_interfaces::msg::builder::Init_InternalState_header();
}

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__BUILDER_HPP_
