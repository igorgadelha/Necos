import requests, json

pdt_msg = {
    "slices": {
        "slice": {
            "id": "TouristicCDN_sliced",
            "name": "TouristicCDN_sliced",
            "short-name": "TouristicCDN_sliced",
            "description": "Slicing for Elastic Touristic CDN",
            "vendor": "MTC",
            "version": "1.0",
            "logo": "elastic-cdn.png",
            "slice-constraints": {
                "geographic": [
                    "GREECE",
                    "USA"
                ],
                "dc-slice-parts": 2,
                "net-slice-parts": 1
            },
            "slice-requirements": {
                "elasticity": True,
                "reliability": {
                    "description": "reliability level",
                    "enabled": True,
                    "value": "none"
                }
            },
            "slice-lifecycle": {
                "description": "lifecycle status",
                "status": "constuction"
            },
            "cost": {
                "dc-model": {
                    "model": "COST_PER_PHYSICAL_MACHINE_PER_DAY",
                    "value-euros": "<=10"
                }
            },
            "net-model": {
                "model": "COST_PER_LINK_PER_DAY",
                "value-euros": "<=50"
            },
            "slice-timeframe": {
                "service-duration": 480
            },
            "service": [
                {
                    "service-function": {
                        "vdu": {
                            "id": "benchmarking_clients",
                            "description": "benchmarking clients for elastic CDN",
                            "flavor": {
                                "vcpu-count": "undefined",
                                "memory-mb": "undefined",
                                "storage-mb": "undefined"
                            },
                            "hosting": "undefined",
                            "slice-part-count": 1,
                            "slice-part-ratio": 1,
                            "allocate-vdus": False,
                            "virtual-nodes-subnet": "undefined",
                            "virtual-nodes-count": "undefined",
                            "placement-type": "undefined",
                            "technology": "undefined",
                            "image": "undefined",
                            "clustering": "undefined",
                            "local-dc-controller": [
                                "swn",
                                "127.0.0.1",
                                "8080"
                            ],
                            "epa-attributes": {
                                "host-epa": {
                                    "cpu-model": "CORE2DUO",
                                    "cpu-architecture": "X86_64",
                                    "cpu-vendor": "Intel",
                                    "cpu-number": 2,
                                    "storage-gb": 120,
                                    "memory-mb": 4048,
                                    "host-range": [
                                        2,
                                        5
                                    ],
                                    "host-count": "undefined",
                                    "max-host-count": "undefined",
                                    "allocate-hosts": False,
                                    "type": "pcgb",
                                    "os-properties": {
                                        "architecture": "x86_64",
                                        "type": "linux",
                                        "distribution": "ubuntu",
                                        "version": "16.04"
                                    },
                                    "image-type": "EMULAB",
                                    "host-image": "Ubuntu-16.04-STD",
                                    "host-ips": [
                                        "195.251.209.214",
                                        "195.251.209.215",
                                        "195.251.209.216",
                                        "195.251.209.217",
                                        "195.251.209.209"
                                    ],
                                    "host-private-ips": [
                                        "10.1.0.2",
                                        "10.1.0.3",
                                        "10.1.0.4",
                                        "10.1.0.5",
                                        "10.1.0.6"
                                    ],
                                    "host-names": [
                                        "mpc12.swn.uom.gr",
                                        "mpc13.swn.uom.gr",
                                        "mpc14.swn.uom.gr",
                                        "mpc15.swn.uom.gr",
                                        "mpc7.swn.uom.gr"
                                    ],
                                    "subnet": "10.1.0"
                                },
                                "hypervisor-epa": {
                                    "type": "undefined",
                                    "version": "undefined"
                                },
                                "VIM-epa": {
                                    "name": "undefined",
                                    "type": "undefined",
                                    "version": "undefined",
                                    "on-demand": "undefined",
                                    "host-count": "undefined",
                                    "max-host-count": "undefined",
                                    "image": "undefined",
                                    "vim-shared": True,
                                    "vim-federated": False,
                                    "vim-ref": "undefined"
                                },
                                "vswitch-epa": {
                                    "type": "openvswitch",
                                    "acceleration": "PREFERRED",
                                    "offload": "PREFERRED"
                                }
                            },
                            "service-end-point": {
                                "name": "external-to-benchmarking_clients",
                                "type": "INGRESS",
                                "link-end": "wsc-eth0",
                                "application": [
                                    {
                                        "app-name": "SSH",
                                        "port": 22,
                                        "protocol": "TCP"
                                    }
                                ],
                                "requirements": {
                                    "bandwidth-GB": "MAX"
                                }
                            },
                            "dc-slice-point-of-presence": {
                                "name": "bench-if",
                                "host-ip": "195.251.209.210",
                                "private-host-ip": "10.1.0.1",
                                "host-name": "mpc8.swn.uom.gr",
                                "router-type": "GRE-HOST",
                                "reservation-protocol": "GRE",
                                "requirements": {
                                    "bandwidth": "MAX"
                                }
                            },
                            "monitoring-parameters": {
                                "tool": "collectd",
                                "measurements_db_ip": "undefined",
                                "measurements_db_port": "undefined",
                                "metrics": [
                                    {
                                        "metric": {
                                            "name": "CPU_UTILIZATION",
                                            "granularity-secs": 10
                                        }
                                    },
                                    {
                                        "metric": {
                                            "name": "MEMORY_ALLOCATION",
                                            "granularity-secs": 10
                                        }
                                    },
                                    {
                                        "metric": {
                                            "name": "BANDWIDTH_UTILIZATION",
                                            "granularity-secs": 10
                                        }
                                    }
                                ]
                            }
                        },
                        "interfaces": [
                            {
                                "service-external-interface": {
                                    "name": "wsc-eth0",
                                    "virtual-interface": {
                                        "internal-name": "eth0",
                                        "type": "VIRTIO",
                                        "bandwidth": "0",
                                        "vcpi": "0000:00:0a.0",
                                        "ip": "undefined"
                                    }
                                }
                            },
                            {
                                "service-internal-interface": {
                                    "name": "wsc-eth1",
                                    "virtual-interface": {
                                        "internal-name": "eth1",
                                        "type": "VIRTIO",
                                        "bandwidth": "0",
                                        "vcpi": "0000:00:0b.0",
                                        "ip": "undefined"
                                    }
                                }
                            },
                            {
                                "service-internal-interface": {
                                    "name": "wsc-eth2",
                                    "description": "monitoring interface",
                                    "virtual-interface": {
                                        "internal-name": "eth2",
                                        "type": "VIRTIO",
                                        "bandwidth": "0",
                                        "vcpi": "0000:00:0c.0",
                                        "ip": "undefined"
                                    }
                                }
                            }
                        ]
                    }
                },
                {
                    "service-function": {
                        "service-element-type": "vdu",
                        "vdu": {
                            "id": "web_server_VMs",
                            "description": "webserver cluster for CDN",
                            "flavor": {
                                "vcpu-count": 1,
                                "memory-mb": 128,
                                "storage-mb": 100
                            },
                            "hosting": "SHARED",
                            "slice-part-count": 1,
                            "slice-part-ratio": 1,
                            "clustering": True,
                            "allocate-vdus": True,
                            "virtual-nodes-subnet": "undefined",
                            "virtual-nodes-count": 5,
                            "placement-type": "QUANTITY",
                            "technology": "Click-os",
                            "image": "default",
                            "epa-attributes": {
                                "host-epa": {
                                    "cpu-model": "single 3GHz",
                                    "cpu-architecture": "X86_64",
                                    "cpu-vendor": "Dell",
                                    "cpu-number": 1,
                                    "storage-gb": 292,
                                    "memory-mb": 4096,
                                    "host-range": [
                                        5,
                                        6
                                    ],
                                    "host-count": "undefined",
                                    "max-host-count": "undefined",
                                    "allocate-hosts": True,
                                    "type": "d430",
                                    "os-properties": {
                                        "architecture": "x86_64",
                                        "type": "linux",
                                        "distribution": "ubuntu",
                                        "version": "16.04"
                                    },
                                    "image-type": "EMULAB",
                                    "host-image": "undefined",
                                    "host-ips": "undefined",
                                    "host-private-ips": "undefined",
                                    "host-names": "undefined",
                                    "subnet": "undefined"
                                },
                                "hypervisor-epa": {
                                    "type": "XEN",
                                    "version": "4.6"
                                },
                                "VIM-epa": {
                                    "name": "cdn-xen-vim",
                                    "type": "XEN-SERVER",
                                    "version": "7.5",
                                    "on-demand": True,
                                    "host-count": "undefined",
                                    "max-host-count": "undefined",
                                    "image": "undefined",
                                    "vim-shared": True,
                                    "vim-federated": False,
                                    "vim-ref": "cdn-xen-vim"
                                },
                                "vswitch-epa": {
                                    "type": "openvswitch",
                                    "acceleration": "PREFERRED",
                                    "offload": "PREFERRED"
                                }
                            },
                            "service-end-point": {
                                "name": "external-to-wsc",
                                "type": "INGRESS",
                                "link-end": "wsc-eth0",
                                "application": [
                                    {
                                        "app-name": "WWW",
                                        "port": 80,
                                        "protocol": "TCP"
                                    }
                                ],
                                "requirements": {
                                    "bandwidth-GB": "MAX"
                                }
                            },
                            "dc-slice-point-of-presence": {
                                "name": "wsc-if",
                                "host-ip": "undefined",
                                "private-host-ip": "undefined",
                                "host-name": "undefined",
                                "router-type": "GRE-HOST",
                                "reservation-protocol": "GRE",
                                "requirements": {
                                    "bandwidth": "MAX"
                                }
                            },
                            "monitoring-parameters": {
                                "tool": "collectd",
                                "measurements_db_ip": "undefined",
                                "measurements_db_port": "undefined",
                                "metrics": [
                                    {
                                        "metric": {
                                            "name": "CPU_UTILIZATION",
                                            "granularity-secs": 10
                                        }
                                    },
                                    {
                                        "metric": {
                                            "name": "MEMORY_ALLOCATION",
                                            "granularity-secs": 10
                                        }
                                    },
                                    {
                                        "metric": {
                                            "name": "BANDWIDTH_UTILIZATION",
                                            "granularity-secs": 10
                                        }
                                    }
                                ]
                            }
                        },
                        "interfaces": [
                            {
                                "service-external-interface": {
                                    "name": "wsc-eth0",
                                    "virtual-interface": {
                                        "internal-name": "eth0",
                                        "type": "VIRTIO",
                                        "bandwidth": "0",
                                        "vcpi": "0000:00:0a.0",
                                        "ip": "undefined"
                                    }
                                }
                            },
                            {
                                "service-internal-interface": {
                                    "name": "wsc-eth1",
                                    "virtual-interface": {
                                        "internal-name": "eth1",
                                        "type": "VIRTIO",
                                        "bandwidth": "0",
                                        "vcpi": "0000:00:0b.0",
                                        "ip": "undefined"
                                    }
                                }
                            },
                            {
                                "service-internal-interface": {
                                    "name": "wsc-eth2",
                                    "description": "monitoring interface",
                                    "virtual-interface": {
                                        "internal-name": "eth2",
                                        "type": "VIRTIO",
                                        "bandwidth": "0",
                                        "vcpi": "0000:00:0c.0",
                                        "ip": "undefined"
                                    }
                                }
                            }
                        ]
                    }
                },
                {
                    "service-link": {
                        "service-element-type": "link",
                        "link": {
                            "name": "orc-to-wsc",
                            "type": "MULTIPLEXED",
                            "ends": [
                                {
                                    "link-end-ref": "orc-eth1"
                                },
                                {
                                    "link-end-ref": "wsc-eth1"
                                }
                            ],
                            "requirements": {
                                "bandwidth-GB": 1,
                                "delay": None,
                                "jitter": None
                            },
                            "constraints": {
                                "hops": {
                                    "lower_than_equal": 2
                                }
                            },
                            "reservation-protocol": "undefined"
                        }
                    }
                }
            ]
        }
    }
}

response = requests.get("http://localhost:8000/locate_slice_resources?pdt=" + json.dumps(pdt_msg))

print(response.json())

#recebimento da msg PDT, através de uma msg SRA, com os campos da requisição preenchido
