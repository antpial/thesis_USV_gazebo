#include <gz/plugin/Register.hh>

using namespace maritime;
 
WindPlugin::WindPlugin()
{
}
 
WindPlugin::~WindPlugin()
{
}
 
void WindPlugin::PostUpdate(const gz::sim::UpdateInfo &_info,
    const gz::sim::EntityComponentManager &_ecm)
{
  gzmsg << "WindPlugin::PostUpdate" << std::endl;
}

 



// Include a line in your source file for each interface implemented.
GZ_ADD_PLUGIN(
    maritime::WindPlugin,
    gz::sim::System,
    maritime::WindPlugin::ISystemPostUpdate)