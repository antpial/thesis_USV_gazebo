// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from msg_interfaces:msg/InternalState.idl
// generated code does not contain a copyright notice

#include "msg_interfaces/msg/detail/internal_state__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_msg_interfaces
const rosidl_type_hash_t *
msg_interfaces__msg__InternalState__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x4c, 0x07, 0xad, 0xce, 0xee, 0xb4, 0x90, 0x88,
      0x32, 0x1b, 0x0d, 0xc4, 0x9c, 0x3c, 0x08, 0x41,
      0x54, 0x5e, 0x3f, 0x63, 0xac, 0xae, 0x66, 0x40,
      0xa8, 0xa4, 0xec, 0xaa, 0x49, 0x94, 0xfc, 0x11,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "std_msgs/msg/detail/header__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t std_msgs__msg__Header__EXPECTED_HASH = {1, {
    0xf4, 0x9f, 0xb3, 0xae, 0x2c, 0xf0, 0x70, 0xf7,
    0x93, 0x64, 0x5f, 0xf7, 0x49, 0x68, 0x3a, 0xc6,
    0xb0, 0x62, 0x03, 0xe4, 0x1c, 0x89, 0x1e, 0x17,
    0x70, 0x1b, 0x1c, 0xb5, 0x97, 0xce, 0x6a, 0x01,
  }};
#endif

static char msg_interfaces__msg__InternalState__TYPE_NAME[] = "msg_interfaces/msg/InternalState";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char std_msgs__msg__Header__TYPE_NAME[] = "std_msgs/msg/Header";

// Define type names, field names, and default values
static char msg_interfaces__msg__InternalState__FIELD_NAME__header[] = "header";
static char msg_interfaces__msg__InternalState__FIELD_NAME__id[] = "id";
static char msg_interfaces__msg__InternalState__FIELD_NAME__v[] = "v";
static char msg_interfaces__msg__InternalState__FIELD_NAME__d[] = "d";
static char msg_interfaces__msg__InternalState__FIELD_NAME__e[] = "e";
static char msg_interfaces__msg__InternalState__FIELD_NAME__de[] = "de";
static char msg_interfaces__msg__InternalState__FIELD_NAME__given_position_lat[] = "given_position_lat";
static char msg_interfaces__msg__InternalState__FIELD_NAME__given_position_lon[] = "given_position_lon";
static char msg_interfaces__msg__InternalState__FIELD_NAME__starting_position_lat[] = "starting_position_lat";
static char msg_interfaces__msg__InternalState__FIELD_NAME__starting_position_lon[] = "starting_position_lon";
static char msg_interfaces__msg__InternalState__FIELD_NAME__left_thrust[] = "left_thrust";
static char msg_interfaces__msg__InternalState__FIELD_NAME__right_thrust[] = "right_thrust";
static char msg_interfaces__msg__InternalState__FIELD_NAME__given_azimuth[] = "given_azimuth";
static char msg_interfaces__msg__InternalState__FIELD_NAME__current_azimuth[] = "current_azimuth";
static char msg_interfaces__msg__InternalState__FIELD_NAME__distance[] = "distance";
static char msg_interfaces__msg__InternalState__FIELD_NAME__p_los[] = "p_los";
static char msg_interfaces__msg__InternalState__FIELD_NAME__i_los[] = "i_los";
static char msg_interfaces__msg__InternalState__FIELD_NAME__kp_los[] = "kp_los";
static char msg_interfaces__msg__InternalState__FIELD_NAME__ki_los[] = "ki_los";
static char msg_interfaces__msg__InternalState__FIELD_NAME__yaw_vel[] = "yaw_vel";

static rosidl_runtime_c__type_description__Field msg_interfaces__msg__InternalState__FIELDS[] = {
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__header, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__id, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__v, 1, 1},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__d, 1, 1},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__e, 1, 1},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__de, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__given_position_lat, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__given_position_lon, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__starting_position_lat, 21, 21},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__starting_position_lon, 21, 21},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__left_thrust, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__right_thrust, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__given_azimuth, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__current_azimuth, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__distance, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__p_los, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__i_los, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__kp_los, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__ki_los, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {msg_interfaces__msg__InternalState__FIELD_NAME__yaw_vel, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription msg_interfaces__msg__InternalState__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
msg_interfaces__msg__InternalState__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {msg_interfaces__msg__InternalState__TYPE_NAME, 32, 32},
      {msg_interfaces__msg__InternalState__FIELDS, 20, 20},
    },
    {msg_interfaces__msg__InternalState__REFERENCED_TYPE_DESCRIPTIONS, 2, 2},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__Header__EXPECTED_HASH, std_msgs__msg__Header__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = std_msgs__msg__Header__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "std_msgs/Header header\n"
  "\n"
  "int32 id\n"
  "\n"
  "# --- Sterowanie ---\n"
  "float32 v           # przepustnica\n"
  "float32 d           # kierownica (ster)\n"
  "\n"
  "# --- B\\xc5\\x82\\xc4\\x99dy sterowania ---\n"
  "float32 e           # blad kursu (heading error)\n"
  "float32 de          # cross track error (odleglosc od linii)\n"
  "\n"
  "# --- Nawigacja GPS (Musi byc float64!) ---\n"
  "float64 given_position_lat    # cel lodzi lat\n"
  "float64 given_position_lon    # cel lodzi lon\n"
  "float64 starting_position_lat # start lodzi lat\n"
  "float64 starting_position_lon # start lodzi lon\n"
  "\n"
  "# --- Wyj\\xc5\\x9bcia silnik\\xc3\\xb3w ---\n"
  "float32 left_thrust   # ciag na lewym silniku\n"
  "float32 right_thrust  # ciag na prawym silniku\n"
  "\n"
  "# --- Stan ---\n"
  "float32 given_azimuth    # azymut do ktorego zmierza lodka\n"
  "float32 current_azimuth  # chwilowy azymut lodzi\n"
  "float32 distance         # dystans do punku docelowego\n"
  "\n"
  "# --- Diagnostyka PID/LOS ---\n"
  "float32 p_los      # warto\\xc5\\x9b\\xc4\\x87 wyj\\xc5\\x9bciowa cz\\xc5\\x82onu P\n"
  "float32 i_los      # wartosc wyjsciowa czlonu I\n"
  "float32 kp_los     # nastawa Kp\n"
  "float32 ki_los     # nastawa Ki\n"
  "float32 yaw_vel    # (dodane po znalezieniu Kp_az) szybkosc obrotu z imu";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
msg_interfaces__msg__InternalState__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {msg_interfaces__msg__InternalState__TYPE_NAME, 32, 32},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 1064, 1064},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
msg_interfaces__msg__InternalState__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[3];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 3, 3};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *msg_interfaces__msg__InternalState__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *std_msgs__msg__Header__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
