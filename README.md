# Ansible role: NTP

Install and configure NTP client in Linux systems.


## Role Variables

* `ntp_config_enabled`:
    - Description: Enable service at boot time
    - Values: `True | False`
    - Default: `True`

* `ntp_config_servers`:
    - Description: List of NTP ervers to sync
    - Default: `[ "0.pool.ntp.org", "1.pool.ntp.org", "2.pool.ntp.org" ]`

* `ntp_config_timezone`:
    - Description: Server time zone
    - Default: `America/Sao_Paulo`


## Example Playbook

    - hosts: servers
      roles:
        - { role: viniciusfs.ntp }


## License

MIT


## Author Information

* Vinícius Figueiredo <viniciusfs@gmail.com>
