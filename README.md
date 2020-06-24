# apama-kasa-plugin
Apama EPL plug-in for using Wake On Lan

## Prerequisites

This plug-in works with Apama 10.5 or later. You can download Apama from http://apamacommunity.com/ . You will also need to add the `wakeonlan` module to the Python in your Apama installation, either by adding a virtual environment, or by installing it from an Apama command prompt:

    pip install wakeonlan

## Using this plug-in from EPL

To use this plug-in to control Kasa devices from EPL, first you need to add the plug-in to your correlator configuration YAML:

	eplPlugins:
	   WoLPlugin:
	      pythonFile: "${PARENT_DIR}/wol.py"
	      class: WakeOnLanePluginClass

Secondly, add `WakeOnLan.mon` to your project.

## Documentation

ApamaDoc documentation can be found in the [doc](https://mjj29.github.io/apama-wake-on-lan-plugin/docs/) sub directory.

## Licence

The Apama EPL Wake On Lan Plug-in is licensed under the Apache 2.0 license.
