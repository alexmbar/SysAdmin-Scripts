#powershell -f FirewallContpaqi.ps1
$puertos = @(9079, 9080, 9081, 9082, 9009, 1099, 1139, 1775, 2003, 1139, 9047, 9020, 9005, 23165, 9015, 9012, 1433, 1434, 443, 15443, 7653)

foreach ($puerto in $puertos) {
    # Permitir tráfico de entrada al puerto
    New-NetFirewallRule -DisplayName "Contpaqi Inbound $puerto" -Direction Inbound -Protocol TCP -LocalPort $puerto -Action Allow

    # Permitir tráfico de salida al puerto
    New-NetFirewallRule -DisplayName "Contpaqi Outbound $puerto" -Direction Outbound -Protocol TCP -LocalPort $puerto -Action Allow
}
