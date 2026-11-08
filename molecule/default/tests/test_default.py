def test_nginx_instalado_e_rodando(host):
    # 1. Pacote instalado
    assert host.package("nginx").is_installed

    # 2. Serviço rodando e habilitado no boot
    servico = host.service("nginx")
    assert servico.is_running
    assert servico.is_enabled

    # 3. Porta 80 escutando
    assert host.socket("tcp://0.0.0.0:80").is_listening