# Fimer/ABB/Aurora Power-One PVI Inverter

[![hassfest](https://github.com/marhali/ha-fimer-abb-aurora-power-one-pvi/actions/workflows/hassfest.yml/badge.svg)](https://github.com/marhali/ha-fimer-abb-aurora-power-one-pvi/actions/workflows/hassfest.yml)
[![HACS Validation](https://github.com/marhali/ha-fimer-abb-aurora-power-one-pvi/actions/workflows/hacs.yml/badge.svg)](https://github.com/marhali/ha-fimer-abb-aurora-power-one-pvi/actions/workflows/hacs.yml)
[![Tests](https://github.com/marhali/ha-fimer-abb-aurora-power-one-pvi/actions/workflows/test.yml/badge.svg)](https://github.com/marhali/ha-fimer-abb-aurora-power-one-pvi/actions/workflows/test.yml)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

A [HACS](https://hacs.xyz/) custom integration for Home Assistant to monitor Fimer/ABB/Aurora Power-One solar inverters, supporting both **Serial (RS485/USB)** and **TCP (Ethernet-to-RS485 gateway)** connections.

## Relationship to Home Assistant core

Home Assistant core ships a built-in [`aurora_abb_powerone`](https://www.home-assistant.io/integrations/aurora_abb_powerone/) integration, but it only supports serial connections. This repository ports the TCP transport support from an open, unmerged upstream pull request — [home-assistant/core#166785](https://github.com/home-assistant/core/pull/166785) — into an independent HACS integration with its own domain (`fimer_abb_aurora_power_one_pvi`), so it can be installed and used today without waiting for that PR to be reviewed and merged, and can coexist on the same Home Assistant instance alongside the core integration if needed.

This project is **not affiliated with or endorsed by** the Home Assistant core team.

## Features

- Config flow setup via the Home Assistant UI — no YAML required
- **Serial** transport: connect via an RS485 or USB-to-RS485 adaptor
- **TCP** transport: connect via an Ethernet-to-RS485 gateway
- Sensors: grid voltage/current/frequency, output power, DC leak currents, string 1/2 power/voltage/current, temperature, isolation resistance, cumulative energy, alarm state

## Installation

### Via HACS (recommended)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=marhali&repository=ha-fimer-abb-aurora-power-one-pvi&category=integration)

Click the badge above to add this repository directly in your Home Assistant instance, or do it manually:

1. In Home Assistant, open **HACS**.
2. Go to the three-dot menu → **Custom repositories**.
3. Add repository URL `https://github.com/marhali/ha-fimer-abb-aurora-power-one-pvi`, category **Integration**.
4. Find **Fimer/ABB/Aurora Power-One PVI Inverter** in HACS and install it.
5. Restart Home Assistant.

### Manual

Copy `custom_components/fimer_abb_aurora_power_one_pvi` into your Home Assistant `custom_components` directory and restart Home Assistant.

## Configuration

1. Go to **Settings → Devices & Services → Add Integration**.
2. Search for **Fimer/ABB/Aurora Power-One**.
3. Choose a transport:
   - **Serial (RS485)**: select the serial port and the inverter's address (as configured on its LCD panel).
   - **TCP (Ethernet gateway)**: enter the gateway's IP address/hostname, TCP port, and the inverter's address.
4. Home Assistant connects to the inverter to fetch its identifier and creates the config entry.

## Protocol references

- [Inverter manual](https://s1.solacity.com/docs/PVI-3.0-3.6-4.2-OUTD-US%20Manual.pdf)
- [Aurora communication protocol](http://www.drhack.it/images/PDF/AuroraCommunicationProtocol_4_2.pdf)
- [Serial address range reference](https://library.e.abb.com/public/e57212c407344a16b4644cee73492b39/PVI-3.0_3.6_4.2-TL-OUTD-Product%20manual%20EN-RevB(M000016BG).pdf)

## Troubleshooting

- **"Unable to connect"**: check connection settings, electrical connection, and that the inverter is on (it may be dark/off at night).
- **"Cannot open serial port"**: check the serial port and permissions, and try again.
- **"Serial port is not a valid device"**: the selected serial port could not be opened — verify the adaptor is connected.
- **"No com ports found"**: the integration needs a valid RS485 device to communicate over serial; use the TCP transport instead if you're using an Ethernet gateway.

## Contributing / running tests locally

```bash
pip install -r requirements_test.txt
pytest tests -v
```

## License

Licensed under the [Apache License, Version 2.0](LICENSE). This project is derived in part from `home-assistant/core` — see [NOTICE](NOTICE) for attribution.
