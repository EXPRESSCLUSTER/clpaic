# Tool definitions
TOOLS_DEFINITIONS = {

    # clpstat
    ## clpstat -s
    "show_cluster_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_cluster_status",
                "description": "Show cluster status",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "command": lambda args: "clpstat -s",
        "description": lambda args: "Show cluster status",
    },

    ## clpstat -g
    "show_group_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_group_status",
                "description": "Show group status (group map)",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "command": lambda args: "clpstat -g",
        "description": lambda args: "Show group status",
    },

    ## clpstat -m
    "show_monitor_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_monitor_status",
                "description": "Show monitor resources status",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "command": lambda args: "clpstat -m",
        "description": lambda args: "Show monitor resources status",
    },

    ## clpstat -n
    "show_heartbeat_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_heartbeat_status",
                "description": "Show heartbeat resources status",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "command": lambda args: "clpstat -n",
        "description": lambda args: "Show heartbeat resources status",
    },

    ## clpstat -f
    "show_fencing_status": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_fencing_status",
                "description": "Show fencing function status (which includes network partition resources and forced stop resources)",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "command": lambda args: "clpstat -f",
        "description": lambda args: "Show fencing function status",
    },

    ## clpstat --cl
    "show_cluster_config": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_cluster_config",
                "description": "Show cluster configuration",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "command": lambda args: "clpstat --cl",
        "description": lambda args: "Show cluster configuration",
    },

    ## clpstat --sv
    "show_server_config": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_server_config",
                "description": "Show the configuration of the specified server",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_name": {
                            "type": "string",
                            "description": "Name of the server to show configuration for"
                        }
                    },
                    "required": ["server_name"]
                }
            }
        },
        "command": lambda args: f"clpstat --sv {args['server_name']}",
        "description": lambda args: f"Show server configuration: {args['server_name']}",
    },

    ## clpstat --hb
    "show_heartbeat_config": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_heartbeat_config",
                "description": "Show the configuration of the specified heartbeat resource",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_name": {
                            "type": "string",
                            "description": "Name of the heartbeat resource to show configuration for"
                        }
                    },
                    "required": ["resource_name"]
                }
            }
        },
        "command": lambda args: f"clpstat --hb {args['resource_name']}",
        "description": lambda args: f"Show heartbeat resource configuration: {args['resource_name']}",
    },

    ## clpstat --fnc
    "show_fencing_config": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_fencing_config",
                "description": "Show the configuration of the specified fencing function (network partition resolution resource and forced stop resource)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_name": {
                            "type": "string",
                            "description": "Name of the fencing function resource to show configuration for"
                        }
                    },
                "required": ["resource_name"]
                }
            }
        },
        "command": lambda args: f"clpstat --fnc {args['resource_name']}",
        "description": lambda args: f"Show fencing function configuration: {args['resource_name']}",
    },

    ## clpstat --svg
    "show_servergroup_config": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_servergroup_config",
                "description": "Show the configuration of the specified server group",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "servergroup_name": {
                            "type": "string",
                            "description": "Name of the server group to show configuration for"
                        }
                    },
                    "required": ["servergroup_name"]
                }
            }
        },
        "command": lambda args: f"clpstat --svg {args['servergroup_name']}",
        "description": lambda args: f"Show server group configuration: {args['servergroup_name']}",
    },

    ## clpstat --grp
    "show_group_config": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_group_config",
                "description": "Show the configuration of the specified group",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_name": {
                            "type": "string",
                            "description": "Name of the group to show configuration for"
                        }
                    },
                    "required": ["group_name"]
                }
            }
        },
        "command": lambda args: f"clpstat --grp {args['group_name']}",
        "description": lambda args: f"Show group configuration: {args['group_name']}",
    },

    ## clpstat --rsc
    "show_resource_config": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_resource_config",
                "description": "Show the configuration of the specified group resource",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_name": {
                            "type": "string",
                            "description": "Name of the group resource to show configuration for"
                        }
                    },
                    "required": ["resource_name"]
                }
            }
        },
        "command": lambda args: f"clpstat --rsc {args['resource_name']}",
        "description": lambda args: f"Show group resource configuration: {args['resource_name']}",
    },

    ## clpstat --mon
    "show_monitor_config": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_monitor_config",
                "description": "Show the configuration of the specified monitor resource",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "monitor_name": {
                            "type": "string",
                            "description": "Name of the monitor resource to show configuration for"
                        }
                    },
                    "required": ["monitor_name"]
                }
            }
        },
        "command": lambda args: f"clpstat --mon {args['monitor_name']}",
        "description": lambda args: f"Show monitor resource configuration: {args['monitor_name']}",
    },

    ## clpstat --xcl
    "show_exclusive_rule_config": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_exclusive_rule_config",
                "description": "Show the configuration of the specified exclusive rule",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Name of the exclusive rule to show configuration for"
                        }
                    },
                    "required": ["name"]
                }
            }
        },
        "command": lambda args: f"clpstat --xcl {args['name']}",
        "description": lambda args: f"Show exclusive rule configuration: {args['name']}",
    },

    ## clpstat -i
    "show_all_config": {
        "schema": {
            "type": "function",
            "function": {
                "name": "show_all_config",
                "description": "Show all cluster configuration",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "command": lambda args: "clpstat -i",
        "description": lambda args: "Show all cluster configuration",
    },

    # clpcl
    ## clpcl -s
    "start_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "start_cluster",
                "description": "Start the cluster. Can be applied to this server only or all servers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "all_servers": {
                            "type": "boolean",
                            "description": "true to start on all servers, false to start on this server only"
                        }
                    },
                    "required": ["all_servers"]
                }
            }
        },
        "command": lambda args: "clpcl -s -a" if args["all_servers"] else "clpcl -s",
        "description": lambda args: "Start cluster: " + ("all servers" if args["all_servers"] else "this server"),
    },

    ## clpcl -t
    "stop_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "stop_cluster",
                "description": "Stop the cluster. Can be applied to this server only or all servers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "all_servers": {
                            "type": "boolean",
                            "description": "true to stop on all servers, false to stop on this server only"
                        }
                    },
                "required": ["all_servers"]
                }
            }
        },
        "command": lambda args: "clpcl -t -a" if args["all_servers"] else "clpcl -t",
        "description": lambda args: "Stop cluster: " + ("all servers" if args["all_servers"] else "this server"),
    },

    ## clpcl -r
    "restart_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "restart_cluster",
                "description": "Restart the CLUSTERPRO daemon. Can be applied to this server only or all servers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "all_servers": {
                            "type": "boolean",
                            "description": "true to restart on all servers, false to restart on this server only"
                        }
                    },
                    "required": ["all_servers"]
                }
            }
        },
        "command": lambda args: "clpcl -r -a" if args["all_servers"] else "clpcl -r",
        "description": lambda args: "Restart cluster: " + ("all servers" if args["all_servers"] else "this server"),
    },

    ## clpcl --suspend
    "suspend_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "suspend_cluster",
                "description": "Suspend the entire cluster",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "command": lambda args: "clpcl --suspend",
        "description": lambda args: "Suspend cluster",
    },

    ## clpcl --resume
    "resume_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "resume_cluster",
                "description": "Resume the entire cluster",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        "command": lambda args: "clpcl --resume",
        "description": lambda args: "Resume cluster",
    },

    # clpdown
    "shutdown_server": {
        "schema": {
            "type": "function",
            "function": {
                "name": "shutdown_server",
                "description": "Stop the CLUSTERPRO daemon and shut down or restart the server",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "restart": {
                            "type": "boolean",
                            "description": "true to restart the server, false to shut down the server"
                        }
                    },
                    "required": ["restart"]
                }
            }
        },
        "command": lambda args: "clpdown -r" if args["restart"] else "clpdown",
        "description": lambda args: "Restart server" if args["restart"] else "Shut down server",
    },

    # clpstdn
    "shutdown_cluster": {
        "schema": {
            "type": "function",
            "function": {
                "name": "shutdown_cluster",
                "description": "Shut down or restart the entire cluster",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "restart": {
                            "type": "boolean",
                            "description": "true to restart the cluster, false to shut down the cluster"
                        }
                    },
                    "required": ["restart"]
                }
            }
        },
        "command": lambda args: "clpstdn -r" if args["restart"] else "clpstdn",
        "description": lambda args: "Restart entire cluster" if args["restart"] else "Shut down entire cluster",
    },

    # clpgrp
    ## clpgrp -s
    "start_group": {
        "schema": {
            "type": "function",
            "function": {
                "name": "start_group",
                "description": "Start the specified group. If no group name is specified, all groups are started",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_name": {
                            "type": "string",
                            "description": "Name of the group to start. If omitted, all groups are started"
                        }
                    }
                },
                "required": []
            }
        },
        "command": lambda args: f"clpgrp -s {args['group_name']}" if args.get("group_name") else "clpgrp -s",
        "description": lambda args: f"Start group: {args['group_name']}" if args.get("group_name") else "Start all groups",
    },

    ## clpgrp -t
    "stop_group": {
        "schema": {
            "type": "function",
            "function": {
                "name": "stop_group",
                "description": "Stop the specified group. If no group name is specified, all groups are stopped",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_name": {
                            "type": "string",
                            "description": "Name of the group to stop. If omitted, all groups are stopped"
                        }
                    }
                },
                "required": []
            }
        },
        "command": lambda args: f"clpgrp -t {args['group_name']}" if args.get("group_name") else "clpgrp -t",
        "description": lambda args: f"Stop group: {args['group_name']}" if args.get("group_name") else "Stop all groups",
    },

    ## clpgrp -m
    "move_group": {
        "schema": {
            "type": "function",
            "function": {
                "name": "move_group",
                "description": "Move the specified group. If no group name is specified, all groups are moved. If a destination server is specified, the group is moved to that server; otherwise it is moved according to the failover policy",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_name": {
                            "type": "string",
                            "description": "Name of the group to move. If omitted, all groups are moved"
                        },
                        "destination": {
                            "type": "string",
                            "description": "Hostname of the destination server. If omitted, the group is moved according to the failover policy"
                        }
                    },
                    "required": []
                }
            }
        },
        "command": lambda args: (
            f"clpgrp -m {args['group_name']} -a {args['destination']}" if args.get("group_name") and args.get("destination") else
            f"clpgrp -m {args['group_name']}"                          if args.get("group_name") else
            f"clpgrp -m -a {args['destination']}"                      if args.get("destination") else
             "clpgrp -m"
        ),
        "description": lambda args: (
            f"Move group: {args['group_name']} -> {args['destination']}" if args.get("group_name") and args.get("destination") else
            f"Move group: {args['group_name']} (according to failover policy)" if args.get("group_name") else
            f"Move all groups -> {args['destination']}"                  if args.get("destination") else
             "Move all groups (according to failover policy)"
        ),
    },

    # clplogcc
    "collect_log": {
        "schema": {
            "type": "function",
            "function": {
                "name": "collect_log",
                "description": "Collect logs from servers. The log collection pattern and target servers (local only or all servers) can be specified",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pattern": {
                            "type": "string",
                            "enum": ["type1", "type2", "type3", "proactdiag"],
                            "description": "Log collection pattern. type1: default pattern, type2: wider scope than type1 for detailed log collection, type3: narrower scope than type1 for minimal log collection, proactdiag: for proactive diagnosis service. Defaults to type1 if omitted"
                        },
                        "local_only": {
                            "type": "boolean",
                            "description": "true to collect logs from the local server only. false or omitted to collect logs from all servers"
                        }
                    },
                    "required": []
                }
            }
        },
        "command": lambda args: "clplogcc" + (f" -t {args['pattern']}" if args.get("pattern") else " -t type1") + (" -l" if args.get("local_only") else ""),
        "description": lambda args: "Collect logs"
            + f" pattern: {args.get('pattern', 'type1')}"
            + (" local only" if args.get("local_only") else " all servers"),
    },

    # clprsc

    # clpmonctrl

}

# Common property definitions
_COMMON_PROPERTIES = {
    # -h
    "hostname": {
        "type": "string",
        "description": "Hostname of the server to send the request to. If omitted, the request is sent to the local server"
    }
}


def _build_tools(definitions):
    tools = []
    for defn in definitions.values():
        schema = defn["schema"]
        # Inject common properties into each schema
        schema["function"]["parameters"]["properties"].update(_COMMON_PROPERTIES)
        tools.append(schema)
    return tools


TOOLS = _build_tools(TOOLS_DEFINITIONS)
