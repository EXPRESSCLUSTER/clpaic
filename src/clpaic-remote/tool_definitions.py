TOOLS_DEFINITIONS = {

    "get_cluster_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_cluster_status",
                "description": "Get cluster status information including cluster name and operational state. Use to check if the cluster is running normally.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: "/api/v1/cluster",
        "body": lambda args: None,
        "description": lambda args: "Get cluster status",
    },

    "get_cluster_toratio": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_cluster_toratio",
                "description": "Get the current timeout ratio value for the cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: "/api/v1/cluster/toratio",
        "body": lambda args: None,
        "description": lambda args: "Get cluster timeout ratio",
    },

    "get_server_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_server_status",
                "description": "Get server status information. If servername is specified, returns status for that server only. Otherwise returns all servers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "servername": {
                            "type": "string",
                            "description": "Name of the server. If omitted, all servers are returned."
                        }
                    },
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: f"/api/v1/servers/{args['servername']}" if args.get("servername") else "/api/v1/servers",
        "body": lambda args: None,
        "description": lambda args: f"Get server status: {args['servername']}" if args.get("servername") else "Get all servers status",
    },

    "get_server_names": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_server_names",
                "description": "Get a list of all server names in the cluster. Returns only names without status information.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: "/api/v1/servers?select=name",
        "body": lambda args: None,
        "description": lambda args: "Get server names",
    },

    "get_group_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_group_status",
                "description": "Get failover group status. If groupname is specified, returns status for that group only. Otherwise returns all groups.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "groupname": {
                            "type": "string",
                            "description": "Name of the group. If omitted, all groups are returned."
                        }
                    },
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: f"/api/v1/groups/{args['groupname']}" if args.get("groupname") else "/api/v1/groups",
        "body": lambda args: None,
        "description": lambda args: f"Get group status: {args['groupname']}" if args.get("groupname") else "Get all groups status",
    },

    "get_group_names": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_group_names",
                "description": "Get a list of all group names. Returns only names without status information.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: "/api/v1/groups?select=name",
        "body": lambda args: None,
        "description": lambda args: "Get group names",
    },

    "get_group_resources": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_group_resources",
                "description": "Get the list of resource names belonging to a specific group. The groupname is required.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "groupname": {
                            "type": "string",
                            "description": "Name of the group to get resources for."
                        }
                    },
                    "required": ["groupname"]
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: f"/api/v1/groups/{args['groupname']}?select=resources",
        "body": lambda args: None,
        "description": lambda args: f"Get resources for group: {args['groupname']}",
    },

    "get_resource_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_resource_status",
                "description": "Get group resource status. If resourcename is specified, returns status for that resource only. Otherwise returns all resources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resourcename": {
                            "type": "string",
                            "description": "Name of the group resource. If omitted, all resources are returned."
                        }
                    },
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: f"/api/v1/resources/{args['resourcename']}" if args.get("resourcename") else "/api/v1/resources",
        "body": lambda args: None,
        "description": lambda args: f"Get resource status: {args['resourcename']}" if args.get("resourcename") else "Get all resources status",
    },

    "get_resource_names": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_resource_names",
                "description": "Get a list of all group resource names. Returns only names without status information.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: "/api/v1/resources?select=name",
        "body": lambda args: None,
        "description": lambda args: "Get resource names",
    },

    "get_monitor_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_monitor_status",
                "description": "Get monitor resource status. If monitorname is specified, returns status for that monitor only. Otherwise returns all monitors.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "monitorname": {
                            "type": "string",
                            "description": "Name of the monitor resource. If omitted, all monitors are returned."
                        }
                    },
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: f"/api/v1/monitors/{args['monitorname']}" if args.get("monitorname") else "/api/v1/monitors",
        "body": lambda args: None,
        "description": lambda args: f"Get monitor status: {args['monitorname']}" if args.get("monitorname") else "Get all monitors status",
    },

    "get_monitor_names": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_monitor_names",
                "description": "Get a list of all monitor resource names. Returns only names without status information.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: "/api/v1/monitors?select=name",
        "body": lambda args: None,
        "description": lambda args: "Get monitor names",
    },

    "start_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "start_cluster",
                "description": "Start the cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/cluster/start",
        "body": lambda args: None,
        "description": lambda args: "Start cluster",
    },

    "stop_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "stop_cluster",
                "description": "Stop the cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/cluster/stop",
        "body": lambda args: None,
        "description": lambda args: "Stop cluster",
    },

    "reboot_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "reboot_cluster",
                "description": "Reboot the cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/cluster/reboot",
        "body": lambda args: None,
        "description": lambda args: "Reboot cluster",
    },

    "shutdown_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "shutdown_cluster",
                "description": "Shutdown the entire cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/cluster/shutdown",
        "body": lambda args: None,
        "description": lambda args: "Shutdown cluster",
    },

    "suspend_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "suspend_cluster",
                "description": "Suspend the cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/cluster/suspend",
        "body": lambda args: None,
        "description": lambda args: "Suspend cluster",
    },

    "resume_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "resume_cluster",
                "description": "Resume a suspended cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/cluster/resume",
        "body": lambda args: None,
        "description": lambda args: "Resume cluster",
    },

    "set_cluster_toratio": {
        "schema": {
            "type": "function",
            "function": {
                "name": "set_cluster_toratio",
                "description": "Set the timeout ratio for the cluster. Temporarily extends various timeout values (monitor resources, heartbeat resources, etc.). Specify ratio=1 to reset to default (time must not be specified in that case).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ratio": {
                            "type": "integer",
                            "description": "Timeout ratio (1-10000). Specify 1 to reset to default."
                        },
                        "time": {
                            "type": "string",
                            "description": "Duration for the extension. Specify in minutes(m), hours(h), or days(d). e.g. '2m', '3h', '4d'. Max 30 days. Must not be specified when ratio=1."
                        }
                    },
                    "required": ["ratio"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/cluster/toratio/set",
        "body": lambda args: {k: v for k, v in {"ratio": args.get("ratio"), "time": args.get("time")}.items() if v is not None},
        "description": lambda args: f"Set cluster timeout ratio to {args.get('ratio')}" + (f" for {args.get('time')}" if args.get("time") else ""),
    },

    "reset_cluster_toratio": {
        "schema": {
            "type": "function",
            "function": {
                "name": "reset_cluster_toratio",
                "description": "Reset the timeout ratio to the original configured value.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/cluster/toratio/reset",
        "body": lambda args: None,
        "description": lambda args: "Reset cluster timeout ratio",
    },

    "start_server_service": {
        "schema": {
            "type": "function",
            "function": {
                "name": "start_server_service",
                "description": "Start the CLUSTERPRO service on the specified server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "servername": {
                            "type": "string",
                            "description": "Name of the server to start."
                        }
                    },
                    "required": ["servername"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/servers/{args['servername']}/start",
        "body": lambda args: None,
        "description": lambda args: f"Start server service: {args['servername']}",
    },

    "stop_server_service": {
        "schema": {
            "type": "function",
            "function": {
                "name": "stop_server_service",
                "description": "Stop the CLUSTERPRO service on the specified server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "servername": {
                            "type": "string",
                            "description": "Name of the server to stop."
                        }
                    },
                    "required": ["servername"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/servers/{args['servername']}/stop",
        "body": lambda args: None,
        "description": lambda args: f"Stop server service: {args['servername']}",
    },

    "reboot_server": {
        "schema": {
            "type": "function",
            "function": {
                "name": "reboot_server",
                "description": "Reboot the specified server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "servername": {
                            "type": "string",
                            "description": "Name of the server to reboot."
                        }
                    },
                    "required": ["servername"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/servers/{args['servername']}/reboot",
        "body": lambda args: None,
        "description": lambda args: f"Reboot server: {args['servername']}",
    },

    "shutdown_server": {
        "schema": {
            "type": "function",
            "function": {
                "name": "shutdown_server",
                "description": "Shutdown the specified server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "servername": {
                            "type": "string",
                            "description": "Name of the server to shutdown."
                        }
                    },
                    "required": ["servername"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/servers/{args['servername']}/shutdown",
        "body": lambda args: None,
        "description": lambda args: f"Shutdown server: {args['servername']}",
    },

    "start_server_dummy_failure": {
        "schema": {
            "type": "function",
            "function": {
                "name": "start_server_dummy_failure",
                "description": "Start a dummy failure on the specified server. Used for failure testing and verification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "servername": {
                            "type": "string",
                            "description": "Name of the server to start dummy failure on."
                        }
                    },
                    "required": ["servername"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/servers/{args['servername']}/dummy-failure/start",
        "body": lambda args: None,
        "description": lambda args: f"Start dummy failure on server: {args['servername']}",
    },

    "stop_server_dummy_failure": {
        "schema": {
            "type": "function",
            "function": {
                "name": "stop_server_dummy_failure",
                "description": "Stop (clear) the dummy failure on the specified server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "servername": {
                            "type": "string",
                            "description": "Name of the server to stop dummy failure on."
                        }
                    },
                    "required": ["servername"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/servers/{args['servername']}/dummy-failure/stop",
        "body": lambda args: None,
        "description": lambda args: f"Stop dummy failure on server: {args['servername']}",
    },

    "start_group": {
        "schema": {
            "type": "function",
            "function": {
                "name": "start_group",
                "description": "Start a failover group. If groupname is omitted, starts all startable groups on the target server. If groupname is specified, starts that specific group on the target server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "groupname": {
                            "type": "string",
                            "description": "Name of the group to start. If omitted, all groups on the target server are started."
                        },
                        "target": {
                            "type": "string",
                            "description": "Name of the server to start the group on."
                        }
                    },
                    "required": ["target"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/groups/{args['groupname']}/start" if args.get("groupname") else "/api/v1/groups/start",
        "body": lambda args: {"target": args["target"]},
        "description": lambda args: f"Start group {args['groupname']} on {args['target']}" if args.get("groupname") else f"Start all groups on {args['target']}",
    },

    "stop_group": {
        "schema": {
            "type": "function",
            "function": {
                "name": "stop_group",
                "description": "Stop a failover group. If groupname is omitted, stops all groups on the target server (target is required). If groupname is specified, stops that group (target is optional).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "groupname": {
                            "type": "string",
                            "description": "Name of the group to stop. If omitted, all groups on the target server are stopped."
                        },
                        "target": {
                            "type": "string",
                            "description": "Name of the server where the group is running. Required when groupname is omitted."
                        }
                    },
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/groups/{args['groupname']}/stop" if args.get("groupname") else "/api/v1/groups/stop",
        "body": lambda args: {"target": args["target"]} if args.get("target") else None,
        "description": lambda args: f"Stop group {args['groupname']}" + (f" on {args['target']}" if args.get("target") else "") if args.get("groupname") else f"Stop all groups on {args.get('target', '(unspecified)')}",
    },

    "move_group": {
        "schema": {
            "type": "function",
            "function": {
                "name": "move_group",
                "description": "Move a failover group to another server. If target is omitted, moves according to the failover policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "groupname": {
                            "type": "string",
                            "description": "Name of the group to move."
                        },
                        "target": {
                            "type": "string",
                            "description": "Name of the destination server. If omitted, moves according to failover policy."
                        }
                    },
                    "required": ["groupname"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/groups/{args['groupname']}/move",
        "body": lambda args: {"target": args["target"]} if args.get("target") else None,
        "description": lambda args: f"Move group {args['groupname']}" + (f" to {args['target']}" if args.get("target") else " (failover policy)"),
    },

    "start_resource": {
        "schema": {
            "type": "function",
            "function": {
                "name": "start_resource",
                "description": "Start a group resource. Dependent stopped resources will also be started.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resourcename": {
                            "type": "string",
                            "description": "Name of the group resource to start."
                        },
                        "target": {
                            "type": "string",
                            "description": "Name of the server to start the resource on."
                        }
                    },
                    "required": ["resourcename", "target"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/resources/{args['resourcename']}/start",
        "body": lambda args: {"target": args["target"]},
        "description": lambda args: f"Start resource {args['resourcename']} on {args['target']}",
    },

    "stop_resource": {
        "schema": {
            "type": "function",
            "function": {
                "name": "stop_resource",
                "description": "Stop a group resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resourcename": {
                            "type": "string",
                            "description": "Name of the group resource to stop."
                        }
                    },
                    "required": ["resourcename"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/resources/{args['resourcename']}/stop",
        "body": lambda args: None,
        "description": lambda args: f"Stop resource {args['resourcename']}",
    },

    "resume_monitor": {
        "schema": {
            "type": "function",
            "function": {
                "name": "resume_monitor",
                "description": "Resume a suspended monitor resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "monitorname": {
                            "type": "string",
                            "description": "Name of the monitor resource to resume."
                        },
                        "target": {
                            "type": "string",
                            "description": "Name of the server to resume the monitor on."
                        }
                    },
                    "required": ["monitorname", "target"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/monitors/{args['monitorname']}/resume",
        "body": lambda args: {"target": args["target"]},
        "description": lambda args: f"Resume monitor {args['monitorname']} on {args['target']}",
    },

    "suspend_monitor": {
        "schema": {
            "type": "function",
            "function": {
                "name": "suspend_monitor",
                "description": "Suspend a monitor resource. Use for maintenance. Resume with resume_monitor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "monitorname": {
                            "type": "string",
                            "description": "Name of the monitor resource to suspend."
                        },
                        "target": {
                            "type": "string",
                            "description": "Name of the server to suspend the monitor on."
                        }
                    },
                    "required": ["monitorname", "target"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/monitors/{args['monitorname']}/suspend",
        "body": lambda args: {"target": args["target"]},
        "description": lambda args: f"Suspend monitor {args['monitorname']} on {args['target']}",
    },

    "start_monitor_dummy_failure": {
        "schema": {
            "type": "function",
            "function": {
                "name": "start_monitor_dummy_failure",
                "description": "Start a dummy failure on the specified monitor resource. Specify target as empty string to apply to all servers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "monitorname": {
                            "type": "string",
                            "description": "Name of the monitor resource."
                        },
                        "target": {
                            "type": "string",
                            "description": "Server name to start dummy failure on. Use empty string for all servers."
                        }
                    },
                    "required": ["monitorname", "target"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/monitors/{args['monitorname']}/dummy-failure/start",
        "body": lambda args: {"target": args["target"]},
        "description": lambda args: f"Start dummy failure on monitor {args['monitorname']}" + (f" on {args['target']}" if args["target"] else " on all servers"),
    },

    "stop_monitor_dummy_failure": {
        "schema": {
            "type": "function",
            "function": {
                "name": "stop_monitor_dummy_failure",
                "description": "Stop (clear) the dummy failure on the specified monitor resource. Specify target as empty string to apply to all servers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "monitorname": {
                            "type": "string",
                            "description": "Name of the monitor resource."
                        },
                        "target": {
                            "type": "string",
                            "description": "Server name to stop dummy failure on. Use empty string for all servers."
                        }
                    },
                    "required": ["monitorname", "target"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: f"/api/v1/monitors/{args['monitorname']}/dummy-failure/stop",
        "body": lambda args: {"target": args["target"]},
        "description": lambda args: f"Stop dummy failure on monitor {args['monitorname']}" + (f" on {args['target']}" if args["target"] else " on all servers"),
    },

    "run_script": {
        "schema": {
            "type": "function",
            "function": {
                "name": "run_script",
                "description": "Execute a script on a CLUSTERPRO server. The script must be placed in the work/rexec/ directory under the CLUSTERPRO installation directory on the target server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "script": {
                            "type": "string",
                            "description": "Script filename to execute (e.g. 'script.bat')."
                        },
                        "target": {
                            "type": "string",
                            "description": "IP address of the CLUSTERPRO server to execute the script on."
                        },
                        "timeout": {
                            "type": "integer",
                            "description": "API timeout in seconds. Default is 180."
                        },
                        "logdir": {
                            "type": "string",
                            "description": "Output file path for execution log. If omitted, no log is output."
                        }
                    },
                    "required": ["script", "target"]
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/scripts/run",
        "body": lambda args: {k: v for k, v in {"script": args["script"], "target": args["target"], "timeout": args.get("timeout"), "logdir": args.get("logdir")}.items() if v is not None},
        "description": lambda args: f"Run script {args['script']} on {args['target']}",
    },

    "get_groups_uptime": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_groups_uptime",
                "description": "Get the continuous uptime of failover groups. If groupname is specified, returns uptime for that group only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "groupname": {
                            "type": "string",
                            "description": "Name of the group. If omitted, all groups are returned."
                        }
                    },
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: f"/api/v1/metrics/groups/{args['groupname']}/uptime" if args.get("groupname") else "/api/v1/metrics/groups/uptime",
        "body": lambda args: None,
        "description": lambda args: f"Get uptime for group: {args['groupname']}" if args.get("groupname") else "Get uptime for all groups",
    },

    "get_config_last_applied_date": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_config_last_applied_date",
                "description": "Get the date and time when the cluster configuration was last applied, in ISO 8601 format.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: "/api/v1/metrics/config/last-applied-date",
        "body": lambda args: None,
        "description": lambda args: "Get config last applied date",
    },

    "mirror_backup_preaction": {
        "schema": {
            "type": "function",
            "function": {
                "name": "mirror_backup_preaction",
                "description": "Execute pre-action for mirror/hybrid disk backup. Runs asynchronously. Check status with get_mirror_backup_status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "no-shutdown": {
                            "type": "boolean",
                            "description": "If true, equivalent to --no-shutdown option."
                        },
                        "no-reboot": {
                            "type": "boolean",
                            "description": "If true, equivalent to --no-reboot option."
                        },
                        "only-shutdown": {
                            "type": "boolean",
                            "description": "If true, equivalent to --only-shutdown option."
                        },
                        "only-reboot": {
                            "type": "boolean",
                            "description": "If true, equivalent to --only-reboot option."
                        },
                        "online": {
                            "type": "boolean",
                            "description": "If true, equivalent to --online option."
                        },
                        "timeout": {
                            "type": "integer",
                            "description": "Timeout in seconds for clpbackup. Default is 900."
                        }
                    },
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/mirrors/backup/preaction",
        "body": lambda args: {k: v for k, v in args.items() if v is not None} or None,
        "description": lambda args: "Mirror backup pre-action",
    },

    "mirror_backup_postaction": {
        "schema": {
            "type": "function",
            "function": {
                "name": "mirror_backup_postaction",
                "description": "Execute post-action for mirror/hybrid disk backup. Runs asynchronously. Check status with get_mirror_backup_status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "no-shutdown": {
                            "type": "boolean",
                            "description": "If true, equivalent to --no-shutdown option."
                        },
                        "no-reboot": {
                            "type": "boolean",
                            "description": "If true, equivalent to --no-reboot option."
                        },
                        "only-shutdown": {
                            "type": "boolean",
                            "description": "If true, equivalent to --only-shutdown option."
                        },
                        "only-reboot": {
                            "type": "boolean",
                            "description": "If true, equivalent to --only-reboot option."
                        },
                        "online": {
                            "type": "boolean",
                            "description": "If true, equivalent to --online option."
                        },
                        "timeout": {
                            "type": "integer",
                            "description": "Timeout in seconds for clpbackup. Default is 900."
                        }
                    },
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/mirrors/backup/postaction",
        "body": lambda args: {k: v for k, v in args.items() if v is not None} or None,
        "description": lambda args: "Mirror backup post-action",
    },

    "mirror_restore_preaction": {
        "schema": {
            "type": "function",
            "function": {
                "name": "mirror_restore_preaction",
                "description": "Execute pre-action for mirror/hybrid disk restore. Runs asynchronously. Check status with get_mirror_restore_status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "no-shutdown": {
                            "type": "boolean",
                            "description": "If true, equivalent to --no-shutdown option."
                        },
                        "no-reboot": {
                            "type": "boolean",
                            "description": "If true, equivalent to --no-reboot option."
                        },
                        "only-shutdown": {
                            "type": "boolean",
                            "description": "If true, equivalent to --only-shutdown option."
                        },
                        "only-reboot": {
                            "type": "boolean",
                            "description": "If true, equivalent to --only-reboot option."
                        },
                        "skip-copy": {
                            "type": "boolean",
                            "description": "If true, equivalent to --skip-copy option."
                        },
                        "online": {
                            "type": "boolean",
                            "description": "If true, equivalent to --online option."
                        },
                        "timeout": {
                            "type": "integer",
                            "description": "Timeout in seconds for clprestore. Default is 900."
                        }
                    },
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/mirrors/restore/preaction",
        "body": lambda args: {k: v for k, v in args.items() if v is not None} or None,
        "description": lambda args: "Mirror restore pre-action",
    },

    "mirror_restore_postaction": {
        "schema": {
            "type": "function",
            "function": {
                "name": "mirror_restore_postaction",
                "description": "Execute post-action for mirror/hybrid disk restore. Runs asynchronously. Check status with get_mirror_restore_status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "no-shutdown": {
                            "type": "boolean",
                            "description": "If true, equivalent to --no-shutdown option."
                        },
                        "no-reboot": {
                            "type": "boolean",
                            "description": "If true, equivalent to --no-reboot option."
                        },
                        "only-shutdown": {
                            "type": "boolean",
                            "description": "If true, equivalent to --only-shutdown option."
                        },
                        "only-reboot": {
                            "type": "boolean",
                            "description": "If true, equivalent to --only-reboot option."
                        },
                        "skip-copy": {
                            "type": "boolean",
                            "description": "If true, equivalent to --skip-copy option."
                        },
                        "online": {
                            "type": "boolean",
                            "description": "If true, equivalent to --online option."
                        },
                        "timeout": {
                            "type": "integer",
                            "description": "Timeout in seconds for clprestore. Default is 900."
                        }
                    },
                    "required": []
                }
            }
        },
        "method": "POST",
        "endpoint": lambda args: "/api/v1/mirrors/restore/postaction",
        "body": lambda args: {k: v for k, v in args.items() if v is not None} or None,
        "description": lambda args: "Mirror restore post-action",
    },

    "get_mirror_backup_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_mirror_backup_status",
                "description": "Get the execution status/result of mirror_backup_preaction or mirror_backup_postaction. Check detail.status for 'running' or completion message.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: "/api/v1/mirrors/backup/status",
        "body": lambda args: None,
        "description": lambda args: "Get mirror backup status",
    },

    "get_mirror_restore_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_mirror_restore_status",
                "description": "Get the execution status/result of mirror_restore_preaction or mirror_restore_postaction. Check detail.status for 'running' or completion message.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "method": "GET",
        "endpoint": lambda args: "/api/v1/mirrors/restore/status",
        "body": lambda args: None,
        "description": lambda args: "Get mirror restore status",
    },
}


def _build_tools(definitions):
    tools = []
    for defn in definitions.values():
        tools.append(defn["schema"])
    return tools


TOOLS = _build_tools(TOOLS_DEFINITIONS)
