# Ansible role: NTP

Install and configure NTP client in Linux systems.

## Role Variables

Name | Description | Default value
-----|-------------|--------------
`ntp_config_enabled` | Enable service at boot time | true
`ntp_config_servers` | List of NTP servers to sync | `[ "a.ntp.br", "b.ntp.br", "c.ntp.br" ]`
`ntp_config_timezone` | Server time zone | `America/Sao_Paulo`


## Example Playbook

    - hosts: servers
      roles:
        - { role: viniciusfs.ntp }


## License

MIT


## Author Information

* Vinícius Figueiredo <viniciusfs@gmail.com>
