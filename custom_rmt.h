// custom_rmt.h
#include "esphome.h"

class FastPulseOutput : public Component, public output::FloatOutput {
public:
    void set_pin(InternalGPIOPin *pin) { pin_ = pin; }
    
    void setup() override {
        pin_->setup();
        pin_->pin_mode(OUTPUT);
    }

    void write_state(float state) override {
        if (state > 0.5f) {
            for (int i = 0; i < 10; i++) {  // 10 импульсов
                pin_->digital_write(true);
                delayMicroseconds(10);  // 10 µs HIGH
                pin_->digital_write(false);
                delayMicroseconds(90);  // 90 µs LOW (10 kHz)
            }
        }
    }

private:
    InternalGPIOPin *pin_;
};
