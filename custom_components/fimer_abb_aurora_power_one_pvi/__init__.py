"""The Fimer/ABB/Aurora Power-One PV inverter sensor integration."""

# Reference info:
# https://s1.solacity.com/docs/PVI-3.0-3.6-4.2-OUTD-US%20Manual.pdf
# http://www.drhack.it/images/PDF/AuroraCommunicationProtocol_4_2.pdf

import logging

from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryError

from .aurora_client import AuroraClient
from .const import (
    CONF_INVERTER_SERIAL_ADDRESS,
    CONF_SERIAL_COMPORT,
    CONF_TCP_HOST,
    CONF_TCP_PORT,
    CONF_TRANSPORT,
    TRANSPORT_SERIAL,
    TRANSPORT_TCP,
)
from .coordinator import AuroraAbbConfigEntry, AuroraAbbDataUpdateCoordinator

PLATFORMS = [Platform.SENSOR]

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: AuroraAbbConfigEntry) -> bool:
    """Set up Fimer/ABB/Aurora Power-One from a config entry."""
    transport = entry.data[CONF_TRANSPORT]
    inverter_serial_address = entry.data[CONF_INVERTER_SERIAL_ADDRESS]

    if transport == TRANSPORT_SERIAL:
        client = AuroraClient.from_serial(
            inverter_serial_address=inverter_serial_address,
            serial_comport=entry.data[CONF_SERIAL_COMPORT],
        )
    elif transport == TRANSPORT_TCP:
        client = AuroraClient.from_tcp(
            inverter_serial_address=inverter_serial_address,
            tcp_host=entry.data[CONF_TCP_HOST],
            tcp_port=entry.data[CONF_TCP_PORT],
        )
    else:
        raise ConfigEntryError(f"Unsupported transport type: {transport}")

    coordinator = AuroraAbbDataUpdateCoordinator(hass, entry, client)
    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: AuroraAbbConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
