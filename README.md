# clpaic
AI chat assistant for operating EXPRESSCLUSTER through natural language commands.

## Overview

This repository contains a prototype AI chat interface that allows you to control **EXPRESSCLUSTER** using natural language.

By leveraging **Tool Use** (also known as Function Calling), the AI can interpret natural language input and automatically map it to the appropriate functions or commands to execute. This means you can interact with EXPRESSCLUSTER without memorizing specific CLI syntax or command options.

- Anthropic Tool Use: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
- OpenAI Function Calling: https://platform.openai.com/docs/guides/function-calling

See the examples below.

```
# clpstat
 ========================  CLUSTER STATUS  ===========================
  Cluster : cluster-x600
  <server>
   *116rhel94 .......: Offline          
      lankhb1        : Offline          Kernel Mode LAN Heartbeat
      pingnp1        : Offline          ping resolution
    117rhel94 .......: Offline          
      lankhb1        : Offline          Kernel Mode LAN Heartbeat
      pingnp1        : Offline          ping resolution
  <group>
    failover1 .......: Offline          
      current        : None
      exec1          : Offline          
    failover2 .......: Offline          
      current        : None
      exec2          : Offline          
  <monitor>
    userw            : Offline          
 =====================================================================

# python3 clpaic.py
=== Command Line Suggestion System ===
Enter cluster operations in natural language (type 'exit' to quit)

>>> start cluster            

Do you want to start the cluster on all servers or just the local server?

>>> all servers

[Suggested Commands]
1. Start cluster: all servers
   Command: clpcl -s -a

Running clpcl -s -a ...
Start 116rhel94 : Command succeeded.
Start 117rhel94 : Command succeeded.

>>> I want to see the cluster status

[Suggested Commands]
1. Show cluster status
  Command: clpstat -s

Running clpstat -s ...                                      
 ========================  CLUSTER STATUS  ===========================
  Cluster : cluster-x600                                                                                                
  <server>                                                                                                              
   *116rhel94 .......: Online                                                                                           
      lankhb1        : Normal           Kernel Mode LAN Heartbeat
      pingnp1        : Normal           ping resolution                                                                 
    117rhel94 .......: Online                                                                                           
      lankhb1        : Normal           Kernel Mode LAN Heartbeat
      pingnp1        : Normal           ping resolution                                                                 
  <group>                                                                                                               
    failover1 .......: Online                                                                                           
      current        : 116rhel94                                                                                        
      exec1          : Online
    failover2 .......: Online                                                                                           
      current        : 116rhel94                                                                                        
      exec2          : Online            
  <monitor>                                                 
    userw            : Normal            
 =====================================================================

>>> move group 

Could you specify the group name you want to move? If you intend to move all groups, or move it to a specific destination server, please let me know!

>>> failover2

[Suggested Commands]
1. Move group: failover2 (according to failover policy)
   Command: clpgrp -m failover2

Running clpgrp -m failover2 ...
Command succeeded.

>>> show group status   

[Suggested Commands]
1. Show group status
   Command: clpstat -g

Running clpstat -g ...
 ======================  GROUPMAP INFORMATION  =======================
  Cluster : cluster-x600
   *server0 : 116rhel94
    server1 : 117rhel94

  --------------------------------------------------------------------
    server0 [o] : failover1[o] 
    server1 [o] : failover2[o] 
 =====================================================================
```

## Versions

There are two versions of clpaic available:

- **clpaic-local**: Operates the cluster using EXPRESSCLUSTER commands installed on the local environment.
- **clpaic-remote**: Operates the cluster using the EXPRESSCLUSTER REST API, allowing remote management without direct access to the cluster nodes.
