#pragma once
#include "esphome.h"

namespace esphome {
namespace fast_pulse {

class FastPulseOutput : public Component, public FloatOutput {
 public:
  void set_pin(GPIOPin *pin) { pin_ = pin; }
  void set_pulse_width(uint32_t width) { pulse_width_ = width; }
  void set_pulse_gap(uint32_t gap) { pulse_gap_ = gap; }
  void set_max_pulses(uint32_t max) { max_pulses_ = max; }

  void setup() override {
    pin_->setup();
    pin_->digital_write(false);
  }

  void write_state(float state) override {
    if (state > 0.5f) {
      for(uint32_t i = 0; i < max_pulses_; i++) {
        pin_->digital_write(true);
        delayMicroseconds(pulse_width_);
        pin_->digital_write(false);
        delayMicroseconds(pulse_gap_);
      }
    }
  }

 protected:
  GPIOPin *pin_;
  uint32_t pulse_width_{10};
  uint32_t pulse_gap_{40};
  uint32_t max_pulses_{10000};
};

}  // namespace fast_pulse
}  // namespace esphome
