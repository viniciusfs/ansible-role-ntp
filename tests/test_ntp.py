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


def test_step_tickers_file(File):
    ntp_conf = File('/etc/ntp/step-tickers')
    assert ntp_conf.user == 'root'
    assert ntp_conf.group == 'root'
    assert ntp_conf.mode == 0664


def test_sysconfig_clock_file(File):
    ntp_conf = File('/etc/sysconfig/clock')
    assert ntp_conf.user == 'root'
    assert ntp_conf.group == 'root'
    assert ntp_conf.mode == 0644


def test_ntp_running_and_enabled(Service):
    ntpd = Service('ntpd')
    assert ntpd.is_running
    assert ntpd.is_enabled
