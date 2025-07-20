from esphome import pins
from esphome.components.output import Output
import esphome.config_validation as cv
import esphome.codegen as cg

# Импортируем реализацию
from .output import FastPulseOutput

# Конфигурационная схема
CONFIG_SCHEMA = Output.BASE_OUTPUT_SCHEMA.extend({
    cv.Required("pin"): pins.gpio_output_pin_schema,
    cv.Optional("pulse_width", default="10us"): cv.positive_time_period_microseconds,
    cv.Optional("pulse_gap", default="40us"): cv.positive_time_period_microseconds,
    cv.Optional("max_pulses", default=10000): cv.positive_int,
})

# Функция для создания компонента
async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await Output.register_output(var, config)
    
    pin = await cg.gpio_pin_expression(config["pin"])
    cg.add(var.set_pin(pin))
    
    cg.add(var.set_pulse_width(config["pulse_width"]))
    cg.add(var.set_pulse_gap(config["pulse_gap"]))
    cg.add(var.set_max_pulses(config["max_pulses"]))
