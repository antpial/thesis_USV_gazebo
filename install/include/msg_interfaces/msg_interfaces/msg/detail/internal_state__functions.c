// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from msg_interfaces:msg/InternalState.idl
// generated code does not contain a copyright notice
#include "msg_interfaces/msg/detail/internal_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
msg_interfaces__msg__InternalState__init(msg_interfaces__msg__InternalState * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    msg_interfaces__msg__InternalState__fini(msg);
    return false;
  }
  // id
  // v
  // d
  // e
  // de
  // given_position_lat
  // given_position_lon
  // starting_position_lat
  // starting_position_lon
  // left_thrust
  // right_thrust
  // given_azimuth
  // current_azimuth
  // distance
  // p_los
  // i_los
  // kp_los
  // ki_los
  return true;
}

void
msg_interfaces__msg__InternalState__fini(msg_interfaces__msg__InternalState * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // id
  // v
  // d
  // e
  // de
  // given_position_lat
  // given_position_lon
  // starting_position_lat
  // starting_position_lon
  // left_thrust
  // right_thrust
  // given_azimuth
  // current_azimuth
  // distance
  // p_los
  // i_los
  // kp_los
  // ki_los
}

bool
msg_interfaces__msg__InternalState__are_equal(const msg_interfaces__msg__InternalState * lhs, const msg_interfaces__msg__InternalState * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // id
  if (lhs->id != rhs->id) {
    return false;
  }
  // v
  if (lhs->v != rhs->v) {
    return false;
  }
  // d
  if (lhs->d != rhs->d) {
    return false;
  }
  // e
  if (lhs->e != rhs->e) {
    return false;
  }
  // de
  if (lhs->de != rhs->de) {
    return false;
  }
  // given_position_lat
  if (lhs->given_position_lat != rhs->given_position_lat) {
    return false;
  }
  // given_position_lon
  if (lhs->given_position_lon != rhs->given_position_lon) {
    return false;
  }
  // starting_position_lat
  if (lhs->starting_position_lat != rhs->starting_position_lat) {
    return false;
  }
  // starting_position_lon
  if (lhs->starting_position_lon != rhs->starting_position_lon) {
    return false;
  }
  // left_thrust
  if (lhs->left_thrust != rhs->left_thrust) {
    return false;
  }
  // right_thrust
  if (lhs->right_thrust != rhs->right_thrust) {
    return false;
  }
  // given_azimuth
  if (lhs->given_azimuth != rhs->given_azimuth) {
    return false;
  }
  // current_azimuth
  if (lhs->current_azimuth != rhs->current_azimuth) {
    return false;
  }
  // distance
  if (lhs->distance != rhs->distance) {
    return false;
  }
  // p_los
  if (lhs->p_los != rhs->p_los) {
    return false;
  }
  // i_los
  if (lhs->i_los != rhs->i_los) {
    return false;
  }
  // kp_los
  if (lhs->kp_los != rhs->kp_los) {
    return false;
  }
  // ki_los
  if (lhs->ki_los != rhs->ki_los) {
    return false;
  }
  return true;
}

bool
msg_interfaces__msg__InternalState__copy(
  const msg_interfaces__msg__InternalState * input,
  msg_interfaces__msg__InternalState * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // id
  output->id = input->id;
  // v
  output->v = input->v;
  // d
  output->d = input->d;
  // e
  output->e = input->e;
  // de
  output->de = input->de;
  // given_position_lat
  output->given_position_lat = input->given_position_lat;
  // given_position_lon
  output->given_position_lon = input->given_position_lon;
  // starting_position_lat
  output->starting_position_lat = input->starting_position_lat;
  // starting_position_lon
  output->starting_position_lon = input->starting_position_lon;
  // left_thrust
  output->left_thrust = input->left_thrust;
  // right_thrust
  output->right_thrust = input->right_thrust;
  // given_azimuth
  output->given_azimuth = input->given_azimuth;
  // current_azimuth
  output->current_azimuth = input->current_azimuth;
  // distance
  output->distance = input->distance;
  // p_los
  output->p_los = input->p_los;
  // i_los
  output->i_los = input->i_los;
  // kp_los
  output->kp_los = input->kp_los;
  // ki_los
  output->ki_los = input->ki_los;
  return true;
}

msg_interfaces__msg__InternalState *
msg_interfaces__msg__InternalState__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__msg__InternalState * msg = (msg_interfaces__msg__InternalState *)allocator.allocate(sizeof(msg_interfaces__msg__InternalState), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(msg_interfaces__msg__InternalState));
  bool success = msg_interfaces__msg__InternalState__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
msg_interfaces__msg__InternalState__destroy(msg_interfaces__msg__InternalState * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    msg_interfaces__msg__InternalState__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
msg_interfaces__msg__InternalState__Sequence__init(msg_interfaces__msg__InternalState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__msg__InternalState * data = NULL;

  if (size) {
    data = (msg_interfaces__msg__InternalState *)allocator.zero_allocate(size, sizeof(msg_interfaces__msg__InternalState), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = msg_interfaces__msg__InternalState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        msg_interfaces__msg__InternalState__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
msg_interfaces__msg__InternalState__Sequence__fini(msg_interfaces__msg__InternalState__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      msg_interfaces__msg__InternalState__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

msg_interfaces__msg__InternalState__Sequence *
msg_interfaces__msg__InternalState__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__msg__InternalState__Sequence * array = (msg_interfaces__msg__InternalState__Sequence *)allocator.allocate(sizeof(msg_interfaces__msg__InternalState__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = msg_interfaces__msg__InternalState__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
msg_interfaces__msg__InternalState__Sequence__destroy(msg_interfaces__msg__InternalState__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    msg_interfaces__msg__InternalState__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
msg_interfaces__msg__InternalState__Sequence__are_equal(const msg_interfaces__msg__InternalState__Sequence * lhs, const msg_interfaces__msg__InternalState__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!msg_interfaces__msg__InternalState__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
msg_interfaces__msg__InternalState__Sequence__copy(
  const msg_interfaces__msg__InternalState__Sequence * input,
  msg_interfaces__msg__InternalState__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(msg_interfaces__msg__InternalState);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    msg_interfaces__msg__InternalState * data =
      (msg_interfaces__msg__InternalState *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!msg_interfaces__msg__InternalState__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          msg_interfaces__msg__InternalState__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!msg_interfaces__msg__InternalState__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
