import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate, ble_client
from esphome.const import CONF_ID

CODEOWNERS = ["@Frank802"]
DEPENDENCIES = ["ble_client"]

madoka_vam_ns = cg.esphome_ns.namespace("madoka_vam")
MadokaVam = madoka_vam_ns.class_(
    "MadokaVam", climate.Climate, ble_client.BLEClientNode, cg.PollingComponent
)

CONFIG_SCHEMA = (
    climate.CLIMATE_SCHEMA.extend(
        {
            cv.GenerateID(): cv.declare_id(MadokaVam),
        }
    )
    .extend(ble_client.BLE_CLIENT_SCHEMA)
    .extend(cv.polling_component_schema("10s"))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await climate.register_climate(var, config)
    await ble_client.register_ble_node(var, config)
