#ifndef WIND_PLUGIN_HH_
#define WIND_PLUGIN_HH_

#include <gz/sim/System.hh>
 
namespace maritime{
 
  class WindPlugin :
    // This class is a system.
    public gz::sim::System,
    // This class also implements the ISystemPreUpdate, ISystemUpdate,
    // and ISystemPostUpdate interfaces.
    public gz::sim::ISystemPreUpdate,
    public gz::sim::ISystemUpdate,
    public gz::sim::ISystemPostUpdate,
    public gz::sim::ISystemReset
  {
    public: WindPlugin();
 
    public: ~WindPlugin() override;
 
    public: void PreUpdate(const gz::sim::UpdateInfo &_info,
                gz::sim::EntityComponentManager &_ecm) override;
 
    // public: void Update(const gz::sim::UpdateInfo &_info,
    //             gz::sim::EntityComponentManager &_ecm) override;
 
    public: void PostUpdate(const gz::sim::UpdateInfo &_info,
                const gz::sim::EntityComponentManager &_ecm) override;
 
    // public: void Reset(const gz::sim::UpdateInfo &_info,
    //              gz::sim::EntityComponentManager &_ecm) override;
  };
}
#endif