import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.const import CONF_ID, CONF_PIN

DEPENDENCIES = []
CODEOWNERS = ["@isiirk32"]

fast_pulse_ns = cg.esphome_ns.namespace('fast_pulse')
FastPulseOutput = fast_pulse_ns.class_('FastPulseOutput', cg.Component, cg.Output)

CONFIG_SCHEMA = cv.Schema({
    cv.Required(CONF_PIN): pins.gpio_output_pin_schema,
    cv.Optional('pulse_width', default='10us'): cv.positive_time_period_microseconds,
    cv.Optional('pulse_gap', default='40us'): cv.positive_time_period_microseconds,
    cv.Optional('max_pulses', default=10000): cv.positive_int,
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    
    pin = await cg.gpio_pin_expression(config[CONF_PIN])
    cg.add(var.set_pin(pin))
    
    cg.add(var.set_pulse_width(config['pulse_width']))
    cg.add(var.set_pulse_gap(config['pulse_gap']))
    cg.add(var.set_max_pulses(config['max_pulses']))
