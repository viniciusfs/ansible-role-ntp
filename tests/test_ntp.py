import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_ntp_is_installed(Package):
    ntp = Package('ntp')
    assert ntp.is_installed


def test_ntp_conf_file(File):
    ntp_conf = File('/etc/ntp.conf')
    assert ntp_conf.user == 'root'
    assert ntp_conf.group == 'root'
    assert ntp_conf.mode == 0664
    assert ntp_conf.contains('server 0.pool.ntp.org iburst')
    assert ntp_conf.contains('server 1.pool.ntp.org iburst')
    assert ntp_conf.contains('server 2.pool.ntp.org iburst')


def test_step_tickers_file(File):
    step_tickers = File('/etc/ntp/step-tickers')
    assert step_tickers.user == 'root'
    assert step_tickers.group == 'root'
    assert step_tickers.mode == 0664
    assert step_tickers.contains('0.pool.ntp.org')
    assert step_tickers.contains('1.pool.ntp.org')
    assert step_tickers.contains('2.pool.ntp.org')


def test_localtime_file(File):
    localtime = File('/etc/localtime')
    assert localtime.is_symlink
    assert localtime.linked_to == '/usr/share/zoneinfo/America/Sao_Paulo'


def test_sysconfig_clock_file(File):
    sysconfig_clock = File('/etc/sysconfig/clock')
    assert sysconfig_clock.user == 'root'
    assert sysconfig_clock.group == 'root'
    assert sysconfig_clock.mode == 0644
    assert sysconfig_clock.contains('ZONE=America/Sao_Paulo')


def test_ntp_running_and_enabled(Service):
    ntpd = Service('ntpd')
    assert ntpd.is_running
    assert ntpd.is_enabled
