# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/network/tc/tc.yaml
#
# DONOT EDIT - generated by diligent bots

import pytest
from dent_os_testbed.lib.tc.linux.linux_tc_filter_impl import LinuxTcFilterImpl
from dent_os_testbed.lib.test_lib_object import TestLibObject


class TcFilter(TestLibObject):
    """
    - tc [ OPTIONS ] filter [ add | change | replace | delete | get ] dev DEV [ parent qdisc-id | root]
    [ handle filter-id ] protocol protocol prio priority filtertype [ filtertype specific parameters ]
    flowid flow-id
    - tc [ OPTIONS ] filter [ add | change | replace | delete | get ] block BLOCK_INDEX [ handle filter-id ]
    protocol protocol prio priority filtertype [ filtertype specific parameters ] flowid flow-id
    - tc [ OPTIONS ] filter show dev DEV
    - tc [ OPTIONS ] filter show block BLOCK_INDEX
    OPTIONS := { [ -force ] -b[atch] [ filename ] | [ -n[etns] name ] | [ -nm | -nam[es] ] |
      [ { -cf | -c[onf] } [ filename ] ] [ -t[imestamp] ] | [ -t[short] | [ -o[neline] ] }

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
                    impl_obj = LinuxTcFilterImpl()
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

    async def add(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcFilter.add(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'root':'bool',
                        'handle':'int',
                        'protocol':'string',
                        'prio':'int',
                        'filtertype':'string',
                        'flowid':'int',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] filter [ add | change | replace | delete | get ] dev DEV  [  parent
        qdisc-id  | root ] [ handle filter-id ] protocol protocol prio priority filtertype
        [ filtertype specific parameters ] flowid flow-id
        tc [ OPTIONS ] filter [ add | change | replace | delete | get ] block  BLOCK_INDEX
        [  handle filter-id ] protocol protocol prio priority filtertype [ filtertype spe
        cific parameters ] flowid flow-id

        """
        return await TcFilter._run_command("add", *argv, **kwarg)

    async def change(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcFilter.change(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'root':'bool',
                        'handle':'int',
                        'protocol':'string',
                        'prio':'int',
                        'filtertype':'string',
                        'flowid':'int',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] filter [ add | change | replace | delete | get ] dev DEV  [  parent
        qdisc-id  | root ] [ handle filter-id ] protocol protocol prio priority filtertype
        [ filtertype specific parameters ] flowid flow-id
        tc [ OPTIONS ] filter [ add | change | replace | delete | get ] block  BLOCK_INDEX
        [  handle filter-id ] protocol protocol prio priority filtertype [ filtertype spe
        cific parameters ] flowid flow-id

        """
        return await TcFilter._run_command("change", *argv, **kwarg)

    async def replace(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcFilter.replace(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'root':'bool',
                        'handle':'int',
                        'protocol':'string',
                        'prio':'int',
                        'filtertype':'string',
                        'flowid':'int',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] filter [ add | change | replace | delete | get ] dev DEV  [  parent
        qdisc-id  | root ] [ handle filter-id ] protocol protocol prio priority filtertype
        [ filtertype specific parameters ] flowid flow-id
        tc [ OPTIONS ] filter [ add | change | replace | delete | get ] block  BLOCK_INDEX
        [  handle filter-id ] protocol protocol prio priority filtertype [ filtertype spe
        cific parameters ] flowid flow-id

        """
        return await TcFilter._run_command("replace", *argv, **kwarg)

    async def delete(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcFilter.delete(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'root':'bool',
                        'handle':'int',
                        'protocol':'string',
                        'prio':'int',
                        'filtertype':'string',
                        'flowid':'int',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] filter [ add | change | replace | delete | get ] dev DEV  [  parent
        qdisc-id  | root ] [ handle filter-id ] protocol protocol prio priority filtertype
        [ filtertype specific parameters ] flowid flow-id
        tc [ OPTIONS ] filter [ add | change | replace | delete | get ] block  BLOCK_INDEX
        [  handle filter-id ] protocol protocol prio priority filtertype [ filtertype spe
        cific parameters ] flowid flow-id

        """
        return await TcFilter._run_command("delete", *argv, **kwarg)

    async def get(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcFilter.get(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'root':'bool',
                        'handle':'int',
                        'protocol':'string',
                        'prio':'int',
                        'filtertype':'string',
                        'flowid':'int',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] filter [ add | change | replace | delete | get ] dev DEV  [  parent
        qdisc-id  | root ] [ handle filter-id ] protocol protocol prio priority filtertype
        [ filtertype specific parameters ] flowid flow-id
        tc [ OPTIONS ] filter [ add | change | replace | delete | get ] block  BLOCK_INDEX
        [  handle filter-id ] protocol protocol prio priority filtertype [ filtertype spe
        cific parameters ] flowid flow-id

        """
        return await TcFilter._run_command("get", *argv, **kwarg)

    async def show(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcFilter.show(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'block':'int',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] filter show dev DEV
        tc [ OPTIONS ] filter show block BLOCK_INDEX

        """
        return await TcFilter._run_command("show", *argv, **kwarg)
