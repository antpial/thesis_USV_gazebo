// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from msg_interfaces:msg/InternalState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "msg_interfaces/msg/internal_state.hpp"


#ifndef MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__STRUCT_HPP_
#define MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__msg_interfaces__msg__InternalState __attribute__((deprecated))
#else
# define DEPRECATED__msg_interfaces__msg__InternalState __declspec(deprecated)
#endif

namespace msg_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct InternalState_
{
  using Type = InternalState_<ContainerAllocator>;

  explicit InternalState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
      this->v = 0.0f;
      this->d = 0.0f;
      this->e = 0.0f;
      this->de = 0.0f;
      this->given_position_lat = 0.0;
      this->given_position_lon = 0.0;
      this->starting_position_lat = 0.0;
      this->starting_position_lon = 0.0;
      this->left_thrust = 0.0f;
      this->right_thrust = 0.0f;
      this->given_azimuth = 0.0f;
      this->current_azimuth = 0.0f;
      this->distance = 0.0f;
      this->p_los = 0.0f;
      this->i_los = 0.0f;
      this->kp_los = 0.0f;
      this->ki_los = 0.0f;
      this->yaw_vel = 0.0f;
    }
  }

  explicit InternalState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
      this->v = 0.0f;
      this->d = 0.0f;
      this->e = 0.0f;
      this->de = 0.0f;
      this->given_position_lat = 0.0;
      this->given_position_lon = 0.0;
      this->starting_position_lat = 0.0;
      this->starting_position_lon = 0.0;
      this->left_thrust = 0.0f;
      this->right_thrust = 0.0f;
      this->given_azimuth = 0.0f;
      this->current_azimuth = 0.0f;
      this->distance = 0.0f;
      this->p_los = 0.0f;
      this->i_los = 0.0f;
      this->kp_los = 0.0f;
      this->ki_los = 0.0f;
      this->yaw_vel = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _id_type =
    int32_t;
  _id_type id;
  using _v_type =
    float;
  _v_type v;
  using _d_type =
    float;
  _d_type d;
  using _e_type =
    float;
  _e_type e;
  using _de_type =
    float;
  _de_type de;
  using _given_position_lat_type =
    double;
  _given_position_lat_type given_position_lat;
  using _given_position_lon_type =
    double;
  _given_position_lon_type given_position_lon;
  using _starting_position_lat_type =
    double;
  _starting_position_lat_type starting_position_lat;
  using _starting_position_lon_type =
    double;
  _starting_position_lon_type starting_position_lon;
  using _left_thrust_type =
    float;
  _left_thrust_type left_thrust;
  using _right_thrust_type =
    float;
  _right_thrust_type right_thrust;
  using _given_azimuth_type =
    float;
  _given_azimuth_type given_azimuth;
  using _current_azimuth_type =
    float;
  _current_azimuth_type current_azimuth;
  using _distance_type =
    float;
  _distance_type distance;
  using _p_los_type =
    float;
  _p_los_type p_los;
  using _i_los_type =
    float;
  _i_los_type i_los;
  using _kp_los_type =
    float;
  _kp_los_type kp_los;
  using _ki_los_type =
    float;
  _ki_los_type ki_los;
  using _yaw_vel_type =
    float;
  _yaw_vel_type yaw_vel;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__id(
    const int32_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__v(
    const float & _arg)
  {
    this->v = _arg;
    return *this;
  }
  Type & set__d(
    const float & _arg)
  {
    this->d = _arg;
    return *this;
  }
  Type & set__e(
    const float & _arg)
  {
    this->e = _arg;
    return *this;
  }
  Type & set__de(
    const float & _arg)
  {
    this->de = _arg;
    return *this;
  }
  Type & set__given_position_lat(
    const double & _arg)
  {
    this->given_position_lat = _arg;
    return *this;
  }
  Type & set__given_position_lon(
    const double & _arg)
  {
    this->given_position_lon = _arg;
    return *this;
  }
  Type & set__starting_position_lat(
    const double & _arg)
  {
    this->starting_position_lat = _arg;
    return *this;
  }
  Type & set__starting_position_lon(
    const double & _arg)
  {
    this->starting_position_lon = _arg;
    return *this;
  }
  Type & set__left_thrust(
    const float & _arg)
  {
    this->left_thrust = _arg;
    return *this;
  }
  Type & set__right_thrust(
    const float & _arg)
  {
    this->right_thrust = _arg;
    return *this;
  }
  Type & set__given_azimuth(
    const float & _arg)
  {
    this->given_azimuth = _arg;
    return *this;
  }
  Type & set__current_azimuth(
    const float & _arg)
  {
    this->current_azimuth = _arg;
    return *this;
  }
  Type & set__distance(
    const float & _arg)
  {
    this->distance = _arg;
    return *this;
  }
  Type & set__p_los(
    const float & _arg)
  {
    this->p_los = _arg;
    return *this;
  }
  Type & set__i_los(
    const float & _arg)
  {
    this->i_los = _arg;
    return *this;
  }
  Type & set__kp_los(
    const float & _arg)
  {
    this->kp_los = _arg;
    return *this;
  }
  Type & set__ki_los(
    const float & _arg)
  {
    this->ki_los = _arg;
    return *this;
  }
  Type & set__yaw_vel(
    const float & _arg)
  {
    this->yaw_vel = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    msg_interfaces::msg::InternalState_<ContainerAllocator> *;
  using ConstRawPtr =
    const msg_interfaces::msg::InternalState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msg_interfaces::msg::InternalState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msg_interfaces::msg::InternalState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::msg::InternalState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::msg::InternalState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::msg::InternalState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::msg::InternalState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msg_interfaces::msg::InternalState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msg_interfaces::msg::InternalState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msg_interfaces__msg__InternalState
    std::shared_ptr<msg_interfaces::msg::InternalState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msg_interfaces__msg__InternalState
    std::shared_ptr<msg_interfaces::msg::InternalState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InternalState_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->id != other.id) {
      return false;
    }
    if (this->v != other.v) {
      return false;
    }
    if (this->d != other.d) {
      return false;
    }
    if (this->e != other.e) {
      return false;
    }
    if (this->de != other.de) {
      return false;
    }
    if (this->given_position_lat != other.given_position_lat) {
      return false;
    }
    if (this->given_position_lon != other.given_position_lon) {
      return false;
    }
    if (this->starting_position_lat != other.starting_position_lat) {
      return false;
    }
    if (this->starting_position_lon != other.starting_position_lon) {
      return false;
    }
    if (this->left_thrust != other.left_thrust) {
      return false;
    }
    if (this->right_thrust != other.right_thrust) {
      return false;
    }
    if (this->given_azimuth != other.given_azimuth) {
      return false;
    }
    if (this->current_azimuth != other.current_azimuth) {
      return false;
    }
    if (this->distance != other.distance) {
      return false;
    }
    if (this->p_los != other.p_los) {
      return false;
    }
    if (this->i_los != other.i_los) {
      return false;
    }
    if (this->kp_los != other.kp_los) {
      return false;
    }
    if (this->ki_los != other.ki_los) {
      return false;
    }
    if (this->yaw_vel != other.yaw_vel) {
      return false;
    }
    return true;
  }
  bool operator!=(const InternalState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InternalState_

// alias to use template instance with default allocator
using InternalState =
  msg_interfaces::msg::InternalState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__MSG__DETAIL__INTERNAL_STATE__STRUCT_HPP_
