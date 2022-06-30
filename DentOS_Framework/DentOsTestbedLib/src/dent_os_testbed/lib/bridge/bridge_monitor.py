# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/network/bridge/bridge.yaml
#
# DONOT EDIT - generated by diligent bots

import pytest
from dent_os_testbed.lib.bridge.linux.linux_bridge_monitor_impl import LinuxBridgeMonitorImpl
from dent_os_testbed.lib.test_lib_object import TestLibObject


class BridgeMonitor(TestLibObject):
    """
    The bridge utility can monitor the state of devices and addresses continuously.
    """

    async def _run_command(api, *argv, **kwarg):
        devices = kwarg["input_data"]
        result = list()
        for device in devices:
            for device_name in device:
                device_result = {device_name: dict()}
                # device lookup
                if "device_obj" in kwarg:
                    device_obj = kwarg.get("device_obj", None)[device_name]
                else:
                    if device_name not in pytest.testbed.devices_dict:
                        device_result[device_name] = "No matching device " + device_name
                        result.append(device_result)
                        return result
                    device_obj = pytest.testbed.devices_dict[device_name]
                commands = ""
                if device_obj.os in ["dentos", "cumulus"]:
                    impl_obj = LinuxBridgeMonitorImpl()
                    for command in device[device_name]:
                        commands += impl_obj.format_command(command=api, params=command)
                        commands += "&& "
                    commands = commands[:-3]

                else:
                    device_result[device_name]["rc"] = -1
                    device_result[device_name]["result"] = "No matching device OS " + device_obj.os
                    result.append(device_result)
                    return result
                device_result[device_name]["command"] = commands
                try:
                    rc, output = await device_obj.run_cmd(
                        ("sudo " if device_obj.ssh_conn_params.pssh else "") + commands
                    )
                    device_result[device_name]["rc"] = rc
                    device_result[device_name]["result"] = output
                    if "parse_output" in kwarg:
                        parse_output = impl_obj.parse_output(
                            command=api, output=output, commands=commands
                        )
                        device_result[device_name]["parsed_output"] = parse_output
                except Exception as e:
                    device_result[device_name]["rc"] = -1
                    device_result[device_name]["result"] = str(e)
                result.append(device_result)
        return result

    async def monitor(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        BridgeMonitor.monitor(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'options':'string',
                }],
            }],
        )
        Description:
        bridge monitor [ all | neigh | link | mdb ]

        """
        return await BridgeMonitor._run_command("monitor", *argv, **kwarg)
